# Register your models here.
from django.contrib import admin

from .models import ProfileStore


class FBAPIAdmin(admin.ModelAdmin):
    fields = ('Name', 'Api Info', 'Backup Picture')


admin.site.register(ProfileStore, FBAPIAdmin)