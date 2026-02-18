from django.shortcuts import render, get_object_or_404
from .models import *
def about(request):
    return render(request,'about.html',{'about':AboutMe.objects.first()})
def achievements(request):
    return render(request,'achievements.html',{'achievements':Achievement.objects.all()})
def achievement_detail(request,pk):
    return render(request,'achievement_detail.html',{'achievement':get_object_or_404(Achievement,pk=pk)})
def school(request):
    return render(request,'school.html',{'school':School.objects.first()})
