from django.db import models

class ScovilleScale(models.Model):

    '''
    *** This class creates a department and its properties ***
   
    Properties:
      pepper_name: This property will contain the name of pepper for the scoville scale category.
      heat_range: This property contains the numerical range of scoville heat units for the category.
      img: This property will contain an image of the pepper that the category is named after.
    '''

    class Meta:
        verbose_name = ("ScovilleScale")
        verbose_name_plural = ("ScovilleScales")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ScovilleScale_detail", kwargs={"pk": self.pk})
