from django.shortcuts import render, get_object_or_404
from lager_app_ru.models import *


def home_page(request):
    text = AboutUs2.objects.first()
    photos = Photos2.objects.all()
    ctx = {
        "text": text,
        "photos": photos,
    }
    return render(request, 'lager_ru/index.html', ctx)


def activity_page(request):
    activities = Activity2.objects.all()
    ctx = {
        "activities": activities
    }
    return render(request, 'lager_ru/activity.html', ctx)


def news_page(request):
    news_item = News2.objects.all()
    ctx = {
        "news_item": news_item
    }
    return render(request, 'lager_ru/news_section.html', ctx)


def education_page(request):
    educations = Education2.objects.all()
    ctx = {
        "educations": educations
    }
    return render(request, 'lager_ru/education.html', ctx)


def education_detail(request, id):
    education = get_object_or_404(Education2, pk=id)
    ctx = {
        'education': education
    }
    return render(request, 'lager_ru/education_detail.html', ctx)


def recreation_zone_page(request):
    rest_areas = RecreationZone2.objects.all()
    ctx = {
        "rest_areas": rest_areas
    }
    return render(request, 'lager_ru/recreation_zone.html', ctx)


def hotel_section_page(request):
    hotels = Hotel2.objects.all()
    ctx = {
        "hotels": hotels
    }
    return render(request, 'lager_ru/hotel_section.html', ctx)


def contact_page1(request):
    if request.method == 'POST':
        pass
    return render(request, 'lager_ru/index1.html')


def about_page1(request):
    context = AboutUs2.objects.all()
    ctx = {
        'context': context
    }
    return render(request, 'lager_ru/about.html', ctx)


def photos_page1(request):
    photos = Photos2.objects.all()
    ctx = {
        'photos': photos
    }
    return render(request, 'lager_ru/photos.html', ctx)
