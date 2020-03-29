import sqlite3
from django.shortcuts import redirect, render, reverse
from scovilleapp.models import Blogpost
from ..connection import Connection
from scovilleapp.models import model_factory
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

        new_blogpost = Blogpost(
            title = form_data['title'],
            body = form_data['body'],
            created_on = form_data['created_on'],
            tolerance = form_data['tolerance'],
            image = form_data['image'],
            author = form_data['author'],
            scoville_scale = form_data['scoville_scale']
        )

        # and then save to the db
        print(new_blogpost.author.user.username)
        new_blogpost.save()

        # Or...
        # Use a shortcut to do both at the same time
        # new_book = Book.objects.create(
        #     title = form_data['title'],
        #     author = form_data['author'],
        #     isbn = form_data['isbn'],
        #     year = form_data['year_published'],
        #     location_id = request.user.librarian.id,
        #     librarian_id = form_data["location"]
        # )

        return redirect(reverse('scovilleapp:blogposts'))