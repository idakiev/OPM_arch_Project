from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from OPM_arch_Project.web_app import views

urlpatterns = [
    path('', views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
