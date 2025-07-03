import streamlit as st
from Placement_App.Db import Database
import mysql.connector
import pandas as pd
import numpy as np

st.title('Placement Eligibility Checker')

d=Database(host="127.0.0.1", user="root", password="1GopiAmbi!", database='placement_app')
students = d.fetch_all_students()
# st.write(students)

# option = st.selectbox('What you want to view?', ('title','num'),) 
# st.write("You selected to view", option)

option=st.sidebar.selectbox('Select a Page',('Home','Students','Check the eligibility','Technical Skills','Companies','Analytics'))
# st.write(option,'Page')

if option =='Home':
    st.title("Welcome to Home Page")
    st.write("Use side bar to navigate")

if option=='Students':
    st.header('Welcome to Students Page')
    st.write("Students Table:")
    st.write("Below is the list of the students")
    d=Database(host="127.0.0.1", user="root", password="1GopiAmbi!", database='placement_app')
    students = d.fetch_all_students()
    # st.table(students)
    st.dataframe(students)

if option=="Check the eligibility":
    st.subheader("Please check the eligibility of student based on Programming Language")
    min_problems = st.sidebar.number_input('Minimum problems solved', min_value=0, max_value=100, value=50)
    min_communication = st.sidebar.number_input('Minimum Communication Score',min_value=0,max_value=100, value=45)
    Programming_Language = st.sidebar.radio('Preferred Programming Language:', ["SQL",'Python','Java','R'])
    if Programming_Language:
        query = f'''
    select s.name, s.course_batch, p.language, p.problems_solved, ss.communication from students s
    join programming p on s.Student_Id = p.Student_Id
    join soft_skills ss on s.Student_Id = ss.Student_Id where
    (p.problems_solved>={min_problems} and ss.communication>={min_communication}) and p.language=%s '''

        d.cursor.execute(query,(Programming_Language,))
        eligible_students = d.cursor.fetchall()

        st.write(f'Display the student data for atleaset {min_problems} problems solved and communication score is {min_communication}')
        st.dataframe(eligible_students)

if option== "Technical Skills": 
    st.header("Selected students based on their Technical Skills")
    Programming_Language = st.sidebar.radio('Preferred Programming Language:', ["SQL",'Python','Java','R'])
    st.write(f"Selected programming language : **{Programming_Language}**")
    if Programming_Language:
        lan = '''
          SELECT s.name, s.email, s.phone, s.city,
           p.Programming_Id, p.language, p.problems_solved, p.assessments_completed
                FROM students s
              JOIN programming p ON s.Student_Id = p.student_Id
             WHERE p.language = %s
    '''

    # Wrap the string in a tuple correctly
        d.cursor.execute(lan, (Programming_Language,))
        prog_stus = d.cursor.fetchall()
        df = pd.DataFrame(prog_stus)
        if not df.empty:
            st.write(f"🎯 Students with specific technical skills:")
            st.dataframe(df)
        else:
            st.warning("⚠️ No students found with the selected languages.")

if option=="Companies":
    st.header('List of companies with high package yearly')
    company=""" SELECT
    pl.company_name, YEAR(pl.placement_date) AS year, pl.placement_package FROM placements pl
JOIN (
    SELECT YEAR(placement_date) AS year, MAX(placement_package) AS max_package FROM placements WHERE placement_status = 'Placed'
    GROUP BY YEAR(placement_date)
) AS yearly_max
ON YEAR(pl.placement_date) = yearly_max.year
   AND pl.placement_package = yearly_max.max_package
WHERE pl.placement_status = 'Placed'
ORDER BY year DESC
LIMIT 0, 50;"""
    d.cursor.execute(company)
    company_list=d.cursor.fetchall()
    view=pd.DataFrame(company_list)
    st.dataframe(view)

    
