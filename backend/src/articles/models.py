from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()

    def __str__(self):
        return f'{self.pk}--{self.title}'
