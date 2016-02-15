from django.db import models


class List(models.Model):
    pass


class Item(models.Model):
    """docstring for Item"""
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)


# Create your models here.
