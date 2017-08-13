from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView, View
from models import UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group,User
from videoApp.models import Album, Video

# Create your views here.

class UserProfileView(LoginRequiredMixin, View):
    model = UserProfile
    template_name = 'registration/profile.html'

    def get(self, request):

        user_obj = UserProfile.objects.get(owner = request.user)
        group = Group.objects.get(name = user_obj.group)
        album_obj = Album.objects.get(group = group)
        context = {
            'user_detail' : user_obj,
            'album': album_obj
        }

        return render(request,self.template_name , context)


