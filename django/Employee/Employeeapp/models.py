from django.db import models

# Create your models here.
class EmployeeDetails(models.Model):
    emp_name=models.CharField(max_length=100)
    emp_id=models.CharField(max_length=100)
    desg=models.CharField(max_length=100)
    salary=models.IntegerField()
    exp=models.IntegerField()
    company=models.CharField(max_length=100)
    phone_number=models.BigIntegerField()
    address=models.CharField(max_length=100)
