from django.db import models
from django.contrib.auth.models import User


class UserClass(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username


class Deck(models.Model):
    name = models.CharField(max_length=200, null=True)
    sub_name = models.CharField(max_length=20, null=True)
    date_created = models.DateField(auto_now_add=True, null=True)
    owner = models.ForeignKey(
        UserClass, null=True, blank=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Card(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=1000)
    deck = models.ForeignKey(Deck, null=True, on_delete=models.CASCADE)
