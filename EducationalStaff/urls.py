from django.urls import path
from EducationalStaff import views
app_name='EducationalStaff'

urlpatterns = [ 
    path('MyProfile/',views.MyProfile,name="MyProfile"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
    path('HomePage/',views.HomePage,name="HomePage"),
    path('ViewJuvenile/',views.ViewJuvenile,name="ViewJuvenile"),
    path('AddEduReport/<int:jid>',views.AddEduReport,name="AddEduReport"),
    path('editedureport/<int:edid>',views.editedureport,name="editedureport"),
    path('logout/',views.logout,name="logout"),

]