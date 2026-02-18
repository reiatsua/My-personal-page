from django.db import models
class AboutMe(models.Model):
    bio = models.TextField()
    github = models.URLField()
    photo = models.ImageField(upload_to='about/')
    school = models.CharField(max_length=255)
class Achievement(models.Model):
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='achievements/covers/')
    description = models.TextField()
class AchievementImage(models.Model):
    achievement = models.ForeignKey(Achievement,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='achievements/images/')
class School(models.Model):
    description = models.TextField()
    photos = models.ImageField(upload_to='school/')
