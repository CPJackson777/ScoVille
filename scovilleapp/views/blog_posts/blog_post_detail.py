import sqlite3
from django.shortcuts import redirect, render, reverse
from django.contrib.auth.decorators import login_required
from scovilleapp.models import Blogpost, ScovilleScale
from ..connection import Connection
# from scovilleapp.models import model_factory


def get_blogpost(blogpost_id):
    return Blogpost.objects.get(pk=blogpost_id)

# @login_required
def blogpost_details(request, blogpost_id):
    if request.method == 'GET':
        blogpost = get_blogpost(blogpost_id)

        template = 'blog_post/blogpost_detail.html'
        context = {
            'blogpost': blogpost
        }
        return render(request, template, context)


    elif request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for editing a blogpost
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

        # # retrieve it first:
            blogpost_to_update = Blogpost.objects.get(pk=blogpost_id)

            # # Reassign a property's value
            blogpost_to_update.title = form_data['title']
            blogpost_to_update.body = form_data['body']
            blogpost_to_update.created_on = form_data['created_on']
            blogpost_to_update.tolerance = form_data['tolerance']
            blogpost_to_update.image = form_data['image']
            blogpost_to_update.author = form_data['author']
            blogpost_to_update.scoville_scale = form_data['scoville_scale']

            # # Save the change to the db
            blogpost_to_update.save()

            return redirect(reverse('scovilleapp:blogposts'))