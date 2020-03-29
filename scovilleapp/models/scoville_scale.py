from django.db import models
from django.urls import reverse

class ScovilleScale(models.Model):

    image = models.FilePathField(path="/img")
    pepper_name = models.CharField(max_length=100)
    heat_range = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("scovilleScale")
        verbose_name_plural = ("scovilleScales")

    def __str__(self):
        return self.pepper_name

    def get_absolute_url(self):
        return reverse("scovilleScale_detail", kwargs={"pk": self.pk})
