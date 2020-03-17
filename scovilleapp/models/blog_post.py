from django.db import models
from django.urls import reverse
from .scoville_scale import ScovilleScale
from .user import User

class BlogPost(models.Model):

    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    tolerance = models.CharField(max_length=100)
    image = models.FilePathField(path="/img")
    video = image = models.CharField(max_length=255)
    scoville_scale = models.ForeignKey(ScovilleScale, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("BlogPost")
        verbose_name_plural = ("BlogPosts")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("BlogPost_detail", kwargs={"pk": self.pk})
