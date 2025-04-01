from django.urls import path
from Lawyer import views
app_name='Lawyer'

urlpatterns = [ 
    path('MyProfile/',views.MyProfile,name="MyProfile"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
    path('AddHearing/<int:id>',views.AddHearing,name="AddHearing"),
    path('HomePage/',views.HomePage,name="HomePage"),
    path('ViewJuvenile/',views.ViewJuvenile,name="ViewJuvenile"),
    path('ViewEReport/',views.ViewEReport,name='ViewEReport'),
    path('ViewHReport/',views.ViewHReport,name='ViewHReport'),
    path('ViewRReport/',views.ViewRReport,name='ViewRReport'),
    path('Report/',views.Report,name='Report'),
    path('logout/',views.logout,name="logout"),
    path('Payment/',views.Payment,name="Payment"),
]
