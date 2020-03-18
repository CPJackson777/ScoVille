from django.conf.urls import url
from django.urls import include, path
from .views import *
# from sc import views as core_views

app_name = "scovilleapp"

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
]