if option=="Analytics":
    st.subheader("Analytics Dashboard")
    st.markdown('### 1. Average Programming Performance Per Batch')
    query1 = '''
select s.course_batch,
avg(p.problems_solved) as Avg_Problems_Solved,
avg(p.assessments_completed) as Avg_Assessments,
avg(p.mini_projects) as Avg_Mini_Projects,
avg(certificates_Earned) as Avg_Certifications_Earned
from students s join programming p on s.student_Id=p.student_Id
group by s.course_batch'''
    d.cursor.execute(query1)
    view1=d.cursor.fetchall()

    if len(view1)>0:
        st.dataframe(view1)
    else:
        st.warning("No data for programming performance")

    st.markdown('### 2. Top five students by mini_projects')
    query2="""
select s.student_id, s.name, s.course_batch, p.mini_projects from students s 
join programming p on s.student_id = p.student_id order by p.mini_projects desc limit 5"""
    d.cursor.execute(query2)
    view2=d.cursor.fetchall()

    if len(view1)>0:
        st.dataframe(view2)
    else:
        st.write("No students with more mini_projects")

    st.markdown('### 3. Language Summary as maximum values')
    query3="""
select p.language, max(p.problems_solved) as Maximum_Problems_Solved, max(p.assessments_completed) as Maximum_Assessments_Completed,
max(p.mini_projects) as Maximum_Mini_Projects, max(p.certificates_earned) as Maximum_Certificates_Earned, max(p.latest_project_score) as 
Maximum_Latest_Project_Score from students s join programming p on s.student_id =p.student_id group by p.language"""
    d.cursor.execute(query3)
    view3=d.cursor.fetchall()
    st.dataframe(view3)

    st.markdown('### 4. Soft_Skills Summary')
    soft_skill=st.sidebar.radio('Preferred Soft Skill:', ["Communication",'Teamwork','Presentation','Leadership',"Critical_thinking","Interpersonal_Skills"])
    
    st.write(f"Preferred Soft Skill is **{soft_skill}**")
    if soft_skill:
        query4=f"""
select s.name, ss.communication, ss.Teamwork, ss.Presentation, 
ss.Leadership,ss.critical_thinking, ss.Interpersonal_skills
from students s 
join Soft_skills ss on s.student_id = ss.student_id 
order by {soft_skill} desc limit 50"""
    d.cursor.execute(query4)
    ss = d.cursor.fetchall()
    view4 = pd.DataFrame(ss)
    st.dataframe(view4)

    st.markdown('### 5. Programming Summary')
    language=st.sidebar.radio('Preferred Programming Language:', ["SQL",'Python','Java','R'])
    Criteria=st.sidebar.radio('Preferred criteria:', ['problems_solved', "assessments_completed", "mini_projects", 
"certificates_earned", "latest_project_score"])
    st.write(f"Preferred Programming language is **{language}**")
    if language:
        query5=f"""
select s.name, p.programming_id, p.language, p.problems_solved, p.assessments_completed, p.mini_projects, 
p.certificates_earned, p.latest_project_score from students s join programming p on
s.student_id=p.student_id where language = %s order by {Criteria} desc"""
    d.cursor.execute(query5,(language,))
    p=d.cursor.fetchall()
    p1=pd.DataFrame(p)
    st.dataframe(p)

    st.markdown('### 6. Placement Summary')
    Status=st.sidebar.radio('Status of the student:',['Ready','Placed','Not Ready'])
    query6=f"""
select s.name, pl.* from placements pl join students s on pl.student_id = s.student_id where pl.placement_status = %s"""
    st.write(f"Criteria of the students for Placement is **{Status}**")
    d.cursor.execute(query6,(Status,))
    s=d.cursor.fetchall()
    s1=pd.DataFrame(s)
    st.dataframe(s1)

    st.markdown('### 7. Overall Language Summary')
    if language:
        query7="""
select s.name, p.language, p.problems_solved, p.assessments_completed, p.mini_projects, 
p.certificates_earned, p.latest_project_score, ss.communication, ss.teamwork,ss.presentation,ss.leadership, 
ss.critical_thinking, ss.interpersonal_skills, pl.placement_status from students s 
join programming p on s.student_id=p.student_id 
join soft_skills ss on s.student_id = ss.student_id
join placements pl on s.student_id = pl.student_id where language = %s ORDER BY {Criteria} DESC limit 10"""
    d.cursor.execute(query5,(language,))
    o=d.cursor.fetchall()
    o1=pd.DataFrame(o)
    st.dataframe(o1)

    st.markdown('### 8. Students with mini projects count')
    project_count = st.sidebar.number_input('Mini Projects completed', min_value=5, max_value=12, value=5)
    query8=f"""
select s.name,s.course_batch, s.graduation_year,p.mini_projects from students s 
join programming p on s.student_id=p.student_id where mini_projects={project_count}"""
    d.cursor.execute(query8)
    q=d.cursor.fetchall()
    view8=pd.DataFrame(q)
    if len(view8)>5:
        st.dataframe(view8)
    else:
        st.warning("No Student found with 0 mini projects")


    st.markdown('### 9. Student with Internships Completed')
    inter_count = st.sidebar.number_input('Interships completed', min_value=2, max_value=8, value=2)
    query9=f"""select s.name, s.email,s.phone, s.enrollment_year, s.course_batch, s.graduation_year, pl.Internships_completed
    from students s join placements pl on s.student_id = pl.student_id where internships_completed = {inter_count}
"""
    d.cursor.execute(query9)
    q1=d.cursor.fetchall()
    view9=pd.DataFrame(q1)
    if len(view9)>2:
        st.dataframe(view9)
    else:
        st.warning("No students with lessthan 2 internships")

    st.markdown("### 10. Top 10 Students with high placement package")
    query10=f"""select s.name, s.email,s.phone,s.course_batch, s.graduation_year,pl.interview_rounds_cleared, pl.placement_package
    from students s join placements pl on s.student_id=pl.student_id where placement_status = 'placed'
    order by placement_package desc limit 10"""
    
    d.cursor.execute(query10)
    q2=d.cursor.fetchall()
    view10=pd.DataFrame(q2)
    st.dataframe(view10)

    st.markdown(f"### 11. Students placed with high package with {language} as a skill")
    if language:
        query11=f""" select s.name, s.email, s.graduation_year, p.language, pl.placement_package
    from students s join programming p on s.student_id=p.student_id
    join placements pl on s.student_id=pl.student_id where pl.placement_status='placed' and p.language= %s
    order by pl.placement_package desc """
    d.cursor.execute(query11,(language,))
    q3=d.cursor.fetchall()
    view11=pd.DataFrame(q3)
    st.dataframe(view11)

    st.markdown('### 12. List of students who are all placed')
    query12="""select s.name, s.email, s.graduation_year, pl.placement_status from students s join placements pl on
    s.student_id=pl.student_id where pl.placement_status='Placed' """
    d.cursor.execute(query12)
    q4=d.cursor.fetchall()
    view12=pd.DataFrame(q4)
    st.dataframe(view12)

    st.markdown('### 13. Total number of students based on placement_status')
    query13="""select placement_status,count(*) as Total_No_of_Students from placements group by placement_status"""
    d.cursor.execute(query13)
    q5=d.cursor.fetchall()
    view13=pd.DataFrame(q5)
    st.dataframe(view13)

    st.markdown('### 14. Packages provided by each company')
    query14=""" select company_name, max(placement_package) as Maximum_Package, avg(placement_package) as Average_Package,
    min(placement_package) as Minimum_Package from placements where placement_status='Placed' group by company_name"""
    d.cursor.execute(query14)
    q6=d.cursor.fetchall()
    view14=pd.DataFrame(q6)
    st.dataframe(view14)

    st.markdown('### 15. Top 10 students placed in companies with high packages')
    query15=""" select s.name, pl.company_name, pl.placement_package from students s join placements pl on s.student_id=pl.student_id 
    where placement_status='Placed' order by placement_package desc limit 10"""
    d.cursor.execute(query15)
    q7=d.cursor.fetchall()
    view15=pd.DataFrame(q7)
    st.dataframe(view15)

    st.markdown('### 16. Details of students who are ready to attend an interview')
    query16="""select s.name, p.language,p.mini_projects,p.certificates_earned, p.latest_project_score,pl.internships_completed from 
    students s join programming p on s.student_id=p.student_id
    join placements pl on s.student_id=pl.student_id where placement_status='ready' """

    d.cursor.execute(query16)
    q8=d.cursor.fetchall()
    view16=pd.DataFrame(q8)
    st.dataframe(view16)
    
        







 
