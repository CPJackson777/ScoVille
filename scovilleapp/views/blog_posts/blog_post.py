import sqlite3
from django.shortcuts import redirect, render, reverse
from scovilleapp.models import Blogpost
from ..connection import Connection
from django.contrib.auth.decorators import login_required


def blogpost_list(request, scoville_scale_id=None):
    if request.method == 'GET':
        if scoville_scale_id is not None:
            all_blogposts = Blogpost.objects.filter(scoville_scale_id = scoville_scale_id)
        else:   
            all_blogposts = Blogpost.objects.all().order_by('created_on')

        template = 'blog_post/blogpost_list.html'
        context = {
            'all_blogposts': all_blogposts, #the value is the list of blogs being retrieved by the view on line 11
            'scoville_scale_id': scoville_scale_id
        }
        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        #make blog post instance and save to database at the same time
        new_blogpost = Blogpost.objects.create(
            title = form_data['title'],
            body = form_data['body'],
            tolerance = form_data['tolerance'],
            blog_image = form_data['blog_image'],
            author_id = request.user.id,
            scoville_scale_id = form_data['scoville_scale']
        )


        return redirect(reverse('scovilleapp:blogposts'))
