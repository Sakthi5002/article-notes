from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Link(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text
