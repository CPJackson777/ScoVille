#Auth views
from .auth.logout import logout_user
from .auth.register import register_user

#View for Home
from .home import home

#View for scoville scale page
from .scoville_scale.sslist import scovillescale_list

#Views for blog posts
from .blog_posts.blog_post import blogpost_list
from .blog_posts.blog_post_detail import blogpost_details
from .blog_posts.blog_post_form import blogpost_form, blogpost_edit_form