from django.db import models

# Create your models here.
from datetime import *
class Student_profile(models.Model):
    Std_id=models.CharField(max_length=50)
    Std_name=models.CharField(max_length=100)
    Std_profile=models.ImageField(upload_to="std_profile",null=True,blank=True)

class Employee_profile(models.Model):
    Emp_id=models.CharField(max_length=50)
    Emp_name=models.CharField(max_length=100)
    Emp_profile=models.ImageField(upload_to='emp_profile',null=True,blank=True)
    Emp_resume=models.FileField(upload_to='emp_resume',null=True,blank=True)
    

class parent(models.Model):
    App_Id=models.CharField(max_length=10)
    Name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=150)
    Mobile=models.CharField(max_length=10)

grade=[
    ('A',"A"),
    ('B',"B"),
    ('C','C')
]

classes=[
    ('8',"8th"),
    ('9',"9th"),
    ('10','10th')
]

class Student(parent):
    Roll_no=models.CharField(max_length=12)
    Class=models.CharField(choices=classes,max_length=20)
    Grade=models.CharField(choices=grade,max_length=20)

class Employee(parent):
    Emp_id=models.CharField(max_length=12)
    Emp_designation=models.CharField(max_length=100)
    Emp_salary=models.CharField(max_length=50)

project=[
    ('p1',"Ecommers"),
    ('p2',"LMS"),
    ('p3','Admin')
]
 
class Project_info(Employee):
    Project_name=models.CharField(choices=project,max_length=30)
    Project_dead_line=models.DateTimeField(default=datetime.now())
    Project_client=models.CharField(max_length=100)
'''
class parent1(models.Model):
    emp_id=models.BigAutoField(primary_key=True)
    Emp_designation=models.CharField(max_length=100)
    Emp_exp=models.IntegerField()
    Emp_sal=models.CharField(max_length=10)


company=[
    ('ABC',"ABC"),
    ('BCA',"BCA"),
    ('KPP','KPP')
]

class Placement(parent,parent1):
    placed_company=models.CharField(choices=company)
    # if any two fields are common in parents in an multiple inheritence will not be acceptable.
    '''

class Applicants(models.Model):
    Applicant_id=models.CharField(max_length=10,null=False,blank=False)
    Applicant_name=models.CharField(max_length=50)
    Applicant_email=models.EmailField(max_length=100)
    Applicant_mobile=models.CharField(max_length=10)
    
    def __str__(self):
        return str(f'{self.Applicant_id} => {self.Applicant_name}')
    
    
class JobApplication(models.Model):
    Applicant_info=models.OneToOneField(Applicants,on_delete=models.CASCADE)
