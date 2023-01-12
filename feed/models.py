from django.db import models
from sorl.thumbnail import ImageField


class Post(models.Model):
    title = models.CharField(max_length=25, blank=False, null=False)
    text = models.CharField(max_length=140, blank=False, null=False)
    image = models.ImageField()

    def __str__(self):
        return self.text
