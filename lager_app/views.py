from django.shortcuts import render, get_object_or_404
from lager_app.models import *


def home_page(request):
    text = AboutUs.objects.first()
    photos = Photos.objects.all()
    ctx = {
        "text": text,
        "photos": photos,
    }
    return render(request, 'lager/index.html', ctx)


def activity_page(request):
    activities = Activity.objects.all()
    ctx = {
        "activities": activities
    }
    return render(request, 'lager/activity.html', ctx)


def news_page(request):
    news_item = News.objects.all()
    ctx = {
        "news_item": news_item
    }
    return render(request, 'lager/news_section.html', ctx)


def education_page(request):
    educations = Education.objects.all()
    ctx = {
        "educations": educations
    }
    return render(request, 'lager/education.html', ctx)


def education_detail(request, id):
    education = get_object_or_404(Education, pk=id)
    ctx = {
        'education': education
    }
    return render(request, 'lager/education_detail.html', ctx)


def recreation_zone_page(request):
    rest_areas = RecreationZone.objects.all()
    ctx = {
        "rest_areas": rest_areas
    }
    return render(request, 'lager/recreation_zone.html', ctx)


def hotel_section_page(request):
    hotels = Hotel.objects.all()
    ctx = {
        "hotels": hotels
    }
    return render(request, 'lager/hotel_section.html', ctx)
