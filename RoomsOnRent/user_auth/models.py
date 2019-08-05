from django.db import models
from django.contrib.auth.models import User
from user_auth.choices import * 

def upload_avatr(instance,filename):
    return "media/{user}/{filename}/".format(user=instance.user,filename=filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name = 'userprofile')
    avtar = models.ImageField(upload_to=upload_avatr, blank=True, null=True)
    mobile = models.BigIntegerField(blank=False)
    state = models.CharField(choices= STATES_UNION_TERRITORIES,max_length=256, blank=False)
    city = models.CharField(max_length=256, blank=False)
    locality = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return self.user.username
