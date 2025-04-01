from django.db import models
from Admin. models import*
class tbl_healthreport(models.Model):
   healthreport_date=models.DateField(auto_now_add=True)
   healthreport_details=models.CharField(max_length=200)
   health_staff=models.ForeignKey(tbl_healthstaff,on_delete=models.CASCADE)
   juvenile=models.ForeignKey(tbl_juvenile,on_delete=models.CASCADE)