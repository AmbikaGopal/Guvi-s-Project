import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user='root',
    password= '1GopiAmbi!',
    database= 'placement_app'
)

cursor=mydb.cursor()

cursor.execute('''
create table if not exists Students(
    Student_Id int auto_increment primary key,
    Name varchar(30),
    Age int,
    Gender varchar(8),
    Email varchar(250),
    Phone varchar(20),
    Enrollment_Year int,
    Course_Batch varchar(10),
    City varchar(50),
    Graduation_Year int) 
''')

print('Students table created sucessfully')

cursor.execute('''
create table if not exists Programming(
    Programming_Id int auto_increment primary key,
    Student_Id int,
    Language varchar(70),
    Problems_Solved int,
    Assessments_Completed int,
    Mini_Projects int,
    Certificates_Earned int,
    Latest_Project_Score int,
    foreign key(Student_Id) references Students(Student_Id)) 
''')
print("Programming Table created sucessfully")

cursor.execute('''
create table if not exists Soft_Skills(
    Soft_Skill_Id int auto_increment primary key,
    Student_Id int,
    Communication int,
    Teamwork int,
    Presentation int,
    Leadership int,
    Critical_Thinking int,
    Interpersonal_skills int,
    foreign key(Student_Id) references Students(Student_Id)) 
''')
print("Soft Skills Table created sucessfully")

cursor.execute('''
create table if not exists Placements(
    Placement_Id int auto_increment primary key,
    Student_Id int,
    Mock_Interview_Score int,
    Internships_Completed int,
    Placement_Status varchar(15),
    Company_Name varchar(15),
    Placement_package varchar(40),
    Interview_rounds_cleared int(10),
    Placement_Date varchar(17),
    foreign key(Student_Id) references Students(Student_Id))
''')
print("Placements table created sucessfully")
print("All Tables created")

cursor.close()
mydb.close()