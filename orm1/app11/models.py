from django.db import models

class Employeedata(models.Model):
    emp_name=models.CharField(max_length=50)
    emp_id=models.IntegerField()
    emp_phno=models.IntegerField()
    emp_cmpname=models.CharField(max_length=60)
    emp_status=models.TextField()
    emp_address=models.TextField()
    
