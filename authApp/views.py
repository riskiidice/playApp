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
        user_obj = UserProfile.object.get(request.user)
        print user_obj
        return HttpResponse('eiei')

