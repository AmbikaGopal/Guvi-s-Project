import mysql.connector
from faker import Faker
fake = Faker()
Faker.seed(42)
from datetime import datetime
import random


conn = mysql.connector.connect(host = "127.0.0.1", user="root", 
                                     password="1GopiAmbi!", database="placement_app")
cursor=conn.cursor()
cursor.execute('SET FOREIGN_KEY_CHECKS = 0')
cursor.execute('Truncate table Placements')
cursor.execute('Truncate table Soft_Skills')
cursor.execute('Truncate table Programming')
cursor.execute('Truncate table Students')
cursor.execute('SET FOREIGN_KEY_CHECKS = 1')
conn.commit()
print('All the tables are truncated')

students_data = []

for _ in range(300):
  Name = fake.name()
  dob = fake.date_of_birth(minimum_age=18, maximum_age=59)
  Age=random.randint(23,42)
  Gender = random.choice(['Male', 'Female','Other'])
  Email = fake.unique.email()
  Phone = fake.unique.phone_number()
    # self.enrollment_id = f"ENR{random.randint(100000,999999)}"
  current_year = datetime.now().year
  Enrollment_year = random.randint(current_year -10, current_year -4)
  batch_number = random.randint(1,5)
  course_batch= f'Batch-{str(batch_number)}'
  city=fake.city()
  duration=random.choice([3,4])
  completion_year = Enrollment_year + duration
  graduation_year= completion_year + random.choice([0,1])
  # students_data.append((fake.name()))

  students_data.append((Name,Age,Gender,Email,Phone,Enrollment_year,course_batch,city,graduation_year))
# print(students_data)

Stu_query=""" insert into Students(Name, Age, Gender, Email, Phone, Enrollment_year, 
                            course_batch, city, graduation_year)
           values(%s,%s,%s,%s,%s,%s,%s,%s,%s) """
cursor.executemany(Stu_query, students_data)
conn.commit()
print("Inserted the data into Students table")

cursor.execute('select student_id from students')
rows=cursor.fetchall()
# print(rows)
student_ids = []
# print(student_ids) # Empty List
for row in rows:
  student_ids.append(row[0])
# print(student_ids) # Appends all the student_ids in students table

Programming_data = []
for Student_id in student_ids:
  Language=random.choice(["SQL",'Python','Java','R'])
  Problems_solved=random.randint(0,100)
  Assessments_completed=random.randint(0,40)
  enrollment_id = f"ENR{random.randint(100000,999999)}"
  enrollment_date = fake.date_between(start_date='-4y', end_date='today')
  Project_Completed=random.randint(0,20)
  Mini_Projects=random.randint(5,12)
  Certificates_Earned=random.randint(3,9)
  Latest_Project_Score=random.randint(6,10)
  Programming_data.append((Student_id, Language, Problems_solved, Assessments_completed, Mini_Projects,
     Certificates_Earned,Latest_Project_Score))

Program_query=""" insert into Programming(student_id,Language,Problems_solved,Assessments_Completed,Mini_Projects,Certificates_Earned,
              Latest_Project_Score) values(%s,%s,%s,%s,%s,%s,%s) """
cursor.executemany(Program_query, Programming_data)
conn.commit()
print("Values are inserted into Programming Table")

Soft_Skills_data = []
for Student_id in student_ids:
  Communication=random.randint(0,100)
  Teamwork=random.randint(0,100)
  Presentation=random.randint(0,100)
  Leadership = random.randint(0,100)
  Critical_Thinking=random.randint(0,100)
  Interpersonal_Skills=random.randint(0,100)
  Soft_Skills_data.append((Student_id,Communication, Teamwork,Presentation,Leadership,Critical_Thinking,Interpersonal_Skills))

soft_query = """ insert into Soft_Skills(Student_id,Communication, Teamwork,Presentation,Leadership,Critical_Thinking,Interpersonal_Skills)
             values(%s,%s,%s,%s,%s,%s,%s)"""

cursor.executemany(soft_query,Soft_Skills_data)
conn.commit()
print("Values are inserted into Soft Skills Table")

Placement_Data = []
for Student_id in student_ids:
  Mock_Interview_Score = random.randint(0,100)
  Internships_Completed = random.randint(2,8)
  Placement_Status = random.choice(['Ready','Not Ready','Placed'])
  if Placement_Status == 'Placed':
    Company_Name=random.choice(['Infosys','TCS','Wipro','Accenture','Mindtree','L&T','HCL','CTS','Bosch','Virtusa'])
    Placement_package=round(random.uniform(350000, 5000000), 2)
    Interview_rounds_cleared=random.randint(2,4)
    Placement_Date=fake.date_between(start_date='-5y', end_date='-1d')
  else:
    Company_Name=None
    Placement_package=0.0
    Interview_rounds_cleared=0
    Placement_Date=None
  Placement_Data.append((Student_id, Mock_Interview_Score, Internships_Completed, Placement_Status, Company_Name,
                         Placement_package, Interview_rounds_cleared, Placement_Date))
  placement_query=""" insert into Placements(Student_id, Mock_Interview_Score, Internships_Completed, Placement_Status, Company_Name,
                         Placement_package, Interview_rounds_cleared, Placement_Date)
                         values(%s,%s,%s,%s,%s,%s,%s,%s)"""
cursor.executemany(placement_query, Placement_Data)
conn.commit()
print("Inserted values into placement table")


cursor.close()
conn.close()
