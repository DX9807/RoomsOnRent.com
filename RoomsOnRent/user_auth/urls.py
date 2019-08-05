from django.urls import path
from user_auth.views import (
                             register_user,
                             special,
                             IndexTemplateView,
                             UserUpdateView,
                             UserProfileUpdateView,
                             )


app_name = 'user_auth'

urlpatterns = [
               path('register/',register_user,name='register'),
               path('edit-profile/',special,name='edit-profile'),
               path('user/<int:pk>/update',UserUpdateView.as_view(),name='user-update'),
               # path('user/<int:pk>/update',UserProfileUpdateView.as_view(),name='user-update'),
              ]
