from django.db import models
from Admin.models import*
# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=30)


class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=30)
    admin_email=models.CharField(max_length=30)
    admin_password=models.CharField(max_length=30)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)

class tbl_subcategory(models.Model):
    category_id=models.ForeignKey(tbl_category,on_delete=models.CASCADE)
    subcategory_name=models.CharField(max_length=50)

class tbl_lawyer(models.Model):
    lawyer_name=models.CharField(max_length=30)
    lawyer_email=models.CharField(max_length=30)
    lawyer_contact=models.CharField(max_length=10)
    lawyer_address=models.CharField(max_length=100)
    lawyer_photo=models.FileField(upload_to="Assets/Admin/Photo/")
    lawyer_proof=models.FileField(upload_to="Assets/Admin/Photo/")
    lawyer_password=models.CharField(max_length=15)


class tbl_casetype(models.Model):
    case_type=models.CharField(max_length=100)


class tbl_parent(models.Model):
    parent_name=models.CharField(max_length=30)
    parent_email=models.CharField(max_length=30)
    parent_contact=models.CharField(max_length=13)
    parent_address=models.CharField(max_length=100)
    parent_photo=models.FileField(upload_to="Assets/Parent/Photo/")
    parent_proof=models.FileField(upload_to="Assets/Parent/Proof/")
    parent_password=models.CharField(max_length=15)
    parent_role=models.CharField(max_length=50)


class tbl_juvenile(models.Model):
    juvenile_name=models.CharField(max_length=30)
    juvenile_age=models.CharField(max_length=2)
    juvenile_gender=models.CharField(max_length=10)
    juvenile_height=models.CharField(max_length=10)
    juvenile_weight=models.CharField(max_length=10)
    juvenile_address=models.CharField(max_length=100)
    juvenile_photo=models.FileField(upload_to="Assets/Admin/Photo")
    juvenile_proof=models.FileField(upload_to="Assets/Admin/Proof")
    lawyer=models.ForeignKey(tbl_lawyer,on_delete=models.CASCADE)
    parent=models.ForeignKey(tbl_parent,on_delete=models.CASCADE,null=True)
    juvenile_dob=models.DateField(null=True)
    juvenile_admissiondate=models.DateField(null=True)


class tbl_case(models.Model):
   case_name=models.CharField(max_length=30)
   case_details=models.CharField(max_length=100)
   case_date=models.DateField(auto_now_add=True)
   casetype=models.ForeignKey(tbl_casetype,on_delete=models.CASCADE)
   juvenile=models.ForeignKey(tbl_juvenile,on_delete=models.CASCADE)



class tbl_healthstaff(models.Model):
    healthstaff_name=models.CharField(max_length=30)
    healthstaff_email=models.EmailField()
    healthstaff_contact=models.CharField(max_length=11)
    healthstaff_password=models.CharField(max_length=30)
    hlt_status=models.IntegerField(default=0)
    
class tbl_rehabilitationstaff(models.Model):
    rehabilitationstaff_name=models.CharField(max_length=30)
    rehabilitationstaff_email=models.EmailField()
    rehabilitationstaff_contact=models.CharField(max_length=11)
    rehabilitationstaff_password=models.CharField(max_length=30)
    rehab_status=models.IntegerField(default=0)

class tbl_educationalstaff(models.Model):
    educationalstaff_name=models.CharField(max_length=30)
    educationalstaff_email=models.EmailField()
    educationalstaff_contact=models.CharField(max_length=11)
    educationalstaff_password=models.CharField(max_length=30)
    ed_status=models.IntegerField(default=0)

class tbl_assignedustf(models.Model):
    juvenile=models.ForeignKey(tbl_juvenile,on_delete=models.CASCADE)
    educationalstaff=models.ForeignKey(tbl_educationalstaff,on_delete=models.CASCADE)

class tbl_assignhltstf(models.Model):
    juvenile=models.ForeignKey(tbl_juvenile,on_delete=models.CASCADE)
    healthstaff=models.ForeignKey(tbl_healthstaff,on_delete=models.CASCADE)

class tbl_assignrehabstf(models.Model):
    juvenile=models.ForeignKey(tbl_juvenile,on_delete=models.CASCADE)
    rehabilitationstaff=models.ForeignKey(tbl_rehabilitationstaff,on_delete=models.CASCADE)









