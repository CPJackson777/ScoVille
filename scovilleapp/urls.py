from django.conf.urls import url
from django.urls import include, path
from .views import *

app_name = "scovilleapp"

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
]