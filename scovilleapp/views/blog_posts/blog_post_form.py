from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from scovilleapp.models import Blogpost, ScovilleScale
from scovilleapp.views.blog_posts.blog_post_detail import blogpost_details, get_blogpost

#GET form to ADD/CREATE a blog post
@login_required
def blogpost_form(request, scoville_scale_id=None):
    '''Getting the form 
'''
    if request.method == 'GET':
        if scoville_scale_id is not None:
            scales = ScovilleScale.objects.filter(id = scoville_scale_id)
        else:
            scales = ScovilleScale.objects.all()
        template = 'blog_post/blogpost_form.html'
        context = {
            'scales': scales
        }
        for scale in scales: 
            print('scale', scale)
        return render(request, template, context)

#GET form to EDIT/UPDATE a blog post
@login_required
def blogpost_edit_form(request, blogpost_id):
    if request.method == 'GET':
        blogpost = Blogpost.objects.get(id=blogpost_id) 
        scales = ScovilleScale.objects.all()
        
        template = 'blog_post/blogpost_form.html'
        context = {
            'blogpost': blogpost,
            'scales': scales
        }
        print('blogpost', blogpost)
        return render(request, template, context)