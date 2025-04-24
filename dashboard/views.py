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
    activities = Activity.objects.all()
    hotel_section = Hotel.objects.all()
    recreation_section = RecreationZone.objects.all()
    news_section = News.objects.all()

    ctx = {
        "activities": len(activities),
        "hotel_section": len(hotel_section),
        "recreation_section": len(recreation_section),
        "news_section": len(news_section),
    }

    return render(request, 'dashboard/index.html', ctx)


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
    hotel = get_object_or_404(Hotel, pk=pk)
    form = HotelForm(request.POST or None, request.FILES or None, instance=hotel)
    if form.is_valid():
        form.save()
        return redirect('hotel_list')

    ctx = {
        "form": form
    }
    return render(request, 'dashboard/hotel_section/form.html', ctx)


@login_required_decorator
def hotel_delete(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    hotel.delete()
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
    zone = get_object_or_404(RecreationZone, pk=pk)
    form = RecreationForm(request.POST or None, request.FILES or None, instance=zone)
    if form.is_valid():
        form.save()
        return redirect('recreation_list')

    ctx = {
        'form': form
    }
    return render(request, 'dashboard/recreation_section/form.html', ctx)


@login_required_decorator
def recreation_delete(request, pk):
    zone = get_object_or_404(RecreationZone, pk=pk)
    zone.delete()
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
