from django.db import models
from django.urls import reverse

class ScovilleScale(models.Model):

    pepper_name = models.CharField(max_length=100)
    heat_range = models.CharField(max_length=100)
    image = models.FilePathField(path="/img")

    class Meta:
        verbose_name = ("ScovilleScale")
        verbose_name_plural = ("ScovilleScales")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ScovilleScale_detail", kwargs={"pk": self.pk})
