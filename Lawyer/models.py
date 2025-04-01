from django.db import models
from Lawyer.models import*
from Admin.models import*

class tbl_hearing(models.Model):
  hearing_date=models.DateField()
  hearing_status=models.IntegerField(default=0)
  juvenile=models.ForeignKey(tbl_juvenile,on_delete=models.CASCADE)
  juvenile_fordate=models.DateField()
  amount=models.CharField(max_length=50)