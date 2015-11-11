# Register your models here.
from django.contrib import admin

from .models import ProfileStore


class FBAPIAdmin(admin.ModelAdmin):
    name = 'Name'
    api_string = 'Api Info'
    bPic = 'Backup Picture'


admin.site.register(ProfileStore, FBAPIAdmin)
