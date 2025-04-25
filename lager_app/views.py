from django.shortcuts import render, redirect
from .models import *


def home_page(request):
    photos = Photos.objects.all()
    ctx = {
        "photos": photos
    }
    return render(request, 'lager/index.html', ctx)


def activity_page(request):
    activities = Activity.objects.all()
    ctx = {
        "activities": activities
    }
    return render(request, 'lager/faoliyat.html', ctx)
