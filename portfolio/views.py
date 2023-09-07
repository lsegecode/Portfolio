from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all().order_by('title')
    return render(request, 'home.html', {'projects' : projects})
    

def git(request):

    return render(request, 'git.html')