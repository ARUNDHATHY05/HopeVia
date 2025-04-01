from django.shortcuts import render,redirect
from Admin.models import*
from Lawyer.models import*
from Parent.models import*
from EducationalStaff.models import*
from HealthStaff.models import*
from RehabilitationStaff.models import*

def Homepage(request):
    return render(request,'Parent/Homepage.html')

def MyProfile(request):
    parent=tbl_parent.objects.get(id=request.session['pid'])
    return render(request,'Parent/MyProfile.html',{'parent':parent})

def ChangePassword(request):
    parent=tbl_parent.objects.get(id=request.session['pid'])
    dbpass=parent.parent_password
    if request.method=='POST':
        oldpass=request.POST.get('opass')
        newpass=request.POST.get('npas')
        cnfmpass=request.POST.get('cpas')
        if dbpass==oldpass:
            if newpass == cnfmpass:
                parent.parent_password=newpass
                parent.save()
                return render(request,'Parent/ChangePassword.html',{'msg':"Password Changed"})
            else:
                return render(request,'Parent/ChangePassword.html',{'msg':"Invalid Password"})
        else:
            return render(request,'Parent/ChangePassword.html',{'msg':"Re-Enter Old Password"})
    else:
        return render(request,'Parent/ChangePassword.html')
    
def EditProfile(request):
    parent=tbl_parent.objects.get(id=request.session['pid'])
    if request.method=='POST':
        parent.parent_name=request.POST.get('name')
        parent.parent_email=request.POST.get('email')
        parent.parent_contact=request.POST.get('contact')
        parent.parent_address=request.POST.get('address')
        parent.save()
        return render(request,'Parent/EditProfile.html',{'msg':"Updated"})
    return render(request,'Parent/EditProfile.html',{'parent':parent})

def JuvenileDetails(request):
    juvenile=tbl_juvenile.objects.filter(parent=request.session['pid'])
    return render(request,'Parent/JuvenileDetails.html',{'juvenile':juvenile})

def JuvenileCaseDetails(request,id):
    juvid=tbl_juvenile.objects.get(id=id)
    casedt=tbl_case.objects.get(juvenile=juvid)
    return render(request,'Parent/JuvenileCaseDetails.html',{'casedt':casedt})

def ViewJuvenile(request):
    viewjuvenile=tbl_juvenile.objects.filter(parent=request.session['pid'])
    return render(request,'Parent/ViewJuvenile.html',{'viewjuvenile':viewjuvenile})

def ViewHearing(request,id):
    hearing=tbl_hearing.objects.filter(juvenile=id)
    return render(request,'Parent/ViewHearing.html',{'hearing':hearing})

def AddComplaint(request):
    complaint=tbl_complaint.objects.filter(parent=request.session['pid'])
    parent=tbl_parent.objects.get(id=request.session['pid'])
    if request.method=='POST':
        content=request.POST.get('complaint')
        tbl_complaint.objects.create(complaint_content=content,parent=parent)
        return render(request,'Parent/AddComplaint.html',{'msg':"Complaint Added"})
    return render(request,'Parent/AddComplaint.html',{'complaint':complaint,'parent':parent})

def Appointment(request,id):
    app=tbl_appointment.objects.all()
    juvenile=tbl_juvenile.objects.get(id=id)
    if request.method=='POST':
        details=request.POST.get('appointment')
        date=request.POST.get('date')
        time=request.POST.get('time')
        tbl_appointment.objects.create(appointment_fordate=date,appointment_fortime=time,juvenile=juvenile,appointment_details=details)
        return render(request,'Parent/Appointment.html',{'msg':"Appointment Added"})
    return render(request,'Parent/Appointment.html',{'app':app,'juvenile':juvenile})

def ViewAppointment(request):
    viewapp=tbl_appointment.objects.filter(juvenile__parent=request.session['pid'])
    return render(request,'Parent/ViewAppointment.html',{'appointment':viewapp})

def ViewLawyer(request,id):
    law=tbl_juvenile.objects.filter(lawyer=id)
    return render(request,'Parent/ViewLawyer.html',{'lawyer':law})

def payment(request,id):
   hear = tbl_hearing.objects.get(id=id)
   amount = hear.amount
   if request.method == "POST":
      hear.hearing_status = 1
      hear.save()
      return redirect("Parent:loader")
   else:
      return render(request,"Parent/Payment.html", {"total":amount})

def loader(request):
    return render(request,"Parent/Loader.html")

def paymentsuc(request):
    return render(request,"Parent/Payment_suc.html")

def ViewEReport(request):
    ereport=tbl_educationalreport.objects.all()
    return render(request,'Parent/ViewEReport.html',{'ereport':ereport})

def ViewHReport(request):
    hrreport=tbl_healthreport.objects.all()
    return render(request,'Parent/ViewHReport.html',{'hrreport':hrreport})

def ViewRReport(request):
    rrreport=tbl_rehabilitationreport.objects.all()
    return render(request,'Parent/ViewRReport.html',{'rrreport':rrreport})

def Report(request):
    return render(request,'Parent/Report.html')

def logout(request):
    del request.session["pid"]
    return redirect("Guest:Login")


   
