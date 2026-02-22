from django.db import models
class AboutMe(models.Model):
    full_name = models.CharField(max_length=255, blank=True)
    birthday = models.DateField(null=True, blank=True)
    birthplace = models.CharField(max_length=255, blank=True)
    bio = models.TextField()
    github = models.URLField()
    photo = models.ImageField(upload_to='about/')
    school = models.CharField(max_length=255)
    hobbies = models.TextField(default="Информация отсутсвует")
    relatives = models.TextField(default="Информация отсутсвует")
    friends = models.TextField(default="Информация отсутсвует")
    photo_friends = models.ImageField(upload_to='about/', null=True, blank=True)
    zodiak = models.TextField(default="Информация отсутсвует")
    wishes = models.TextField(default="Информация отсутсвует")
class Achievement(models.Model):
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='achievements/covers/')
    description = models.TextField()
class AchievementImage(models.Model):
    achievement = models.ForeignKey(Achievement,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='achievements/images/')
class School(models.Model):
    description = models.TextField()
    photos = models.ImageField(upload_to='school/', null=True, blank=True)

class SchoolPhoto(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='photo_gallery')
    photo = models.ImageField(upload_to='school/', null=True, blank=True)
    video = models.FileField(upload_to='school/videos/', null=True, blank=True, help_text='Поддерживает .mp4, .webm, .ogg')
