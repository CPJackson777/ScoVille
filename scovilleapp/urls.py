# from django.conf.urls import url, include
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *


app_name = "scovilleapp"

urlpatterns = [
    path(r'accounts/', include('django.contrib.auth.urls')),
    path(r'^logout/$', logout_user, name='logout'),
    path(r'^register/$', register_user, name='register'),
]