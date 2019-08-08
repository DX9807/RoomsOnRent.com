from django.urls import path
from room_service.views import  (
                                room_on_rent,
                                RoomCreateView,
                                RoomListView,
                                RoomDetailView,
                                RoomDeleteView,
                                RoomUpdateView,
                                add_images_to_room,
                                image_remove,
                                )

app_name = 'room_service'

urlpatterns = [
             path('',RoomListView.as_view(),name='room_list'),
             path('add/',RoomCreateView.as_view(),name='add-room'),

             path('room/<int:pk>/',RoomDetailView.as_view(), name='room_detail'),
             path('room/<int:pk>/edit/',RoomUpdateView.as_view(), name='room_edit'),
             path('room/<int:pk>/remove/',RoomDeleteView.as_view(), name='room_remove'),
             path('room/<int:pk>/image/', add_images_to_room, name='add_image_to_room'),
             path('image/<int:pk>/remove/',image_remove, name='image_remove'),
             ]
