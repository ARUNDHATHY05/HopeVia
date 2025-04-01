from django.shortcuts import render,redirect
from Admin.models import*
from Parent.models import*
from EducationalStaff.models import*    
from HealthStaff.models import*
from RehabilitationStaff.models import*
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Count
import json
from django.db.models.functions import TruncMonth
from django.db.models import Count
from django.utils import timezone
import json
from datetime import datetime
from django.utils import timezone
from collections import defaultdict 
from django.db.models import Count

def District(request):
    distdata=tbl_district.objects.all()
    if request.method=='POST':
        disname=request.POST.get('district')
        tbl_district.objects.create(district_name=disname)
        return render(request,'Admin/District.html',{'msg':"Inserted"})
    return render(request,'Admin/District.html',{'ddata':distdata})
def deldis(request,did):
    tbl_district.objects.get(id=did).delete()
    return render(request,'Admin/District.html',{'msg':"Deleted"})
def editdis(request,eid):
    data=tbl_district.objects.get(id=eid)
    if request.method=='POST':
        data.district_name=request.POST.get('district')
        data.save()
        return render(request,'Admin/District.html',{'msg':"Updated"})
    return render(request,'Admin/District.html',{'data':data})

def Case(request,id):
    case=tbl_case.objects.filter(juvenile=id)
    casetp=tbl_casetype.objects.all()
    if request.method=='POST':
        juvenileid=tbl_juvenile.objects.get(id=id)
        case=request.POST.get('name')
        details=request.POST.get('txt_details')
        casetp=tbl_casetype.objects.get(id=request.POST.get("casetype"))
        tbl_case.objects.create(case_name=case,casetype=casetp,case_details=details,juvenile=juvenileid)
        return render(request,'Admin/Case.html',{'msg':"Inserted"})
    return render(request,'Admin/Case.html',{'case':case,'casetp':casetp})

def CaseType(request):
    casedata=tbl_casetype.objects.all()
    if request.method=='POST':
        casetype=request.POST.get('casetype')
        tbl_casetype.objects.create(case_type=casetype)
        return render(request,'Admin/CaseType.html',{'msg':"Inserted"})
    return render(request,'Admin/CaseType.html',{'cdata':casedata})
def delct(request,dct):
    tbl_casetype.objects.get(id=dct).delete()
    return render(request,'Admin/CaseType.html',{'msg':"Deleted"})
def editct(request,cid):
    data=tbl_casetype.objects.get(id=cid)
    if request.method=='POST':
        data.case_type=request.POST.get('casetype')
        data.save()
        return render(request,'Admin/CaseType.html',{'msg':"Updated"})
    return render(request,'Admin/CaseType.html',{'data':data})


def Admin(request):
    pdata=tbl_admin.objects.all()
    if request.method=='POST':
        aname=request.POST.get('name')
        aemail=request.POST.get('email')
        apass=request.POST.get('password')
        tbl_admin.objects.create(admin_name=aname,admin_email=aemail,admin_password=apass)
        return render(request,'Admin/AdminReg.html',{'msg':"Inserted"})
    return render(request,'Admin/AdminReg.html',{'pdata':pdata})

def delad(request,aid):
    tbl_admin.objects.get(id=aid).delete()
    return render(request,'Admin/AdminReg.html',{'msg':"Deleted"})
def editad(request,adid):
    data=tbl_admin.objects.get(id=adid)
    if request.method=='POST':
        data.admin_name=request.POST.get('name')
        data.admin_email=request.POST.get('email')
        data.admin_password=request.POST.get('password')
        data.save()
        return render(request,'Admin/AdminReg.html',{'msg':"Updated"})
    return render(request,'Admin/AdminReg.html',{'data':data})


def place(request):
    dis=tbl_district.objects.all()
    pl=tbl_place.objects.all()
    if request.method=="POST":
        district=tbl_district.objects.get(id=request.POST.get("sel_district"))
        placename=request.POST.get("place")
        tbl_place.objects.create(place_name=placename,district=district)
        return redirect("Admin:place")
    else:
        return render(request,'Admin/Place.html',{'district':dis,'place':pl})   
def delpl(request,plid):
    tbl_place.objects.get(id=plid).delete()
    return render(request,'Admin/Place.html',{'msg':"Deleted"})
def editpl(request,eplid):
    dis=tbl_district.objects.all()
    data=tbl_place.objects.get(id=eplid)
    if request.method=='POST':
        data.district=tbl_district.objects.get(id=request.POST.get("sel_district"))
        data.place_name=request.POST.get('place')
        data.save()
        return render(request,'Admin/Place.html',{'msg':"Updated"})
    return render(request,'Admin/Place.html',{'district':dis,'data':data})


