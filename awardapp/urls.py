from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    path('',views.welcome,name='welcome'),
    path('',views.index,name='index'),
    path('login/',views.signin,name='login'),
    path('register/',views.register,name='register'),
    path('signout/',views.signout,name='signout'),
    path('profile/',views.profile,name='profile'),
    path('addpost/',views.addpost,name='addpost'),
    path('new-project/', views.postproject, name='newproject'),
    path('update', views.update_profile, name='update'),
    path('search/', views.search_project, name='search'),
    path('vote/(<post_id>\d+)', views.project, name='vote'), 
    path('api/post/', views.PostItems.as_view()),
    path('api/profile/', views.ProfileItems.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('api/profile',views.ProfileItems.as_view(), name='apiprofiles'),



   
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

