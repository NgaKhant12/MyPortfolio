from django.urls import path
from .views import send_email_view

from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('info/',views.personal_info,name='info'),
    path('projects/',views.projects,name='projects'),
    path('contact/',views.contact,name='contact'),
    path('service/',views.service,name='service'),
    path('send-email/', send_email_view, name='send_email'),


]
