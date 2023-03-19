from django.db import models


class Item(models.Model):
    text = models.CharField(max_length=256, null=False, default='')
    list = models.ForeignKey('List', on_delete=models.CASCADE, default=None)


class List(models.Model):
    pass
