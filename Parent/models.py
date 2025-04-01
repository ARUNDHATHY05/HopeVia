from django.db import models
from Admin.models import *
class tbl_complaint(models.Model):
    complaint_content=models.CharField(max_length=100)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_status=models.IntegerField(default=0)
    complaint_reply=models.CharField(max_length=100,default="Not Yet Replyed")
    parent=models.ForeignKey(tbl_parent,on_delete=models.CASCADE)

class tbl_appointment(models.Model):
    appointment_details=models.CharField(max_length=250)
    appointment_date=models.DateField(auto_now_add=True)
    appointment_status=models.IntegerField(default=0)
    appointment_fordate=models.DateField()
    appointment_fortime=models.TimeField()
    juvenile=models.ForeignKey(tbl_juvenile,on_delete=models.CASCADE)