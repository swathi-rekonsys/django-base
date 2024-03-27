from django.db import models

# Create your models here.
class SwatiDetails(models.Model):
    login_name=models.CharField(max_length=100)
    login_id=models.CharField(max_length=100)
    desg=models.CharField(max_length=100)
    salary=models.IntegerField()
    exp=models.IntegerField()
    company=models.CharField(max_length=100)
    phone_no=models.BigIntegerField()
    address=models.CharField(max_length=100)
