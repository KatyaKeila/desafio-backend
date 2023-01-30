from django.db import models


class Form(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(max_length=600)
