from django.db import models

# Create your models here.


class Value(models.Model):

    text = models.TextField()


class Principle(models.Model):

    text = models.TextField()
