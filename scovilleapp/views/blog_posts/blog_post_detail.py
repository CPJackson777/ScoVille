import sqlite3
from django.shortcuts import redirect, render, reverse
from scovilleapp.models import BlogPost
from ..connection import Connection
from scovilleapp.models import model_factory
from django.contrib.auth.decorators import login_required


def get_post(request, blogpost_id):
    if request.method == 'GET':
        blogpost = BlogPost.objects.get(pk=blogpost_id)

        template = 'blog_post/blogpost_detail.html'
        context = {
            'blogpost': blogpost
        }
        return render(request, template, context)