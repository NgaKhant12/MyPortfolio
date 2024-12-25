from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('info/',views.personal_info,name='info'),
    path('projects/',views.projects,name='projects'),
    path('contact/',views.contact,name='contact'),
]
