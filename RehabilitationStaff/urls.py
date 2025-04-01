from django.urls import path,include
from RehabilitationStaff import views
app_name='RehabilitationStaff'
urlpatterns = [
    path('HomePage/',views.Homepage,name="HomePage"),
    path('MyProfile/',views.MyProfile,name="MyProfile"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
    path('ViewJuvenile/',views.ViewJuvenile,name="ViewJuvenile"),
    path('AddRehabReport/<int:id>',views.AddRehabReport,name="AddRehabReport"),
    path('editedureport/<int:rid>/<int:id>',views.editedureport,name="editedureport"),
    path('logout/',views.logout,name='logout'),
]
