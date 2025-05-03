from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


def login_required_decorator(func):
    return login_required(func, login_url="login_page")


def login_page(request):
    if request.POST:
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main_dashboard")
    return render(request, "dashboard/login.html")


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


@login_required_decorator
def account_view(request):
    return render(request, 'dashboard/account.html')


@login_required_decorator
def settings_view(request):
    return render(request, 'dashboard/settings.html')


@login_required_decorator
def billing_view(request):
    return render(request, 'dashboard/billing.html')


@login_required_decorator
def main_dashboard(request):
    about_us = AboutUs.objects.all()
    photos = Photos.objects.all()
    educations = Education.objects.all()
    activities = Activity.objects.all()
    hotels = Hotel.objects.all()
    rest_area = RecreationZone.objects.all()
    news = News.objects.all()

    ctx = {
        "counts": {
            "photos": len(photos),
            "educations": len(educations),
            "activities": len(activities),
            "hotels": len(hotels),
            "rest_area": len(rest_area),
            "news": len(news),
        }
    }
    return render(request, 'dashboard/index.html', ctx)


@login_required_decorator
def about_us_list(request):
    text = AboutUs.objects.all()

    ctx = {
        "text": text
    }
    return render(request, 'dashboard/about_us/list.html', ctx)


@login_required_decorator
def about_us_create(request):
    form = AboutUsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('about_us_list')
    ctx = {
        "form": form
    }
    return render(request, 'lager/about_us/form.html', ctx)


@login_required_decorator
def about_us_update(request, pk):
    text = get_object_or_404(AboutUs, pk=pk)
    form = ActivityForm(request.POST or None, instance=text)
    if form.is_valid():
        form.save()
        return redirect('about_us_list')

    ctx = {
        'form': form
    }
    return render(request, 'dashboard/about_us/form.html', ctx)


@login_required_decorator
def about_us_delete(request, pk):
    text = get_object_or_404(AboutUs, pk=pk)
    text.delete()
    return redirect('about_us_list')


@login_required_decorator
def activity_list(request):
    activities = Activity.objects.all()

    ctx = {
        "activities": activities
    }
    return render(request, 'dashboard/activity_section/list.html', ctx)


@login_required_decorator
def activity_create(request):
    form = ActivityForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('activity_list')

    ctx = {
        'form': form,
    }
    return render(request, 'dashboard/activity_section/form.html', ctx)


@login_required_decorator
def activity_update(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    form = ActivityForm(request.POST or None, request.FILES or None, instance=activity)
    if form.is_valid():
        form.save()
        return redirect('activity_list')

    ctx = {
        'form': form
    }
    return render(request, 'dashboard/activity_section/form.html', ctx)


@login_required_decorator
def activity_delete(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    activity.delete()
    return redirect('activity_list')


@login_required_decorator
def hotel_list(request):
    hotels = Hotel.objects.all()

    ctx = {
        'hotels': hotels
    }
    return render(request, 'dashboard/hotel_section/list.html', ctx)


@login_required_decorator
def hotel_create(request):
    form = HotelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('hotel_list')

    ctx = {
        'form': form
    }
    return render(request, 'dashboard/hotel_section/form.html', ctx)


@login_required_decorator
def hotel_update(request, pk):
    hotels = get_object_or_404(Hotel, pk=pk)
    form = HotelForm(request.POST or None, request.FILES or None, instance=hotels)
    if form.is_valid():
        form.save()
        return redirect('hotel_list')

    ctx = {
        "form": form
    }
    return render(request, 'dashboard/hotel_section/form.html', ctx)


@login_required_decorator
def hotel_delete(request, pk):
    hotels = get_object_or_404(Hotel, pk=pk)
    hotels.delete()
    return redirect('hotel_list')


@login_required_decorator
def recreation_list(request):
    zones = RecreationZone.objects.all()

    ctx = {
        'zones': zones
    }
    return render(request, 'dashboard/recreation_section/list.html', ctx)


@login_required_decorator
def recreation_create(request):
    form = RecreationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('recreation_list')

    ctx = {
        'form': form,
    }
    return render(request, 'dashboard/recreation_section/form.html', ctx)


@login_required_decorator
def recreation_update(request, pk):
    zones = get_object_or_404(RecreationZone, pk=pk)
    form = RecreationForm(request.POST or None, request.FILES or None, instance=zones)
    if form.is_valid():
        form.save()
        return redirect('recreation_list')

    ctx = {
        'form': form
    }
    return render(request, 'dashboard/recreation_section/form.html', ctx)


@login_required_decorator
def recreation_delete(request, pk):
    zones = get_object_or_404(RecreationZone, pk=pk)
    zones.delete()
    return redirect('recreation_list')


@login_required_decorator
def news_list(request):
    news = News.objects.order_by('-created_at')

    ctx = {
        "news": news
    }
    return render(request, 'dashboard/news_section/list.html', ctx)


@login_required_decorator
def news_create(request):
    form = NewsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('news_list')

    ctx = {
        'form': form
    }
    return render(request, 'dashboard/news_section/form.html', ctx)


@login_required_decorator
def news_update(request, pk):
    news = get_object_or_404(News, pk=pk)
    form = NewsForm(request.POST or None, request.FILES or None, instance=news)
    if form.is_valid():
        form.save()
        return redirect('news_list')

    ctx = {
        "form": form
    }
    return render(request, 'dashboard/news_section/form.html', ctx)


@login_required_decorator
def news_delete(request, pk):
    news = get_object_or_404(News, pk=pk)
    news.delete()
    return redirect('news_list')


@login_required_decorator
def photo_list(request):
    photos = Photos.objects.all()

    ctx = {
        "photos": photos
    }
    return render(request, 'dashboard/photo_section/list.html', ctx)


@login_required_decorator
def photo_create(request):
    form = PhotoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('photo_list')

    ctx = {
        'form': form
    }
    return render(request, 'dashboard/photo_section/form.html', ctx)


@login_required_decorator
def photo_update(request, pk):
    photos = get_object_or_404(Photos, pk=pk)
    form = PhotoForm(request.POST or None, request.FILES or None, instance=photos)
    if form.is_valid():
        form.save()
        return redirect('photo_list')

    ctx = {
        "form": form
    }
    return render(request, 'dashboard/photo_section/form.html', ctx)


@login_required_decorator
def photo_delete(request, pk):
    photo = get_object_or_404(Photos, pk=pk)
    photo.delete()
    return redirect('photo_list')


@login_required_decorator
def education_list(request):
    educations = Education.objects.all()

    ctx = {
        "educations": educations
    }
    return render(request, 'dashboard/education_section/list.html', ctx)


@login_required_decorator
def education_create(request):
    form = EducationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('education_list')

    ctx = {
        'form': form
    }
    return render(request, 'dashboard/education_section/form.html', ctx)


@login_required_decorator
def education_update(request, pk):
    education = get_object_or_404(Education, pk=pk)
    form = EducationForm(request.POST or None, request.FILES or None, instance=education)
    if form.is_valid():
        form.save()
        return redirect('education_list')

    ctx = {
        "form": form
    }
    return render(request, 'dashboard/education_section/form.html', ctx)


@login_required_decorator
def education_delete(request, pk):
    education = get_object_or_404(Education, pk=pk)
    education.delete()
    return redirect('education_list')
