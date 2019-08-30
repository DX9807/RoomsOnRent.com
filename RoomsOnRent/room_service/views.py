from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from room_service.models import Room, RoomImages
from django.contrib.auth.models import User
from django.utils import timezone
from room_service.forms import RoomForm, RoomImagesForm
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect,HttpResponse
from django.forms.models import modelformset_factory


class RoomCreateView(CreateView,LoginRequiredMixin,):
    login_url = '/login/'
    redirect_field_name = 'room_service/room_detail.html'
    form_class = RoomForm
    model =Room
    def form_valid(self, form):
        room = form.save(commit=False)
        room.ownner =  self.request.user
        room.save()
        return HttpResponseRedirect(reverse_lazy("room_service:room_detail",kwargs={'pk':room.pk}))





@login_required
def add_images_to_room(request, pk):
    ImageFormSet = modelformset_factory(RoomImages,
                                        form=RoomImagesForm, extra=5)
    room = get_object_or_404(Room, pk=pk)
    if request.method == "POST":
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=RoomImages.objects.none())
        if formset.is_valid():
            for form in formset:
                data = form.save(commit=False)
                data.room = room
                if 'room_image' in request.FILES:
                    data.room_image = request.FILES['room_image']


                data.save()
            return redirect('room_service:room_detail', pk=room.pk)
    else:
        formset = ImageFormSet(queryset=RoomImages.objects.none())
    return render(request, 'room_service/add_images.html', {'formset': formset})



@login_required
def image_remove(request, pk):
    image = get_object_or_404(RoomImages, pk=pk)
    room_pk = image.room.pk
    image.delete()
    return redirect('room_service:room_detail', pk=room_pk)


class RoomDeleteView(LoginRequiredMixin,DeleteView):
    model = Room
    success_url = reverse_lazy('room_service:room_list')



class RoomUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'room_service/room_detail.html'
    template_name = 'room_service/room_form.html'
    form_class = RoomForm

    model = Room



class RoomListView(ListView):
    model = Room

    def get_queryset(self):
        return Room.objects.filter(added_date__lte=timezone.now()).order_by('-added_date')

class RoomDetailView(DetailView):
    model = Room


##Creating add room form for the user.....................................
@login_required
def room_on_rent(request):

    ImageFormSet = modelformset_factory(RoomImages,
                                        form=RoomImagesForm, extra=3)

    if request.method == 'POST':

        roomform = RoomForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=RoomImages.objects.none())


        if roomform.is_valid() and formset.is_valid():
            room_form = roomform.save(commit=False)
            room_form.ownner = request.user
            room_form.save()

            for form in formset.cleaned_data:
                image = form['room_image']
                photo = RoomImages(room=room_form, room_image=image)
                photo.save()

            return HttpResponseRedirect("room_service/room_detail.htm")
        else:
            print(roomform.errors, formset.errors)
    else:
        roomform = RoomForm()
        formset = ImageFormSet(queryset=RoomImages.objects.none())
    return render(request, 'room_service/room_form.html',{'roomform': roomform, 'formset': formset})
