from django.urls import path

from . import views

urlpatterns = [
    path("auth/", views.request_authentication, name="spotifyauth-auth"),
    path("callback/", views.callback, name="spotifyauth-callback"),
]