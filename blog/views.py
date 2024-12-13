from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Post
# Create your views here.

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'Max Sorin- About Me'} )

def resume(request):
    return render(request, 'blog/resume.html', {'title' : 'Hire me!'} )

def arduino(request):
    return render(request, 'blog/arduino.html', {'title' : 'Digital Clutch Slipper'} )
def webdev(request):
    return render(request, 'blog/webdev.html', {'title' : 'Creation of This Site'} )

def rambo(request):
    return render(request, 'blog/rambo.html', {'title' : 'Rambo\'s Fountain'})

def triggerbot(request):
    return render(request, 'blog/triggerbot.html', {'title' : 'Overwatch 2 Trigger Bot'})