from django.shortcuts import render,redirect
from Admin.models import*
from Lawyer.models import*
from EducationalStaff.models import*
from HealthStaff.models import*
from RehabilitationStaff.models import*

def MyProfile(request):
    lawyer=tbl_lawyer.objects.get(id=request.session['lid'])
    return render(request,'Lawyer/MyProfile.html',{'lawyer':lawyer})

def EditProfile(request): 
    data=tbl_lawyer.objects.get(id=request.session['lid'])
    if request.method=='POST':
        data.lawyer_name=request.POST.get('txt_name')
        data.lawyer_email=request.POST.get('txt_name')
        data.lawyer_contact=request.POST.get('contact')
        data.lawyer_address=request.POST.get('address')
        data.save()
        return render(request,'Lawyer/EditProfile.html',{'msg':"Updated"})
    return render(request,'Lawyer/EditProfile.html',{'data':data})

def ChangePassword(request):
    data=tbl_lawyer.objects.get(id=request.session['lid'])
    dbpass=data.lawyer_password
    if request.method=='POST':
        oldpass=request.POST.get('opass')
        newpass=request.POST.get('npas')
        cnfmpass=request.POST.get('cpas')
        if dbpass==oldpass:
            if newpass == cnfmpass:
                data.lawyer_password=newpass
                data.save()
                return render(request,'Lawyer/ChangePassword.html',{'msg':"Password Changed"})
            else:
                return render(request,'Lawyer/ChangePassword.html',{'msg':"Invalid Password"})
        else:
            return render(request,'Lawyer/ChangePassword.html',{'msg':"Re-Enter Old Password"})
    else:
        return render(request,'Lawyer/ChangePassword.html')
    
def HomePage(request):
    return render(request,'Lawyer/HomePage.html')

def AddHearing(request,id):
    casehearing=tbl_hearing.objects.filter(juvenile=id)
    if request.method=='POST':
        juvenile=tbl_juvenile.objects.get(id=id)
        date=request.POST.get('date')
        fordate=request.POST.get('fordate')
        amount=request.POST.get('amount')
        tbl_hearing.objects.create(hearing_date=date,juvenile=juvenile,juvenile_fordate=fordate,amount=amount)
        return render(request,'Lawyer/AddHearing.html',{'msg':"Report Added","id":id})
    else:
        return render(request,'Lawyer/AddHearing.html',{'casehearing':casehearing})


def ViewJuvenile(request):
    viewjuvenile=tbl_juvenile.objects.filter(lawyer=request.session['lid'])
    return render(request,'Lawyer/ViewJuvenile.html',{'viewjuvenile':viewjuvenile})

def ViewEReport(request):
    ereport=tbl_educationalreport.objects.all()
    juvenile=tbl_juvenile.objects.filter()
    return render(request,'Lawyer/ViewEReport.html',{'ereport':ereport,'juvenile':juvenile})

def ViewHReport(request):
    hrreport=tbl_healthreport.objects.all()
    juvenile=tbl_juvenile.objects.filter()
    return render(request,'Lawyer/ViewHReport.html',{'hrreport':hrreport,'juvenile':juvenile})

def ViewRReport(request):
    rrreport=tbl_rehabilitationreport.objects.all()
    juvenile=tbl_juvenile.objects.filter()
    return render(request,'Lawyer/ViewRReport.html',{'rrreport':rrreport,'juvenile':juvenile})

def Report(request):
    return render(request,'Lawyer/Report.html')

def logout(request):
    del request.session["lid"]
    return redirect("Guest:Login")

def Payment(request):
    hearings = tbl_hearing.objects.all()    
    if request.method=='POST':
        juvenile_name = request.POST.get('juvenile_name')
        hearing_date = request.POST.get('hearing')
        hearing = request.POST.get('fordate')
        juvenile = tbl_juvenile.objects.get(name=juvenile_name)
        parent=tbl_parent.objects.get(parent=parent)
        tbl_hearing.objects.create(juvenile=juvenile,hearing_date=hearing_date,juvenile_fordate=hearing)
        return render(request, 'Lawyer/Payment.html', {'msg': "Payment Done", 'hearings': hearings})   
    return render(request, 'Lawyer/Payment.html', {'hearings': hearings})