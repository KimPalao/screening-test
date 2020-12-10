from django.db import models

# Create your models here.


class Value(models.Model):

    text = models.CharField(max_length=127, unique=True)


class Principle(models.Model):

    text = models.CharField(max_length=127, unique=True)
