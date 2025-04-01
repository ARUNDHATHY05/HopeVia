from django.db import models
from Admin.models import*
class tbl_rehabilitationreport(models.Model):
     rehabilitationreport_date=models.DateField(auto_now_add=True)
     rehabilitationreport_details=models.CharField(max_length=200)
     rehabilitation_staff=models.ForeignKey(tbl_rehabilitationstaff,on_delete=models.CASCADE)
     juvenile=models.ForeignKey(tbl_juvenile,on_delete=models.CASCADE)