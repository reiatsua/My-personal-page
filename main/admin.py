from django.contrib import admin
from .models import *

class AchievementImageInline(admin.TabularInline):
    model = AchievementImage

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    inlines = [AchievementImageInline]

class SchoolPhotoInline(admin.TabularInline):
    model = SchoolPhoto
    extra = 1

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    inlines = [SchoolPhotoInline]

admin.site.register(AboutMe)
