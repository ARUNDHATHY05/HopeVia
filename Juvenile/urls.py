

from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('Admin/',include('Admin.urls')),
    path('',include('Guest.urls')),
    path('Parent/',include('Parent.urls')),
    path('Lawyer/',include('Lawyer.urls')),
    path('EducationalStaff/',include('EducationalStaff.urls')),
    path('HealthStaff/',include('HealthStaff.urls')),
    path('RehabilitationStaff/',include('RehabilitationStaff.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)