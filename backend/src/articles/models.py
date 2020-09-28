from django.db import models


class Article(models.Model):
    title = models.CharField(max_lenght=30)
    text = models.TextField()

