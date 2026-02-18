from django.contrib import admin
from .models import *
class AchievementImageInline(admin.TabularInline):
    model = AchievementImage
@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    inlines = [AchievementImageInline]
admin.site.register(AboutMe)
admin.site.register(School)
