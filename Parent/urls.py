
from django.urls import path,include
from Parent import views
app_name='Parent'
urlpatterns = [
    path('Homepage/',views.Homepage,name="Homepage"),

    path('MyProfile/',views.MyProfile,name="MyProfile"),

    path('EditProfile/',views.EditProfile,name="EditProfile"),

    path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
     
    path('JuvenileDetails/',views.JuvenileDetails,name="JuvenileDetails"),

    path('JuvenileCaseDetails/<int:id>',views.JuvenileCaseDetails,name="JuvenileCaseDetails"),

    path('ViewJuvenile/',views.ViewJuvenile,name="ViewJuvenile"),

    path('ViewHearing/<int:id>',views.ViewHearing,name="ViewHearing"),

    path('AddComplaint/',views.AddComplaint,name="AddComplaint"),

    path('Appointment/<int:id>',views.Appointment,name="Appointment"),
    
    path('ViewAppointment/',views.ViewAppointment,name="ViewAppointment"),

    path('ViewLawyer/<int:id>',views.ViewLawyer,name="ViewLawyer"),

    path("payment/<int:id>",views.payment,name="payment"),
    path('loader/',views.loader, name='loader'),
    path('paymentsuc/',views.paymentsuc, name='paymentsuc'),

    path('ViewEReport/',views.ViewEReport,name='ViewEReport'),
    path('ViewHReport/',views.ViewHReport,name='ViewHReport'),
    path('ViewRReport/',views.ViewRReport,name='ViewRReport'),

    path('Report/',views.Report,name='Report'),

    path('logout/',views.logout,name='logout'),
]

    

