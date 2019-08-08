from django.contrib import admin
from room_service.models import Room,RoomImages




class RoomAdmin(admin.ModelAdmin):
    list_display = ('state','city_area','street_address','mobile','room_status','religious_group','monthly_rent',)



class RoomImagesAdmin(admin.ModelAdmin):
    list_display = ('room_image',)
    
admin.site.register(Room,RoomAdmin)
admin.site.register(RoomImages,RoomImagesAdmin)
