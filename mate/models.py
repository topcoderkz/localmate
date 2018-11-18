from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_mate = models.BooleanField(default=False)
    is_guest = models.BooleanField(default=False)


class Skill(models.Model):
    name = models.CharField(max_length=200)
    proficiency = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Mate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    skills = models.ManyToManyField(Skill)
