from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name = 'home'),
    path('profile/',views.project,name = 'profile'),
    path('project/',views.project,name = 'project'),
    path('add-project/',views.add_project,name = 'addproject'),

]