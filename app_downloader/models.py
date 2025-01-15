from django.db import models


class ImageHistory(models.Model):
    sourse_link = models.CharField(max_length=250)
    image = models.ImageField(upload_to="image")
