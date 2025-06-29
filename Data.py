from faker import Faker
fake = Faker()
Faker.seed(42)
from datetime import date
import random

#Student table
class Students_Table():
  def __init__(self):
    self.name = fake.name()
    self.dob = fake.date_of_birth(minimum_age=18, maximum_age=59)
    self.age=random.randint(23,42)
    self.phone_number = fake.phone_number()
    self.enrollment_id = f"ENR{random.randint(100000,999999)}"
    self.enrollment_date = fake.date_between(start_date='-4y', end_date='today')
    self.problems_solved=random.randint(0,100)
    self.Assessment_completed=random.randint(0,40)
    self.Project_Completed=random.randint(0,20)
    self.Communication=random.randint(0,100)
    self.Teamwork=random.randint(0,100)
    self.Presentation=random.randint(0,100)

  def Student(self):
    print(self.name)
    # Generate a dob
    #calculate age from dob
    dob=date.today()
    print(self.age)
    print(self.phone_number)
    print(self.enrollment_id)
    print(self.enrollment_date)

  def Program(self):
    print(self.problems_solved)
    print(self.Assessment_completed)
    print(self.Project_Completed)

  def SoftSkills(self):
    print(self.Communication)
    print(self.Teamwork)
    print(self.Presentation)

  def Placements(self):
    print(self.Communication)
    print(self.Teamwork)
    print(self.Presentation)

s=Students_Table()
s.Student()
s.Program()
s.SoftSkills()
s.Placements()

