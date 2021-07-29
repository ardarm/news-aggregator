from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.url} - {self.user}"
