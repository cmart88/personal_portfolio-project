from django.shortcuts import render
from .models import Forum
# Create your views here.
def forum(request):
    return render(request,'forum/forum.html')
