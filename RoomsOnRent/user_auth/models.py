from django.db import models
from django.contrib.auth.models import User
from user_auth.choices import *




class States(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=30)
    state = models.ForeignKey(States, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

def upload_avatr(instance,filename):
    return "media/{user}/{filename}/".format(user=instance.user,filename=filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name = 'userprofile')
    avtar = models.ImageField(upload_to=upload_avatr, blank=True, null=True)
    mobile = models.BigIntegerField(blank=False)
    state = models.ForeignKey(States, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    locality = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return self.user.username