def Category(request):
    cat=tbl_category.objects.all()
    if request.method=='POST':
        Category=request.POST.get('txtcat')
        tbl_category.objects.create(category_name=Category)
        return redirect('Admin:category')
    else:
        return render(request,'Admin/Category.html',{'cat':cat})
def delcat(request,cid):
    tbl_category.objects.get(id=cid).delete()
    return redirect('Admin:category')
def editcat(request,eid):
    data=tbl_category.objects.get(id=eid)
    if request.method=='POST':
        data.category_name=request.POST.get('txtcat')
        data.save()
        return render(request,'Admin/Category.html',{'msg':"Updated"})
    return render(request,'Admin/Category.html',{'data':data})


def subcategory(request):
    categories = tbl_category.objects.all()
    subcategories=tbl_subcategory.objects.all()
    if request.method=='POST':
        category=tbl_category.objects.get(id=request.POST.get("sel_category"))
        subcategory_name=request.POST.get('subcat')
        tbl_subcategory.objects.create(category_id=category,subcategory_name=subcategory_name)
        return redirect('Admin:subcategory')
    else:
        return render(request,'Admin/Subcategory.html',{'cat':categories,'subcategories':subcategories})
    
def delsub(request,scid):
    tbl_subcategory.objects.get(id=scid).delete()
    return redirect('Admin:subcategory')

def editsub(request,sctid):
    categories = tbl_category.objects.all()
    subcategory=tbl_subcategory.objects.get(id=sctid)
    if request.method=='POST':
        subcategory.subcategory_name=request.POST.get('subcat')
        subcategory.category_id=tbl_category.objects.get(id=request.POST.get('sel_category'))
        subcategory.save()
        return render(request,'Admin/Subcategory.html',{'msg':"Updated"})
    return render(request,'Admin/Subcategory.html',{'cat': categories,'subcategory':subcategory})

