from django.shortcuts import render,redirect
from Admin.models import*
from HealthStaff.models import*
def MyProfile(request):
    hlthstaff=tbl_healthstaff.objects.get(id=request.session['hlthid'])
    return render(request,'HealthStaff/MyProfile.html',{'hlthstaff':hlthstaff})
def EditProfile(request): 
    hlthstaff=tbl_healthstaff.objects.get(id=request.session['hlthid'])
    if request.method=='POST':
        hlthstaff.healthstaff_name=request.POST.get('txt_name')
        hlthstaff.healthstaff_email=request.POST.get('txt_email')
        hlthstaff.healthstaff_contact=request.POST.get('txt_contact')
        hlthstaff.save()
        return render(request,'HealthStaff/EditProfile.html',{'msg':"Updated"})
    return render(request,'HealthStaff/EditProfile.html',{'hlthstaff':hlthstaff})

def ChangePassword(request):
    hlthstaff=tbl_healthstaff.objects.get(id=request.session['hlthid'])
    dbpass=hlthstaff.healthstaff_password
    if request.method=='POST':
        oldpass=request.POST.get('opass')
        newpass=request.POST.get('npas')
        cnfmpass=request.POST.get('cpas')
        if dbpass==oldpass:
            if newpass == cnfmpass:
                hlthstaff.healthstaff_password=newpass
                hlthstaff.save()
                return render(request,'HealthStaff/ChangePassword.html',{'msg':"Password Changed"})
            else:
                return render(request,'HealthStaff/ChangePassword.html',{'msg':"Invalid Password"})
        else:
            return render(request,'HealthStaff/ChangePassword.html',{'msg':"Re-Enter Old Password"})
    else:
        return render(request,'HealthStaff/ChangePassword.html')

def HomePage(request):
    return render(request,'HealthStaff/HomePage.html')

def ViewJuvenile(request):
    hlthstaff=tbl_healthstaff.objects.get(id=request.session['hlthid'])
    viewjuvenile = tbl_assignhltstf.objects.filter(healthstaff=hlthstaff)
    return render(request,'HealthStaff/ViewJuvenile.html',{'viewjuvenile':viewjuvenile,'health_staff': hlthstaff})

def deljuv(request,jid):
    tbl_juvenile.objects.get(id=jid).delete()
    return render(request,'HealthStaff/ViewJuvenile.html',{'msg':"Deleted"})

def AddHltReport(request,id):
    reportdata=tbl_healthreport.objects.filter(juvenile=id)
    if request.method=='POST':
        staff=tbl_healthstaff.objects.get(id=request.session['hlthid'])
        juvenile=tbl_juvenile.objects.get(id=id)
        detail=request.POST.get('details')
        tbl_healthreport.objects.create(healthreport_details=detail,health_staff=staff,juvenile=juvenile)
        return render(request,'HealthStaff/AddHltReport.html',{'msg':"Report Added","id":id})
    else:
        return render(request,'HealthStaff/AddHltReport.html',{'data':reportdata})
    
def editedureport(request,hlthid):
    hltreport=tbl_healthreport.objects.get(id=hlthid)
    if request.method=='POST':
        hltreport.healthreport_details=request.POST.get('details')
        hltreport.save()
        return render(request,'HealthStaff/ViewJuvenile.html',{'msg':"Edited"})
    else:
        return render(request,'HealthStaff/AddHltReport.html',{'hltreport':hltreport})
    
def logout(request):
    del request.session["hlthid"]
    return redirect("Guest:Login")
    
    