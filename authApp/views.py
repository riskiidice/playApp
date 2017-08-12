from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView, View
from django.utils import timezone
from models import UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class UserProfileView(LoginRequiredMixin, View):
    model = UserProfile
    context_object_name = 'all_albums'
    template_name = 'registration/profile.html'

    def get_queryset(self):

        return UserProfile.objects.get(self.pk)
