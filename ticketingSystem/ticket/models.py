from django.db import models

# Create your models here.
from pyexpat import model
from random import choices
from django.db import models
from django.contrib.auth.models import User
from django.forms import IntegerField
from datetime import datetime

SEMESTER_CHOICES =(
    ("1",1),
    ("2",2),
)


# Create your models her
class UserProfile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    role=models.CharField(max_length=20,choices=SEMESTER_CHOICES,default=1)
    is_active=models.BooleanField(default=True)
    phone_number=models.IntegerField(blank=True)
    department_name=models.ForeignKey('Department',on_delete=models.CASCADE,default=None,blank=True,null=True)
    def __str__(self):
        return self.user

class Department(models.Model):
    name=models.CharField(max_length=20)
    created_date=models.DateTimeField(default=datetime.now,blank=False)
    def __str__(self):
        return self.name

class TicketStatus(models.TextChoices):
    TO_DO='To Do'
    IN_PROGRESS= 'In Progress'
    IN_REVIEW ='In Review'
    DONE ='Done'

class Ticket(models.Model):
    title=models.CharField(max_length=20)
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=False,blank=False)
    Department_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    description=models.CharField(max_length=600,blank=True,null=True)
    status=models.CharField(max_length=30,choices=TicketStatus.choices,default=TicketStatus.TO_DO)
    