from django.db import models


class Comment(models.Model):
    username = models.EmailField()
    comment = models.TextField()
    like = models.BooleanField()
