from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

posts = [
    {
        'Author' : 'Max',
        'Title' : 'Test 1',
        'Content' : 'First Test Now',
        'Date' : 'Jan 1 2024'
    },
    {
        'Author' : 'Ange',
        'Title' : 'Test 2',
        'Content' : 'Second Test Now',
        'Date' : 'Jan 11 2024'
    }
    
]
def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'Max Sorin- About Me'} )

def resume(request):
    return render(request, 'blog/resume.html', {'title' : 'Hire me!'} )

def contact(request):
    return render(request, 'blog/contact.html', {'title' : 'Contact Information'} )

def arduino(request):
    return render(request, 'blog/arduino.html', {'title' : 'Digitcal Clutch Slipper'} )
def webdev(request):
    return render(request, 'blog/webdev.html', {'title' : 'Creation of This Site'} )

def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Customize the email content as needed
        email_content = f"From: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"

        # Replace with your email configuration
        send_mail(
            'Subject of the email',
            email_content,
            email,  # Sender's email
            ['maxsorinengineering@gmail.com'],  # List of recipient(s)
            fail_silently=False,
        )

        # Redirect after sending the email
       # return HttpResponseRedirect(reverse('http://localhost:8000/about/'))  # Replace with your success page URL
   # else:
        return render(request, 'blog/about.html')  # Replace 'contact.html' with your actual template