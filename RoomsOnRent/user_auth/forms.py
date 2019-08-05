from django import forms
from django.contrib.auth.models import User

from user_auth.models import UserProfile

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password')
        widgets = {
                  'first_name':forms.TextInput(attrs={'type':'text','placeholder':'Firstname',}),
                  'last_name':forms.TextInput(attrs={'type':'text','placeholder':'Lastname',}),
                  'username':forms.TextInput(attrs={'type':'text','placeholder':'Username',}),
                  'email':forms.EmailInput(attrs={'type':'email','placeholder':'Email',}),
                  'password':forms.TextInput(attrs={'type':'password','placeholder':'********',})
                  }

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = (
                  'mobile',
                  'state',
                  'city',
                  'locality',
                  'avtar'
                 )
        widgets = {
                    'mobile':forms.NumberInput(attrs={'type':'text','placeholder':'Mobile No.','class':'form-control'}),
                    'state':forms.Select(attrs={'type':'select','class':'form-control custom-select'}),
                    'city':forms.TextInput(attrs={'type':'text','placeholder':'City/Area','class':'form-control'}),
                    'locality':forms.TextInput(attrs={'type':'text','placeholder':'Locality','class':'form-control'}),
                    'avtar':forms.FileInput(attrs={'type':'file','placeholder':'Upload Image','class':'form-control'})
                           }
