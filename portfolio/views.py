from django.shortcuts import render
from.models import project

def index(request):
    projects = project.objects.all()
    return render(request,'portfolio/index.html',{'projects':projects})
