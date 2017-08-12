from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'',  include('django.contrib.auth.urls')),
    url(r'^profile/', views.UserProfileView.as_view(), name='profile')
]
