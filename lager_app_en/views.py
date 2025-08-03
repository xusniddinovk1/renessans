from django.shortcuts import render, get_object_or_404
from lager_app_en.models import *


def home_page(request):
    text = AboutUs1.objects.first()
    photos = Photos1.objects.all()
    ctx = {
        "text": text,
        "photos": photos,
    }
    return render(request, 'lager_en/index.html', ctx)


def activity_page(request):
    activities = Activity1.objects.all()
    ctx = {
        "activities": activities
    }
    return render(request, 'lager_en/activity.html', ctx)


def news_page(request):
    news_item = News1.objects.all()
    ctx = {
        "news_item": news_item
    }
    return render(request, 'lager_en/news_section.html', ctx)


def education_page(request):
    educations = Education1.objects.all()
    ctx = {
        "educations": educations
    }
    return render(request, 'lager_en/education.html', ctx)


def education_detail(request, id):
    education = get_object_or_404(Education1, pk=id)
    ctx = {
        'education': education
    }
    return render(request, 'lager_en/education_detail.html', ctx)


def recreation_zone_page(request):
    rest_areas = RecreationZone1.objects.all()
    ctx = {
        "rest_areas": rest_areas
    }
    return render(request, 'lager_en/recreation_zone.html', ctx)


def hotel_section_page(request):
    hotels = Hotel1.objects.all()
    ctx = {
        "hotels": hotels
    }
    return render(request, 'lager_en/hotel_section.html', ctx)

def contact(request):
    if request.method == 'POST':
        pass
    return render(request, 'lager_en/index1.html')

def about(request):
    context = AboutUs1.objects.all()
    ctx = {
        'context': context
    }
    return render(request, 'lager_en/about.html', ctx)


def photos(request):
    photos = Photos1.objects.all()
    ctx = {
        'photos': photos
    }
    return render(request, 'lager_en/photos.html', ctx)