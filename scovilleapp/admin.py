from django.contrib import admin

# Import your models here.
from .models import Blogpost
# from .models import ScovilleScale


# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
admin.site.register(Blogpost)