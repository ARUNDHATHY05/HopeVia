from django.urls import path
from Admin import views
app_name='Admin'

urlpatterns = [
    path('District/',views.District,name="District"),
    path('deldis/<int:did>',views.deldis,name="deldis"),
    path('editdis/<int:eid>',views.editdis,name="editdis"),

    path('CaseType/',views.CaseType,name="casetype"),
    path('delct/<int:dct>',views.delct,name="delct"),
    path('editct/<int:cid>',views.editct,name="editct"),

    path('Admin/',views.Admin,name="Admin"),
    path('delad/<int:aid>',views.delad,name="delad"),
    path('editad/<int:adid>',views.editad,name="editad"),

    path('place/',views.place,name="place"),
    path('delpl/<int:plid>',views.delpl,name="delpl"),
    path('editpl/<int:eplid>',views.editpl,name="editpl"),

    path('Category/',views.Category,name="category"),
    path('delcat/<int:cid>',views.delcat,name="delcat"),
    path('editcat/<int:eid>',views.editcat,name="editcat"),

    path('subcategory/',views.subcategory,name="subcategory"),
    path('delsub/<int:scid>',views.delsub,name="delsub"),
    path('editsub/<int:sctid>',views.editsub,name="editsub"),

    path('Lawyer/',views.Lawyer,name="Lawyer"),

   

    path('Parent/',views.Parent,name="Parent"),

    path('Juvenile/<int:id>',views.Juvenile,name='Juvenile'),

    path('ViewJuvenile/',views.ViewJuvenile,name='ViewJuvenile'),
    path('deljuv/<int:jid>',views.deljuv,name="deljuv"),

    path('Case/<int:id>',views.Case,name='Case'),

    path('HomePage/',views.HomePage,name='HomePage'),

    path('EducationalStaff/',views.EducationalStaff,name='EducationalStaff'),
    path('Ban/<int:id>',views.Ban,name='Ban'),

    path('HealthStaff/', views.HealthStaff, name='HealthStaff'),
    path('BanHealthStaff/<int:id>', views.BanHealthStaff, name='BanHealthStaff'),

    path('RehabilitationStaff/', views.RehabilitationStaff, name='RehabilitationStaff'),
    path('BanRehabilitationStaff/<int:id>', views.BanRehabilitationStaff, name='BanRehabilitationStaff'),

    path('ViewComplaint/',views.ViewComplaint,name='ViewComplaint'),

    path('ReplyComplaint/<int:id>',views.ReplyComplaint,name='ReplyComplaint'),

    path('JuvenileReg/',views.JuvenileReg,name="JuvenileReg"),

    path('ViewAppointment/',views.ViewAppointment,name='ViewAppointment'),
    path('reject/<int:id>',views.reject,name='reject'),
    path('accept/<int:id>',views.accept,name='accept'),

    path('ViewEReport/',views.ViewEReport,name='ViewEReport'),
    path('ViewHReport/',views.ViewHReport,name='ViewHReport'),
    path('ViewRReport/',views.ViewRReport,name='ViewRReport'),

    path('Report/',views.Report,name='Report'),

    path('AssignEdu/<int:id>',views.AssignEdu,name='AssignEdu'),
    path('AssignHlt/<int:id>',views.AssignHlt,name='AssignHlt'),
    path('AssignRehab/<int:id>',views.AssignRehab,name='AssignRehab'),

    path('AssignStaff/<int:id>',views.AssignStaff,name='AssignStaff'),

    path('pie_chart/', views.pie_chart, name='pie_chart'),
    path('case_data/', views.case_data, name='case_data'),

    path('logout/',views.logout,name='logout'),

    path('SystemReport/',views.SystemReport,name='SystemReport'),

    path('complaint_report/',views.complaint_report,name='complaint_report'),

    path('juveniles_enrolled/', views.juveniles_enrolled, name='juveniles_enrolled'),

  # Juvenile Age Group Distribution
    path('age_distribution_report/', views.admin_juvenile_report, name='age_distribution_report'),
    # Upcoming Appointments
    path('upcoming_appointments_report', views.upcoming_appointments_report, name='upcoming_appointments_report'),
    # Juvenile Gender Based Counts
    path('admin_gender_report/', views.admin_gender_report, name='admin_gender_report'),
 ]
