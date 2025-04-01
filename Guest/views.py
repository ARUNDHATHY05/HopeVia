from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import*

def Parent(request):
    pdata=tbl_parent.objects.all()
    if request.method=='POST':
        pname=request.POST.get('name')
        pemail=request.POST.get('email')
        pcontact=request.POST.get('contact')
        padd=request.POST.get('address')
        ppic=request.FILES.get('photo')
        pprf=request.FILES.get('proof')
        ppass=request.POST.get('password')
        tbl_parent.objects.create(parent_name=pname,parent_email=pemail,parent_contact=pcontact,parent_address=padd,parent_photo=ppic,parent_proof=pprf,parent_password=ppass)
        return render(request,'Guest/ParentReg.html',{'msg':"Inserted"})
    return render(request,'Guest/ParentReg.html',{'pdata':pdata})

def Login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        parentcount=tbl_parent.objects.filter(parent_email=email,parent_password=password).count()
        admincount=tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        lawyer=tbl_lawyer.objects.filter(lawyer_email=email,lawyer_password=password).count()
        edcount=tbl_educationalstaff.objects.filter(educationalstaff_email=email,educationalstaff_password=password).count()
        hltcount=tbl_healthstaff.objects.filter(healthstaff_email=email,healthstaff_password=password).count()
        rhbcount=tbl_rehabilitationstaff.objects.filter(rehabilitationstaff_email=email,rehabilitationstaff_password=password).count()
        if parentcount>0:
            parentdata=tbl_parent.objects.get(parent_email=email,parent_password=password)
            request.session['pid']=parentdata.id
            return redirect('Parent:Homepage')
        elif admincount>0:
            admindata=tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session['aid']=admindata.id
            return redirect('Admin:HomePage')
        elif lawyer>0:
            lawyer=tbl_lawyer.objects.get(lawyer_email=email,lawyer_password=password)
            request.session['lid']=lawyer.id
            return redirect('Lawyer:HomePage')
        elif edcount>0:
            eddata=tbl_educationalstaff.objects.get(educationalstaff_email=email,educationalstaff_password=password)
            request.session['edid']=eddata.id
            return redirect('EducationalStaff:HomePage')
        elif hltcount>0:
            hlth=tbl_healthstaff.objects.get(healthstaff_email=email,healthstaff_password=password)
            request.session['hlthid']=hlth.id
            return redirect('HealthStaff:HomePage')
        elif rhbcount>0:
            rhbh=tbl_rehabilitationstaff.objects.get(rehabilitationstaff_email=email,rehabilitationstaff_password=password)
            request.session['rid']=rhbh.id
            return redirect('RehabilitationStaff:HomePage')
        else:
            return render(request,'Guest/Login.html',{'msg':"Invalid Data"})
    return render(request,'Guest/Login.html')

def index(request):
    return render(request,'Guest/index.html')
