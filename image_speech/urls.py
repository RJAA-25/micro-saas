from django.urls import path

from .views import *

app_name = "image_speech"
urlpatterns = [
    path("", index, name="index"),
    path("new/", create, name="create"),
    path("generate/", generate, name="generate"),
    path("<uuid:uuid>/", detail, name="detail"),
    path("<uuid:uuid>/regenerate", regenerate, name="regenerate"),
]
