from django.db import models
from django.urls import reverse
from .scoville_scale import ScovilleScale
# from .profile import Profile
from django.contrib.auth.models import User

class Blogpost(models.Model):

    title = models.CharField(max_length=255)
    body = models.CharField(max_length=1000, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    tolerance = models.CharField(max_length=100)
    image = models.FilePathField(path="./scovilleapp/static/img", null=True)
    video = models.CharField(max_length=255, null=True)
    scoville_scale = models.ForeignKey(ScovilleScale, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blogposts', null=True)


    class Meta:
        verbose_name = ("blogpost")
        verbose_name_plural = ("blogposts")
        ordering = ['-created_on'] #this will sort results in descending order per the created_on field

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'

    def get_absolute_url(self):
        return reverse("blogpost_detail", kwargs={"pk": self.pk})
