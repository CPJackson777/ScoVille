from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from scovilleapp.models import Blogpost, ScovilleScale
from scovilleapp.views.blog_posts.blog_post_detail import blogpost_details, get_blogpost

#GET form to ADD/CREATE a blog post
@login_required
def blogpost_form(request):
    '''Getting the form 
'''
    if request.method == 'GET':
        blogpost_list = Blogpost.objects.all()
        template = 'blog_post/blogpost_form.html'
        context = {
            'blogpost_list': blogpost_list
        }
        return render(request, template, context)

#GET form to EDIT/UPDATE a blog post
@login_required
def blogpost_edit_form(request, blogpost_id):
    if request.method == 'GET':
        blogpost = get_blogpost(blogpost_id)
        blogpost_list = Blogpost.objects.all()
        template = 'blog_post/blogpost_form.html'
        context = {
            'blogpost': blogpost
        }

        return render(request, template, context)