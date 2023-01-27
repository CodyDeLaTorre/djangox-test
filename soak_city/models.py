from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Water(models.Model):
  name = models.CharField(max_length=256)
  description = models.TextField("")
  ph_level = models.CharField(max_length=256)
  electrolyte = models.CharField(max_length=256)
  cost = models.IntegerField()

  def __str__(self):
        return self.name

  def get_absolute_url(self):
      return reverse("water_detail", args=[str(self.id)])
  