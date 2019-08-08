from django import forms
from room_service.models import Room,RoomImages
from django.forms.models import inlineformset_factory



class RoomImagesForm(forms.ModelForm):

    class Meta:
        model = RoomImages
        fields = ('room_image', )
        widgets = {
              'room_image':forms.FileInput(attrs={'type':'file', 'class':'form-control'})
        }


class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ('state','city_area','street_address','mobile','room_status','religious_group','monthly_rent','desciption','cover_image')
        widgets = {
               'state':forms.Select(attrs={'type':'select','class':'form-control'}),
               'city_area':forms.TextInput(attrs={'type':'text','class':'form-control'}),
               'street_address':forms.TextInput(attrs={'type':'text','class':'form-control'}),
               'mobile':forms.NumberInput(attrs={'type':'number','class':'form-control'}),
               'religious_group':forms.Select(attrs={'type':'select','class':'form-control'}),
               'room_status':forms.CheckboxInput(attrs={'type':'checkbox','class':''}),
               'monthly_rent':forms.NumberInput(attrs={'type':'number','class':'form-control'}),
               'desciption':forms.Textarea(attrs={'class':'editable medium-editor-textarea form-control  '}),
               'cover_image':forms.FileInput(attrs={'class':'form-control'}),
        }
