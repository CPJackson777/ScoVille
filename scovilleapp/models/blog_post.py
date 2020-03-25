from django.db import models
from django.urls import reverse
from .scoville_scale import ScovilleScale
from .profile import Profile
from django.contrib.auth.models import User

class BlogPost(models.Model):

    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    tolerance = models.CharField(max_length=100)
    image = models.FilePathField(path="/img", null=True)
    video = models.CharField(max_length=255, null=True)
    scoville_scale = models.ForeignKey("ScovilleScale", on_delete=models.CASCADE)
    profile_id = models.ForeignKey("Profile", on_delete=models.CASCADE, null=True)

    # class Meta:
    #     verbose_name = ("BlogPost")
    #     verbose_name_plural = ("BlogPosts")
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("BlogPost_detail", kwargs={"pk": self.pk})
