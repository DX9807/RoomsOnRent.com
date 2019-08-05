from django.shortcuts import render
from user_auth.forms import UserForm, UserProfileForm
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from user_auth.models import UserProfile
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexTemplateView(TemplateView):
    template_name='registration/index.html'

def register_user(request):
    registered=False
    if request.method=="POST":
        user_form = UserForm(data=request.POST)
        user_profile_form = UserProfileForm(data=request.POST)
        if user_profile_form.is_valid() and user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            user_profile = user_profile_form.save(commit=False)
            user_profile.user = user

            if "avtar" in request.FILES:
                user_profile.avtar = request.FILES['avtar']
            user_profile.save()
            registered=True
        else:
            print(user_form.errors,user_profile_form.errors)
    else:
        user_form=UserForm()
        user_profile_form=UserProfileForm()

    return render(request,'registration/registeration.html',{'user_form':user_form,
                                                             'user_profile_form':user_profile_form,
                                                             'registered':registered})

@login_required
def special(request):
    if request.user:
        user_data = UserProfile.objects.get(user=request.user)
        print(user_data)

    return render(request, 'registration/profile.html',{'user_data':user_data})


class UserUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'edit_profile.html'
    login_url = '/login/'
    redirect_field_name = 'registration/profile.html'

    form_class = UserForm
    model = User


class UserProfileUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'edit_profile.html'
    login_url = '/login/'
    redirect_field_name = 'registration/profile.html'

    form_class = UserProfileForm
    model = UserProfile
