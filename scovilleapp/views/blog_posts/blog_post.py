import sqlite3
from django.shortcuts import redirect, render, reverse
from scovilleapp.models import BlogPost
from ..connection import Connection
from scovilleapp.models import model_factory
from django.contrib.auth.decorators import login_required


def blogpost_list(request):
    if request.method == 'GET':
        all_blogposts = BlogPost.objects.all().order_by('created_on')

        template = 'blog_post/blogpost_list.html'
        context = {
            'all_blogposts': all_blogposts
        }
        return render(request, template, context)