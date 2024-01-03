from django.contrib import admin

from .models import Image, Speech


# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Speech)
class SpeechAdmin(admin.ModelAdmin):
    pass
