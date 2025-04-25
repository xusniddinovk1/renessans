from django.shortcuts import render, redirect
from .models import *


def activity_page(request):
    activities = Activity.objects.all()
    ctx = {
        "activities": activities
    }
    return render(request, 'lager/faoliyat.html', ctx)





