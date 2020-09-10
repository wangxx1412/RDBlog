from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=2000)
