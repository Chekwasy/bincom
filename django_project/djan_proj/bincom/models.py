from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Name(models.Model):
	name = models.CharField(max_length=100)
	posts = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
