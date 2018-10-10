# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Location,tags, Image, Project, Profile


class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

admin.site.register(Location)
admin.site.register(tags)
admin.site.register(Image, ImageAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Profile, ProfileAdmin)