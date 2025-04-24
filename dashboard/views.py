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
            return redirect("dashboard")
    return render(request, "dashboard/login.html")


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


@login_required_decorator
def dashboard(request):
    stats = {
        'activity_count': Activity.objects.count(),
        'hotel_count': Hotel.objects.count(),
        'recreation_count': RecreationZone.objects.count(),
        'news_count': News.objects.count(),
        'latest_activities': Activity.objects.order_by('-id')[:5],
        'latest_hotels': Hotel.objects.order_by('-id')[:5],
        'latest_news': News.objects.order_by('-created_at')[:5],
    }
    return render(request, 'dashboard/dashboard.html', {
        'stats': stats,
        'user': request.user,
    })


@login_required_decorator
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


@login_required_decorator
def activity_list(request):
    activities = Activity.objects.all()
    return render(request, 'dashboard/activities/list.html', {'activities': activities})


@login_required_decorator
def activity_create(request):
    form = ActivityForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('activity_list')
    return render(request, 'dashboard/activities/form.html', {'form': form, 'title': 'Yangi faoliyat qo‘shish'})


@login_required_decorator
def activity_update(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    form = ActivityForm(request.POST or None, request.FILES or None, instance=activity)
    if form.is_valid():
        form.save()
        return redirect('activity_list')
    return render(request, 'dashboard/activities/form.html', {'form': form, 'title': 'Faoliyatni tahrirlash'})


@login_required_decorator
def activity_delete(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == 'POST':
        activity.delete()
        return redirect('activity_list')
    return render(request, 'dashboard/activities/delete_confirm.html', {'activity': activity})


@login_required_decorator
def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'dashboard/hotels/list.html', {'hotels': hotels})


@login_required_decorator
def hotel_create(request):
    form = HotelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('hotel_list')
    return render(request, 'dashboard/hotels/form.html', {'form': form, 'title': 'Yangi mehmonxona qo‘shish'})


@login_required_decorator
def hotel_update(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    form = HotelForm(request.POST or None, request.FILES or None, instance=hotel)
    if form.is_valid():
        form.save()
        return redirect('hotel_list')
    return render(request, 'dashboard/hotels/form.html', {'form': form, 'title': 'Mehmonxonani tahrirlash'})


@login_required_decorator
def hotel_delete(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    if request.method == 'POST':
        hotel.delete()
        return redirect('hotel_list')
    return render(request, 'dashboard/hotels/delete_confirm.html', {'hotel': hotel})


@login_required_decorator
def recreation_list(request):
    zones = RecreationZone.objects.all()
    return render(request, 'dashboard/recreation/list.html', {'zones': zones})


@login_required_decorator
def recreation_create(request):
    form = RecreationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('recreation_list')
    return render(request, 'dashboard/recreation/form.html', {'form': form, 'title': 'Yangi istirohat zonasi qo‘shish'})


@login_required_decorator
def recreation_update(request, pk):
    zone = get_object_or_404(RecreationZone, pk=pk)
    form = RecreationForm(request.POST or None, request.FILES or None, instance=zone)
    if form.is_valid():
        form.save()
        return redirect('recreation_list')
    return render(request, 'dashboard/recreation/form.html', {'form': form, 'title': 'Istirohat zonasini tahrirlash'})


@login_required_decorator
def recreation_delete(request, pk):
    zone = get_object_or_404(RecreationZone, pk=pk)
    if request.method == 'POST':
        zone.delete()
        return redirect('recreation_list')
    return render(request, 'dashboard/recreation/delete_confirm.html', {'zone': zone})


@login_required_decorator
def news_list(request):
    news_list = News.objects.order_by('-created_at')
    return render(request, 'dashboard/news/list.html', {'news_list': news_list})


@login_required_decorator
def news_create(request):
    form = NewsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('news_list')
    return render(request, 'dashboard/news/form.html', {'form': form, 'title': 'Yangi yangilik qo‘shish'})


@login_required_decorator
def news_update(request, pk):
    news = get_object_or_404(News, pk=pk)
    form = NewsForm(request.POST or None, request.FILES or None, instance=news)
    if form.is_valid():
        form.save()
        return redirect('news_list')
    return render(request, 'dashboard/news/form.html', {'form': form, 'title': 'Yangilikni tahrirlash'})


@login_required_decorator
def news_delete(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        news.delete()
        return redirect('news_list')
    return render(request, 'dashboard/news/delete_confirm.html', {'news': news})
