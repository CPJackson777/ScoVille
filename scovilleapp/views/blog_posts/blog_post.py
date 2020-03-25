import sqlite3
from django.shortcuts import redirect, render, reverse
from scovilleapp.models import ScovilleScale
from ..connection import Connection
from scovilleapp.models import model_factory

def blogpost_list(request):
    if request.method == 'GET':
        all_blogposts = ScovilleScale.objects.all()

        template = 'blog_post/blogpost_list.html'
        context = {
            'all_blogposts': all_blogposts
        }
        return render(request, template, context)