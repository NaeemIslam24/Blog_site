from django.db import models


class Register(models.Model):

    objects = None
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    age = models.IntegerField()
    def __str__(self):
        return self.name


