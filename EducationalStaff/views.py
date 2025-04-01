from django.shortcuts import render,redirect
from Admin.models import*
from EducationalStaff.models import*
def MyProfile(request):
    edustaff=tbl_educationalstaff.objects.get(id=request.session['edid'])
    return render(request,'EducationalStaff/MyProfile.html',{'edustaff':edustaff})

def EditProfile(request): 
    edustaff=tbl_educationalstaff.objects.get(id=request.session['edid'])
    if request.method=='POST':
        edustaff.educationalstaff_name=request.POST.get('txt_name')
        edustaff.educationalstaff_email=request.POST.get('txt_email')
        edustaff.educationalstaff_contact=request.POST.get('txt_contact')
        edustaff.save()
        return render(request,'EducationalStaff/EditProfile.html',{'msg':"Updated"})
    return render(request,'EducationalStaff/EditProfile.html',{'edustaff':edustaff})

def ChangePassword(request):
    edustaff=tbl_educationalstaff.objects.get(id=request.session['edid'])
    dbpass=edustaff.educationalstaff_password
    if request.method=='POST':
        oldpass=request.POST.get('opass')
        newpass=request.POST.get('npas')
        cnfmpass=request.POST.get('cpas')
        if dbpass==oldpass:
            if newpass == cnfmpass:
                edustaff.educationalstaff_password=newpass
                edustaff.save()
                return render(request,'EducationalStaff/ChangePassword.html',{'msg':"Password Changed"})
            else:
                return render(request,'EducationalStaff/ChangePassword.html',{'msg':"Invalid Password"})
        else:
            return render(request,'EducationalStaff/ChangePassword.html',{'msg':"Re-Enter Old Password"})
    else:
        return render(request,'EducationalStaff/ChangePassword.html')

def HomePage(request):
    return render(request,'EducationalStaff/HomePage.html')

def ViewJuvenile(request):
    edustaff=tbl_educationalstaff.objects.get(id=request.session['edid'])
    viewjuvenile = tbl_assignedustf.objects.filter(educationalstaff=edustaff)
    return render(request,'EducationalStaff/ViewJuvenile.html',{'viewjuvenile':viewjuvenile,'educationalstaff':edustaff})

def deljuv(request,jid):
    tbl_juvenile.objects.get(id=jid).delete()
    return render(request,'EducationalStaff/ViewJuvenile.html',{'msg':"Deleted"})

def AddEduReport(request,jid):
    reportdata=tbl_educationalreport.objects.filter(juvenile=jid)
    if request.method=='POST':
        staff=tbl_educationalstaff.objects.get(id=request.session['edid'])
        juvenile=tbl_juvenile.objects.get(id=jid)
        detail=request.POST.get('details')
        tbl_educationalreport.objects.create(educationalreport_details=detail,educational_staff=staff,juvenile=juvenile)
        return render(request,'EducationalStaff/AddEduReport.html',{'msg':"Report Added","id":jid})
    else:
        return render(request,'EducationalStaff/AddEduReport.html',{'data':reportdata})
    
def editedureport(request,edid):
    edureport=tbl_educationalreport.objects.get(id=edid)
    if request.method=='POST':
        edureport.educationalreport_details=request.POST.get('details')
        edureport.save()
        return render(request,'EducationalStaff/ViewJuvenile.html',{'msg':"Edited"})
    else:
        return render(request,'EducationalStaff/AddEduReport.html',{'edureport':edureport})
    
def logout(request):
    del request.session["edid"]
    return redirect("Guest:Login")
    
