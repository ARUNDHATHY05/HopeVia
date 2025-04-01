from django.urls import path,include
from HealthStaff import views
app_name='HealthStaff'
urlpatterns = [
    path('HomePage/',views.HomePage,name="HomePage"),
    path('MyProfile/',views.MyProfile,name="MyProfile"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
    path('ViewJuvenile/',views.ViewJuvenile,name="ViewJuvenile"),
    path('AddHltReport/<int:id>',views.AddHltReport,name="AddHltReport"),
    path('editedureport/<int:hlthid>',views.editedureport,name="editedureport"),
    path('logout/',views.logout,name="logout"),
]


