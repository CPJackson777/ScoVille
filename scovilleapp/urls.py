# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *


app_name = "scovilleapp"

urlpatterns = [
   path('', home, name='home'),
   path('accounts/', include('django.contrib.auth.urls')),
   path('logout/', logout_user, name='logout'),
   path('register/', register_user, name='register'),
   path('scovillescale/', scovillescale_list, name='scovillescale'), 
   path('blogposts/', blogpost_list, name='blogposts'),
   path('blogposts/<int:blogpost_id>/', blogpost_details, name='blogpost'),
   
    
]