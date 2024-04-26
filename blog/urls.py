from django.urls import path
from  . import views
urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('about/', views.about, name = 'blog-about'),
    path('resume/', views.resume, name = 'blog-resume'),
    path('contact/', views.contact, name = 'blog-contact'),
    path('arduino/', views.arduino, name = 'blog-arduino'),
    path('webdev/', views.webdev, name = 'blog-webdev'),
    path('send_email/', views.send_email, name = 'send_email'),
    path('rambo/', views.rambo, name = 'blog-rambo'),
]