from django.urls import path
from  . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('about/', views.about, name = 'blog-about'),
    path('resume/', views.resume, name = 'blog-resume'),
    path('arduino/', views.arduino, name = 'blog-arduino'),
    path('webdev/', views.webdev, name = 'blog-webdev'),
    path('rambo/', views.rambo, name = 'blog-rambo'),
    path('triggerbot', views.triggerbot, name = 'blog-triggerbot'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)