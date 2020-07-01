from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=265, unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=265, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class Users(models.Model):
    firstName = models.CharField(max_length=128)
    lastName = models.CharField(max_length=128)
    email = models.EmailField(max_length=264,unique=True)

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    portfolio = models.URLField(blank=True)
    pic = models.ImageField(upload_to='fapp/profileImgs', blank=True)

    def __str__(self):
        return self.user.username