def Lawyer(request):
    ldata=tbl_lawyer.objects.all()
    if request.method=='POST':
        lname=request.POST.get('name')
        lemail=request.POST.get('email')
        lcontact=request.POST.get('contact')
        ladd=request.POST.get('add')
        lpic=request.FILES.get('pic')
        lprf=request.FILES.get('proof')
        lpass=request.POST.get('password')
        tbl_lawyer.objects.create(lawyer_name=lname,lawyer_email=lemail,lawyer_contact=lcontact,lawyer_address=ladd,lawyer_photo=lpic,lawyer_proof=lprf,lawyer_password=lpass)

              # HTML Email message with CSS
        html_message = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f4f4f4;
                    color: #333;
                }}
                .container {{
                    max-width: 600px;
                    margin: 20px auto;
                    background-color: #ffffff;
                    border-radius: 8px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                    overflow: hidden;
                }}
                .header {{
                    background-color: #4CAF50;
                    color: white;
                    padding: 20px;
                    text-align: center;
                }}
                .content {{
                    padding: 25px;
                    line-height: 1.6;
                }}
                .credentials {{
                    background-color: #f9f9f9;
                    padding: 15px;
                    border-radius: 5px;
                    margin: 15px 0;
                }}
                .footer {{
                    background-color: #f0f0f0;
                    padding: 15px;
                    text-align: center;
                    font-size: 12px;
                    color: #666;
                }}
                .highlight {{
                    color: #4CAF50;
                    font-weight: bold;
                }}
                h1 {{
                    margin: 0;
                    font-size: 24px;
                }}
                .btn {{
                    display: inline-block;
                    padding: 10px 20px;
                    background-color: #4CAF50;
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                    margin-top: 15px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Welcome!</h1>
                </div>
                <div class="content">
                    <p>Dear <span class="highlight">{lname}</span>,</p>
                    <p>You have been successfully registered as a Lawyer with us.</p>
                    
                    <div class="credentials">
                        <h3>Your Login Credentials:</h3>
                        <p><strong>Email:</strong> {lemail}</p>
                        <p><strong>Password:</strong> {lpass}</p>
                    </div>
                    
                    <p>Please keep these credentials safe and secure. We recommend changing your password after your first login.</p>
                </div>
                <div class="footer">
                    <p>Warmest regards,<br>
                    Your Hope Team<br>
                    Hopevia | Address | Contact: 123-456-7890 | Email: info@hopevia.com</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        # Send email
        try:
            send_mail(
                subject=f"Welcome {lname} - Registration Successful",
                message="You have been successfully registered. Please check the HTML version of this email for your credentials.",  # Plain text fallback
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[lemail],
                html_message=html_message,  # HTML version
                fail_silently=False,
            )
            return render(request, 'Admin/Lawyer.html', {
                'msg': "Registration successful! Confirmation email has been sent.",
                'Lawyer': ldata
            })
        except Exception as e:
            return render(request, 'Admin/Lawyer.html', {
                'msg': f"Registration successful but failed to send email: {str(e)}",
                'Lawyer':ldata
            })
    
    return render(request,'Admin/Lawyer.html',{'Lawyer':ldata})

def Juvenile(request,id):
    jdata=tbl_juvenile.objects.all()
    ldata=tbl_lawyer.objects.all()
    if request.method=='POST':
        jname=request.POST.get('name')
        jage=request.POST.get('age')
        jgend=request.POST.get('gender')
        dob=request.POST.get('dob')
        jhgt=request.POST.get('height')
        jwgt=request.POST.get('weight')
        jadd=request.POST.get('address')
        jpic=request.FILES.get('pic')
        proof=request.FILES.get('proof')
        admission=request.POST.get('date')
        parentid=tbl_parent.objects.get(id=id)
        lawyer=tbl_lawyer.objects.get(id=request.POST.get("sel_lawyer"))
        print(lawyer)
        tbl_juvenile.objects.create(juvenile_proof=proof,juvenile_name=jname,juvenile_age=jage,juvenile_gender=jgend,juvenile_height=jhgt,juvenile_weight=jwgt,juvenile_address=jadd,juvenile_photo=jpic,lawyer=lawyer,parent=parentid,juvenile_dob=dob,juvenile_admissiondate=admission)
        return render(request,'Admin/Juvenile.html',{'msg':"Inserted"})
    else:
        return render(request,'Admin/Juvenile.html',{'Lawyer':ldata,'Juvenile':jdata})

# def Parent(request):
#     pdata=tbl_parent.objects.all()
#     if request.method=='POST':
#         role=request.POST.get('parent')
#         pname=request.POST.get('name')
#         pemail=request.POST.get('email')
#         pcont=request.POST.get('contact')
#         padd=request.POST.get('address')
#         ppic=request.FILES.get('photo')
#         pprf=request.FILES.get('proof')
#         ppwd=request.POST.get('password')
#         tbl_parent.objects.create(parent_name=pname,parent_email=pemail,parent_contact=pcont,parent_address=padd,parent_photo=ppic,parent_proof=pprf,parent_password=ppwd,parent_role=role)
#         return render(request,'Admin/ParentReg.html',{'msg':"Inserted"})
#     return render(request,'Admin/ParentReg.html',{'pdata':pdata})
        

def Parent(request):
    pdata = tbl_parent.objects.all()
    
    if request.method == 'POST':
        role = request.POST.get('parent')
        pname = request.POST.get('name')
        pemail = request.POST.get('email')
        pcont = request.POST.get('contact')
        padd = request.POST.get('address')
        ppic = request.FILES.get('photo')
        pprf = request.FILES.get('proof')
        ppwd = request.POST.get('password')
        
        # Create the parent object
        tbl_parent.objects.create(
            parent_name=pname,
            parent_email=pemail,
            parent_contact=pcont,
            parent_address=padd,
            parent_photo=ppic,
            parent_proof=pprf,
            parent_password=ppwd,
            parent_role=role
        )
        
        # HTML Email message with CSS
        html_message = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f4f4f4;
                    color: #333;
                }}
                .container {{
                    max-width: 600px;
                    margin: 20px auto;
                    background-color: #ffffff;
                    border-radius: 8px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                    overflow: hidden;
                }}
                .header {{
                    background-color: #4CAF50;
                    color: white;
                    padding: 20px;
                    text-align: center;
                }}
                .content {{
                    padding: 25px;
                    line-height: 1.6;
                }}
                .credentials {{
                    background-color: #f9f9f9;
                    padding: 15px;
                    border-radius: 5px;
                    margin: 15px 0;
                }}
                .footer {{
                    background-color: #f0f0f0;
                    padding: 15px;
                    text-align: center;
                    font-size: 12px;
                    color: #666;
                }}
                .highlight {{
                    color: #4CAF50;
                    font-weight: bold;
                }}
                h1 {{
                    margin: 0;
                    font-size: 24px;
                }}
                .btn {{
                    display: inline-block;
                    padding: 10px 20px;
                    background-color: #4CAF50;
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                    margin-top: 15px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Welcome!</h1>
                </div>
                <div class="content">
                    <p>Dear <span class="highlight">{pname}</span>,</p>
                    <p>You have been successfully registered as a Parent with us.</p>
                    
                    <div class="credentials">
                        <h3>Your Login Credentials:</h3>
                        <p><strong>Email:</strong> {pemail}</p>
                        <p><strong>Password:</strong> {ppwd}</p>
                    </div>        
                    <p>Please keep these credentials safe and secure. We recommend changing your password after your first login.</p>
                </div>
                <div class="footer">
                    <p>Warmest regards,<br>
                    Your Hope Team<br>
                    Hopevia | Address | Contact: 123-456-7890 | Email: info@hopevia.com</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        # Send email
        try:
            send_mail(
                subject=f"Welcome {pname} - Registration Successful",
                message="You have been successfully registered. Please check the HTML version of this email for your credentials.",  # Plain text fallback
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[pemail],
                html_message=html_message,  # HTML version
                fail_silently=False,
            )
            return render(request, 'Admin/ParentReg.html', {
                'msg': "Registration successful! Confirmation email has been sent.",
                'pdata': pdata
            })
        except Exception as e:
            return render(request, 'Admin/ParentReg.html', {
                'msg': f"Registration successful but failed to send email: {str(e)}",
                'pdata': pdata
            })
    
    return render(request, 'Admin/ParentReg.html', {'pdata': pdata})




def ViewJuvenile(request):
    viewjuvenile=tbl_juvenile.objects.all()
    return render(request,'Admin/ViewJuvenile.html',{'viewjuvenile':viewjuvenile})
def deljuv(request,jid):
    tbl_juvenile.objects.get(id=jid).delete()
    return render(request,'Admin/ViewJuvenile.html',{'msg':"Deleted"})

def HomePage(request):
    Juvenile=tbl_juvenile.objects.all().count()
    complaint=tbl_complaint.objects.all().count()
    parent=tbl_parent.objects.all().count()
    complaintdata=tbl_complaint.objects.filter(complaint_status=1).count()
    complaintpendingdata=tbl_complaint.objects.filter(complaint_status=0).count()
    Lawyer=tbl_lawyer.objects.all().count()
    return render(request,'Admin/HomePage.html',{'Juvenile':Juvenile,'complaint':complaint,'parent':parent,'complaintdata':complaintdata,'complaintpendingdata':complaintpendingdata,'Lawyer':Lawyer})

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import tbl_educationalstaff  # Assuming this is in your app's models.py

def EducationalStaff(request):
    edudata = tbl_educationalstaff.objects.all()
    if request.method == 'POST':
        ename = request.POST.get('name')
        eemail = request.POST.get('email')
        econtact = request.POST.get('number')
        epassword = request.POST.get('password')
        tbl_educationalstaff.objects.create(
            educationalstaff_name=ename,
            educationalstaff_email=eemail,
            educationalstaff_contact=econtact,
            educationalstaff_password=epassword
        )
        
        # HTML Email message with CSS
        html_message = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f4f4f4;
                    color: #333;
                }}
                .container {{
                    max-width: 600px;
                    margin: 20px auto;
                    background-color: #ffffff;
                    border-radius: 8px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                    overflow: hidden;
                }}
                .header {{
                    background-color: #4CAF50;
                    color: white;
                    padding: 20px;
                    text-align: center;
                }}
                .content {{
                    padding: 25px;
                    line-height: 1.6;
                }}
                .credentials {{
                    background-color: #f9f9f9;
                    padding: 15px;
                    border-radius: 5px;
                    margin: 15px 0;
                }}
                .footer {{
                    background-color: #f0f0f0;
                    padding: 15px;
                    text-align: center;
                    font-size: 12px;
                    color: #666;
                }}
                .highlight {{
                    color: #4CAF50;
                    font-weight: bold;
                }}
                h1 {{
                    margin: 0;
                    font-size: 24px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Welcome!</h1>
                </div>
                <div class="content">
                    <p>Dear <span class="highlight">{ename}</span>,</p>
                    <p>You have been successfully registered as an Education Staff with us.</p>
                    
                    <div class="credentials">
                        <h3>Your Login Credentials:</h3>
                        <p><strong>Email:</strong> {eemail}</p>
                        <p><strong>Password:</strong> {epassword}</p>
                    </div>
                    
                    <p>Please keep these credentials safe and secure. We recommend changing your password after your first login.</p>
                </div>
                <div class="footer">
                    <p>Warmest regards,<br>
                    Your Hope Team<br>
                    Hopevia | Address | Contact: 123-456-7890 | Email: info@hopevia.com</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        # Send email
        try:
            send_mail(
                subject=f"Welcome {ename} - Registration Successful",
                message="You have been successfully registered. Please check the HTML version of this email for your credentials.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[eemail],
                html_message=html_message,
                fail_silently=False,
            )
            return render(request, 'Admin/EducationalStaff.html', {
                'msg': "Registration successful! Confirmation email has been sent.",
                'EducationalStaff': edudata
            })
        except Exception as e:
            return render(request, 'Admin/EducationalStaff.html', {
                'msg': f"Registration successful but failed to send email: {str(e)}",
                'EducationalStaff': edudata
            })
    
    return render(request, 'Admin/EducationalStaff.html', {'EducationalStaff': edudata})

def Ban(request, id):
    edudata = tbl_educationalstaff.objects.all()
    try:
        staff = tbl_educationalstaff.objects.get(id=id)
        staff.ed_status = 1
        staff.save()
        return render(request, 'Admin/EducationalStaff.html', {
            'msg': "Staff member banned successfully.",
            'EducationalStaff': edudata
        })
    except tbl_educationalstaff.DoesNotExist:
        return render(request, 'Admin/EducationalStaff.html', {
            'msg': "Staff member not found.",
            'EducationalStaff': edudata
        })

def HealthStaff(request):
    hdata = tbl_healthstaff.objects.all()
    if request.method == 'POST':
        hname = request.POST.get('name')
        hemail = request.POST.get('email')
        hcontact = request.POST.get('number')
        hpassword = request.POST.get('password')
        tbl_healthstaff.objects.create(
            healthstaff_name=hname,
            healthstaff_email=hemail,
            healthstaff_contact=hcontact,
            healthstaff_password=hpassword
        )

        html_message = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f4f4f4;
                    color: #333;
                }}
                .container {{
                    max-width: 600px;
                    margin: 20px auto;
                    background-color: #ffffff;
                    border-radius: 8px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                    overflow: hidden;
                }}
                .header {{
                    background-color: #4CAF50;
                    color: white;
                    padding: 20px;
                    text-align: center;
                }}
                .content {{
                    padding: 25px;
                    line-height: 1.6;
                }}
                .credentials {{
                    background-color: #f9f9f9;
                    padding: 15px;
                    border-radius: 5px;
                    margin: 15px 0;
                }}
                .footer {{
                    background-color: #f0f0f0;
                    padding: 15px;
                    text-align: center;
                    font-size: 12px;
                    color: #666;
                }}
                .highlight {{
                    color: #4CAF50;
                    font-weight: bold;
                }}
                h1 {{
                    margin: 0;
                    font-size: 24px;
                }}
                .btn {{
                    display: inline-block;
                    padding: 10px 20px;
                    background-color: #4CAF50;
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                    margin-top: 15px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Welcome!</h1>
                </div>
                <div class="content">
                    <p>Dear <span class="highlight">{hname}</span>,</p>
                    <p>You have been successfully registered as a Health Staff with us.</p>
                    
                    <div class="credentials">
                        <h3>Your Login Credentials:</h3>
                        <p><strong>Email:</strong> {hemail}</p>
                        <p><strong>Password:</strong> {hpassword}</p>
                    </div>
                    
                    <p>Please keep these credentials safe and secure. We recommend changing your password after your first login.</p>
                </div>
                <div class="footer">
                    <p>Warmest regards,<br>
                    Your Hope Team<br>
                    Hopevia | Address | Contact: 123-456-7890 | Email: info@hopevia.com</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        try:
            send_mail(
                subject=f"Welcome {hname} - Registration Successful",
                message="You have been successfully registered. Please check the HTML version of this email for your credentials.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[hemail],
                html_message=html_message,
                fail_silently=False,
            )
            return render(request, 'Admin/HealthStaff.html', {
                'msg': "Registration successful! Confirmation email has been sent.",
                'HealthStaff': hdata
            })
        except Exception as e:
            return render(request, 'Admin/HealthStaff.html', {
                'msg': f"Registration successful but failed to send email: {str(e)}",
                'HealthStaff': hdata
            })
    
    return render(request, 'Admin/HealthStaff.html', {'HealthStaff': hdata})

def BanHealthStaff(request, id):
    hdata = tbl_healthstaff.objects.all()
    try:
        staff = tbl_healthstaff.objects.get(id=id)
        staff.hlt_status = 1
        staff.save()
        return render(request, 'Admin/HealthStaff.html', {
            'msg': "Staff member banned successfully.",
            'HealthStaff': hdata
        })
    except tbl_healthstaff.DoesNotExist:
        return render(request, 'Admin/HealthStaff.html', {
            'msg': "Staff member not found.",
            'HealthStaff': hdata
        })

def RehabilitationStaff(request):
    rdata = tbl_rehabilitationstaff.objects.all()
    if request.method == 'POST':
        rname = request.POST.get('name')
        remail = request.POST.get('email')
        rcontact = request.POST.get('number')
        rpassword = request.POST.get('password')
        tbl_rehabilitationstaff.objects.create(
            rehabilitationstaff_name=rname,
            rehabilitationstaff_email=remail,
            rehabilitationstaff_contact=rcontact,
            rehabilitationstaff_password=rpassword
        )
        
        html_message = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f4f4f4;
                    color: #333;
                }}
                .container {{
                    max-width: 600px;
                    margin: 20px auto;
                    background-color: #ffffff;
                    border-radius: 8px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                    overflow: hidden;
                }}
                .header {{
                    background-color: #4CAF50;
                    color: white;
                    padding: 20px;
                    text-align: center;
                }}
                .content {{
                    padding: 25px;
                    line-height: 1.6;
                }}
                .credentials {{
                    background-color: #f9f9f9;
                    padding: 15px;
                    border-radius: 5px;
                    margin: 15px 0;
                }}
                .footer {{
                    background-color: #f0f0f0;
                    padding: 15px;
                    text-align: center;
                    font-size: 12px;
                    color: #666;
                }}
                .highlight {{
                    color: #4CAF50;
                    font-weight: bold;
                }}
                h1 {{
                    margin: 0;
                    font-size: 24px;
                }}
                .btn {{
                    display: inline-block;
                    padding: 10px 20px;
                    background-color: #4CAF50;
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                    margin-top: 15px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Welcome!</h1>
                </div>
                <div class="content">
                    <p>Dear <span class="highlight">{rname}</span>,</p>
                    <p>You have been successfully registered as a Rehabilitation Staff with us.</p>
                    
                    <div class="credentials">
                        <h3>Your Login Credentials:</h3>
                        <p><strong>Email:</strong> {remail}</p>
                        <p><strong>Password:</strong> {rpassword}</p>
                    </div>
                    
                    <p>Please keep these credentials safe and secure. We recommend changing your password after your first login.</p>
                </div>
                <div class="footer">
                    <p>Warmest regards,<br>
                    Your Hope Team<br>
                    Hopevia | Address | Contact: 123-456-7890 | Email: info@hopevia.com</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        try:
            send_mail(
                subject=f"Welcome {rname} - Registration Successful",
                message="You have been successfully registered. Please check the HTML version of this email for your credentials.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[remail],
                html_message=html_message,
                fail_silently=False,
            )
            return render(request, 'Admin/RehabilitationStaff.html', {
                'msg': "Registration successful! Confirmation email has been sent.",
                'RehabilitationStaff': rdata
            })
        except Exception as e:
            return render(request, 'Admin/RehabilitationStaff.html', {
                'msg': f"Registration successful but failed to send email: {str(e)}",
                'RehabilitationStaff': rdata
            })

    return render(request, 'Admin/RehabilitationStaff.html', {'RehabilitationStaff': rdata})

def BanRehabilitationStaff(request, id):
    rdata = tbl_rehabilitationstaff.objects.all()
    try:
        staff = tbl_rehabilitationstaff.objects.get(id=id)
        staff.rehab_status = 1
        staff.save()
        return render(request, 'Admin/RehabilitationStaff.html', {
            'msg': "Staff member banned successfully.",
            'RehabilitationStaff': rdata
        })
    except tbl_rehabilitationstaff.DoesNotExist:
        return render(request, 'Admin/RehabilitationStaff.html', {
            'msg': "Staff member not found.",
            'RehabilitationStaff': rdata
        })

def ViewComplaint(request):
    complaint=tbl_complaint.objects.all()
    return render(request,'Admin/ViewComplaint.html',{'complaint':complaint})

def ReplyComplaint(request,id):
    complaintdata=tbl_complaint.objects.get(id=id)
    if request.method=='POST':
        complaint=request.POST.get('reply')
        complaintdata.complaint_reply=complaint
        complaintdata.complaint_status=1
        complaintdata.save()
        return render(request,'Admin/ReplyComplaint.html')
    else:
        return render(request,'Admin/ReplyComplaint.html',{'complaintdata':complaintdata})
    
def JuvenileReg(request):
    jdata=tbl_juvenile.objects.all()
    ldata=tbl_lawyer.objects.all()
    if request.method=='POST':
        jname=request.POST.get('name')
        jage=request.POST.get('age')
        jgend=request.POST.get('gender')
        jhgt=request.POST.get('height')
        jwgt=request.POST.get('weight')
        jadd=request.POST.get('address')
        jpic=request.FILES.get('pic')
        lawyer=tbl_lawyer.objects.get(id=request.POST.get("sel_lawyer"))
        print(lawyer)
        tbl_juvenile.objects.create(juvenile_name=jname,juvenile_age=jage,juvenile_gender=jgend,juvenile_height=jhgt,juvenile_weight=jwgt,juvenile_address=jadd,juvenile_photo=jpic,lawyer=lawyer)
        return render(request,'Admin/JuvenileReg.html',{'msg':"Inserted"})
    else:
        return render(request,'Admin/JuvenileReg.html',{'Lawyer':ldata,'Juvenile':jdata})

def ViewAppointment(request):
    appointment=tbl_appointment.objects.all()
    return render(request,'Admin/ViewAppointment.html',{'appointment':appointment})

def reject(request,id):
    appointment=tbl_appointment.objects.get(id=id)
    appointment.appointment_status=2
    appointment.save()
    return redirect('Admin:ViewAppointment')

def accept(request,id):
    appointment=tbl_appointment.objects.get(id=id)
    appointment.appointment_status=1
    appointment.save()
    return redirect('Admin:ViewAppointment')

def ViewEReport(request):
    ereport=tbl_educationalreport.objects.all()
    Juvenile=tbl_juvenile.objects.all()
    if request.method=='POST':
        Juvenile=tbl_juvenile.objects.get(id=request.POST.get("sel_juvenile"))
        report=request.POST.get('report')
        tbl_educationalreport.objects.create(educationalreport=report,juvenile=Juvenile)
        return render(request,'Admin/ViewEReport.html',{'msg':"Inserted"})
    return render(request,'Admin/ViewEReport.html',{'ereport':ereport})

def ViewHReport(request):
    hrreport=tbl_healthreport.objects.all()
    Juvenile=tbl_juvenile.objects.all()
    if request.method=='POST':
        Juvenile=tbl_juvenile.objects.get(id=request.POST.get("sel_juvenile"))
        report=request.POST.get('report')
        tbl_healthreport.objects.create(healthreport=report,juvenile=Juvenile)
        return render(request,'Admin/ViewHReport.html',{'msg':"Inserted"})
    return render(request,'Admin/ViewHReport.html',{'hrreport':hrreport})

def ViewRReport(request):
    rrreport=tbl_rehabilitationreport.objects.all()
    Juvenile=tbl_juvenile.objects.all()
    if request.method=='POST':
        Juvenile=tbl_juvenile.objects.get(id=request.POST.get("sel_juvenile"))
        report=request.POST.get('report')
        tbl_rehabilitationreport.objects.create(rehabilitationreport=report,juvenile=Juvenile)
        return render(request,'Admin/ViewRReport.html',{'msg':"Inserted"})
    return render(request,'Admin/ViewRReport.html',{'rrreport':rrreport})

def Report(request):    
    return render(request,'Admin/Report.html')

def AssignStaff(request, id):
    juvenile = tbl_juvenile.objects.get(id=id)
    return render(request, 'Admin/AssignStaff.html', {'juvenile': juvenile})

def AssignRehab(request, id):
    juvenile = tbl_juvenile.objects.get(id=id)
    rehab = tbl_rehabilitationstaff.objects.all()
    if request.method == 'POST':
        selected_staff_id = request.POST.get("sel_staff")
        if selected_staff_id:
            selected_rehab = tbl_rehabilitationstaff.objects.get(id=selected_staff_id)
            juvenile.rehabilitationstaff = selected_rehab
            juvenile.save()
            tbl_assignrehabstf.objects.create(juvenile=juvenile, rehabilitationstaff=selected_rehab)
            return render(request, 'Admin/AssignRehab.html', {'msg': "Staff Assigned Successfully", 'juvenile': juvenile, 'rehab': rehab})
    return render(request, 'Admin/AssignRehab.html', {'juvenile': juvenile, 'rehab': rehab})

def AssignHlt(request, id):
    juvenile = tbl_juvenile.objects.get(id=id)
    healthStaff = tbl_healthstaff.objects.all()
    if request.method == 'POST':
        selected_staff_id = request.POST.get("sel_staff")
        if selected_staff_id:
            selected_hlt = tbl_healthstaff.objects.get(id=selected_staff_id)
            tbl_assignhltstf.objects.create(juvenile=juvenile, healthstaff=selected_hlt)
            return render(request, 'Admin/AssignHlt.html', {'msg': "Staff Assigned Successfully", 'juvenile': juvenile, 'healthStaff': healthStaff})
    return render(request, 'Admin/AssignHlt.html', {'juvenile': juvenile, 'healthStaff': healthStaff})

def AssignEdu(request, id):
    juvenile = tbl_juvenile.objects.get(id=id)
    educationalStaff = tbl_educationalstaff.objects.all()
    if request.method == 'POST':
        selected_staff_id = request.POST.get("sel_staff")
        if selected_staff_id:
            selected_edu = tbl_educationalstaff.objects.get(id=selected_staff_id)
            tbl_assignedustf.objects.create(juvenile=juvenile, educationalstaff=selected_edu)
            return render(request, 'Admin/AssignEdu.html', {'msg': "Staff Assigned Successfully", 'juvenile': juvenile, 'educationalStaff': educationalStaff})
    return render(request, 'Admin/AssignEdu.html', {'juvenile': juvenile, 'educationalStaff': educationalStaff})

def logout(request):
    del request.session["aid"]
    return redirect("Guest:Login")

def case_data(request):
    casetype = tbl_casetype.objects.all()
    count = []
    for i in casetype:
        case = tbl_case.objects.filter(casetype=i.id).count()
        count.append(case)
    case_data = {
        'labels': [ctype.case_type for ctype in casetype],
        'counts': count     # Juvenile counts
    }

    return JsonResponse(case_data)

def pie_chart(request):
    return render(request, 'Admin/HomePage.html')

def complaint_report(request):
    # Get complaints count grouped by month
    complaints_per_month = (
        tbl_complaint.objects
        .extra(select={'month': "strftime('%%m', complaint_date)"})
        .values('month')
        .annotate(total=Count('id'))
        .order_by('month')
    )

    # Prepare data for the chart
    labels = [entry['month'] for entry in complaints_per_month]
    data = [entry['total'] for entry in complaints_per_month]

    return render(request, "admin/complaint_report.html", {
        "labels": labels,
        "data": data
    })
 
def SystemReport(request):
    return render(request,'Admin/SystemReport.html')

def complaint_report(request):
    # Ensure compatibility across databases (SQLite, MySQL, etc.)
    complaints_per_month = (
        tbl_complaint.objects
        .extra(select={'month': "strftime('%%m', complaint_date)"})  # SQLite example
        .values('month')
        .annotate(total=Count('id'))
        .order_by('month')
    )

    # Map numeric months to month names
    month_mapping = {
        "01": "January", "02": "February", "03": "March", "04": "April",
        "05": "May", "06": "June", "07": "July", "08": "August",
        "09": "September", "10": "October", "11": "November", "12": "December"
    }

    labels = [month_mapping.get(entry['month'], entry['month']) for entry in complaints_per_month]
    data = [entry['total'] for entry in complaints_per_month]

    print("Labels:", labels)  # Debugging
    print("Data:", data)      # Debugging

    return render(request, "admin/complaint_report.html", {
        "labels": json.dumps(labels),
        "data": json.dumps(data)
    })

def juveniles_enrolled(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        # Get the filtered queryset
        Juvenile = tbl_juvenile.objects.filter(
            juvenile_admissiondate__gte=start_date,
            juvenile_admissiondate__lte=end_date
        )
        
        # Aggregate data by month
        monthly_data = (tbl_juvenile.objects
                       .filter(juvenile_admissiondate__gte=start_date,
                              juvenile_admissiondate__lte=end_date)
                       .annotate(month=TruncMonth('juvenile_admissiondate'))
                       .values('month')
                       .annotate(count=Count('id'))
                       .order_by('month'))
        
        # Prepare data for the chart
        month_labels = [data['month'].strftime('%B %Y') for data in monthly_data]
        month_counts = [data['count'] for data in monthly_data]
        
        context = {
            'Juvenile': Juvenile,
            'month_labels': json.dumps(month_labels),
            'month_counts': json.dumps(month_counts),
        }
        
        return render(request, 'Admin/juveniles_enrolled.html', context)
    else:
        return render(request, 'Admin/juveniles_enrolled.html')
    

def upcoming_appointments_report(request):
    today = timezone.now().date()
    
    # Get date range from request
    start_date = request.GET.get('start_date', today)
    end_date = request.GET.get('end_date', today + timezone.timedelta(days=30))
    
    # Convert string dates to date objects
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
    except (ValueError, TypeError):
        start_date = today
        end_date = today + timezone.timedelta(days=30)
    
    # Get all appointments within date range (no status filter)
    upcoming = tbl_appointment.objects.filter(
        appointment_fordate__gte=start_date,
        appointment_fordate__lte=end_date
    ).select_related('juvenile').order_by('appointment_fordate', 'appointment_fortime')
    
    context = {
        'appointments': upcoming,
        'start_date': start_date.strftime('%Y-%m-%d'),
        'end_date': end_date.strftime('%Y-%m-%d'),
        'today': today.strftime('%Y-%m-%d'),
        'next_month': (today + timezone.timedelta(days=30)).strftime('%Y-%m-%d')
    }
    return render(request, 'admin/upcoming_appointments_report.html', context)


def admin_gender_report(request):
    # Count juveniles based on gender
    gender_distribution = tbl_juvenile.objects.values('juvenile_gender').annotate(count=Count('juvenile_gender'))

    # Get all juvenile details
    juvenile_details = tbl_juvenile.objects.all()

    context = {
        'gender_distribution': gender_distribution,
        'juvenile_details': juvenile_details,
    }

    return render(request, 'Admin/admin_gender_report.html', context)



def admin_juvenile_report(request):
    # Define age groups
    age_groups = {
        'Under 10': (0, 9),
        '10-14': (10, 14),
        '15-17': (15, 17),
        
    }

    # Count juveniles in each group
    age_distribution = {}
    for group, (min_age, max_age) in age_groups.items():
        count = tbl_juvenile.objects.filter(juvenile_age__gte=min_age, juvenile_age__lte=max_age).count()
        age_distribution[group] = count

    # Get details of all juveniles
    juvenile_details = tbl_juvenile.objects.all()

    context = {
        'age_distribution': age_distribution,
        'juvenile_details': juvenile_details,
    }

    return render(request, 'Admin/age_distribution_report.html', context)