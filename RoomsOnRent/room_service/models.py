from django.db import models
from django.utils import timezone
from django.urls import  reverse
from django.contrib.auth.models import User
from user_auth.choices import *

def upload_room_images(instance,filename):
    return "Room/Images/{room}/{filename}/".format(room=instance.room,filename=filename)


def upload_cover_image(instance,filename):
    return "Room/cover/{id}/{filename}/".format(id=instance.id,filename=filename)

class Room(models.Model):
    ownner = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(choices = STATES_UNION_TERRITORIES,blank=False, max_length=256 )
    city_area = models.CharField(blank=False, max_length=256)
    street_address = models.CharField(blank=False, max_length=300)
    mobile = models.BigIntegerField(blank=False)
    room_status = models.CharField(blank=False, max_length=10)
    religious_group = models.CharField(choices = RELIGIOUS_GROUP , max_length=15)
    monthly_rent = models.CharField(blank=False,max_length=10)
    desciption = models.TextField(blank=True,max_length=2048)
    added_date = models.DateTimeField(auto_now=True)
    cover_image = models.ImageField(upload_to =upload_cover_image, blank=False )

    def __str__(self):
        return "Room-{id}".format(id=str(self.id))



class RoomImages(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE ,related_name='room_images')
    room_image = models.ImageField(upload_to=upload_room_images,null=False, blank=False)

    def get_absolute_url(self):
        return reverse("room_service:room_list")

    def __str__(self):
        return str(self.room)
