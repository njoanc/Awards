# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Location,tags, Image, Project


class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Location)
admin.site.register(tags)
admin.site.register(Image, ImageAdmin)
admin.site.register(Project, ProjectAdmin)