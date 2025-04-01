from django.shortcuts import render,redirect
from Admin.models import*
from RehabilitationStaff.models import*
def Homepage(request):
    return render(request,'RehabilitationStaff/HomePage.html')

def MyProfile(request):
    rhbstf=tbl_rehabilitationstaff.objects.get(id=request.session['rid'])
    return render(request,'RehabilitationStaff/MyProfile.html',{'rhbstf':rhbstf})

def ChangePassword(request):
    rhbstf=tbl_rehabilitationstaff.objects.get(id=request.session['rid'])
    dbpass=rhbstf.rehabilitationstaff_password
    if request.method=='POST':
        oldpass=request.POST.get('opass')
        newpass=request.POST.get('npas')
        cnfmpass=request.POST.get('cpas')
        if dbpass==oldpass:
            if newpass == cnfmpass:
                rhbstf.rehabilitationstaff_password=newpass
                rhbstf.save()
                return render(request,'RehabilitationStaff/ChangePassword.html',{'msg':"Password Changed"})
            else:
                return render(request,'RehabilitationStaff/ChangePassword.html',{'msg':"Invalid Password"})
        else:
            return render(request,'RehabilitationStaff/ChangePassword.html',{'msg':"Re-Enter Old Password"})
    else:
        return render(request,'RehabilitationStaff/ChangePassword.html')
    
def EditProfile(request):
    rhbstf=tbl_rehabilitationstaff.objects.get(id=request.session['rid'])
    if request.method=='POST':
        rhbstf.rehabilitationstaff_name=request.POST.get('name')
        rhbstf.rehabilitationstaff_email=request.POST.get('email')
        rhbstf.rehabilitationstaff_contact=request.POST.get('contact')
        rhbstf.save()
        return render(request,'RehabilitationStaff/EditProfile.html',{'msg':"Updated"})
    return render(request,'RehabilitationStaff/EditProfile.html',{'rhbstf':rhbstf})

def ViewJuvenile(request):
    rhbstf=tbl_rehabilitationstaff.objects.get(id=request.session['rid'])
    viewjuvenile=tbl_assignrehabstf.objects.filter(rehabilitationstaff=rhbstf)
    return render(request,'RehabilitationStaff/ViewJuvenile.html',{'viewjuvenile':viewjuvenile,'rehabilitationstaff': rhbstf})

def deljuv(request,jid):
    tbl_juvenile.objects.get(id=jid).delete()
    return render(request,'RehabilitationStaff/ViewJuvenile.html',{'msg':"Deleted"})

def AddRehabReport(request,id):
    reportdata=tbl_rehabilitationreport.objects.filter(juvenile=id)
    if request.method=='POST':
        staff=tbl_rehabilitationstaff.objects.get(id=request.session['rid'])
        juvenile=tbl_juvenile.objects.get(id=id)
        detail=request.POST.get('details')
        tbl_rehabilitationreport.objects.create(rehabilitationreport_details=detail,rehabilitation_staff=staff,juvenile=juvenile)
        return render(request,'RehabilitationStaff/AddRehabReport.html',{'msg':"Report Added","id":id})
    else:
        return render(request,'RehabilitationStaff/AddRehabReport.html',{'data':reportdata,"id":id})

def editedureport(request,rid,id):
    rehabreport=tbl_rehabilitationreport.objects.get(id=rid)
    if request.method=='POST':
        rehabreport.rehabilitationreport_details=request.POST.get('details')
        rehabreport.save()
        return render(request,'RehabilitationStaff/AddRehabReport.html',{'msg':"Edited","id":id})
    else:
        return render(request,'RehabilitationStaff/AddRehabReport.html',{'rehabreport':rehabreport})
    
def logout(request):
    del request.session["rid"]
    return redirect("Guest:Login")

   
