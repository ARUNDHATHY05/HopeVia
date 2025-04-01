from django.db import models
from Admin.models import*
class tbl_educationalreport(models.Model):
  educationalreport_date=models.DateField(auto_now_add=True)
  educationalreport_details=models.CharField(max_length=200)
  educational_staff=models.ForeignKey(tbl_educationalstaff,on_delete=models.CASCADE)
  juvenile=models.ForeignKey(tbl_juvenile,on_delete=models.CASCADE)
