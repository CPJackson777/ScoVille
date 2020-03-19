# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *


app_name = "scovilleapp"

urlpatterns = [
   path('accounts/', include('django.contrib.auth.urls')),
   path('logout/', logout_user, name='logout'),
   path('register/', register_user, name='register'),
]