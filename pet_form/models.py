from django.db import models

class Pet(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    behavior = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)

    def __str__(self):
        return self.name
# Create your models here.
