from django.contrib.auth.models import User
from django.db import models


class UserArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.url} - {self.user}"
