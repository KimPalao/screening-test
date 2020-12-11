from django.db import models

# Create your models here.


class JSONSerializableModel(models.Model):
    class Meta:
        abstract = True

    def to_json(self):
        json = {}
        for field in self._meta.fields:
            name = field.name
            value = getattr(self, name)
            if isinstance(value, (int, float, bool, str)):
                json[name] = getattr(self, name)
        return json


class Value(JSONSerializableModel):

    text = models.CharField(max_length=127, unique=True)


class Principle(JSONSerializableModel):

    text = models.CharField(max_length=127, unique=True)
