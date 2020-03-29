import sqlite3
from django.shortcuts import redirect, render, reverse
from scovilleapp.models import Blogpost
from ..connection import Connection
from django.contrib.auth.decorators import login_required


def blogpost_list(request):
    if request.method == 'GET':
        all_blogposts = Blogpost.objects.all().order_by('created_on')

        template = 'blog_post/blogpost_list.html'
        context = {
            'all_blogposts': all_blogposts
        }
        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        new_blogpost = Blogpost.objects.create(
            title = form_data['title'],
            body = form_data['body'],
            tolerance = form_data['tolerance'],
            image = form_data['image'],
            author = request.user.id,
            scoville_scale = form_data['scoville_scale']
        )

        # and then save to the db
       
        new_blogpost.save()

        return redirect(reverse('scovilleapp:blogposts'))