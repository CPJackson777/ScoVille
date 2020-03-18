from django.conf.urls import url, include
# from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *


app_name = "scovilleapp"

urlpatterns = [
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/$', logout_user, name='logout'),
    url(r'^register/$', register_user, name='register'),
]