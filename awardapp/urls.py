from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name = 'home'),
    path('create_profile/',views.create_profile,name = 'create_profile'),
    path('profile/',views.project,name = 'profile'),
    path('project/',views.project,name = 'project'),
    path('add_project/',views.add_project,name = 'addproject'),
    path('rate_project/(<image_id>\d+)',views.rate_project,name = 'rate_project'),
    path('search_project/(<image_id>\d+)',views.project_search,name = 'search_project'),
]