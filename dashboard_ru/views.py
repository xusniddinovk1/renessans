from django.shortcuts import render, redirect, get_object_or_404
from dashboard_ru.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


def login_required_decorator(func):
    return login_required(func, login_url="ru-admin:login_page")


def login_page(request):
    if request.POST:
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("ru-admin:main_dashboard")
    return render(request, "dashboard_ru/login.html")


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("ru-admin:login_page")


@login_required_decorator
def account_view(request):
    return render(request, 'dashboard_ru/account.html')


@login_required_decorator
def settings_view(request):
    return render(request, 'dashboard_ru/settings.html')


@login_required_decorator
def billing_view(request):
    return render(request, 'dashboard_ru/billing.html')


@login_required_decorator
def main_dashboard(request):
    photos = Photos2.objects.all()
    educations = Education2.objects.all()
    activities = Activity2.objects.all()
    hotels = Hotel2.objects.all()
    rest_area = RecreationZone2.objects.all()
    news = News2.objects.all()

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
    return render(request, 'dashboard_ru/index.html', ctx)


@login_required_decorator
def about_us_list(request):
    text = AboutUs2.objects.all()

    ctx = {
        "text": text
    }
    return render(request, 'dashboard_ru/about_us/list.html', ctx)


@login_required_decorator
def about_us_create(request):
    form = AboutUsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ru-admin:about_us_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard_ru/about_us/form.html', ctx)


@login_required_decorator
def about_us_update(request, pk):
    text = get_object_or_404(AboutUs2, pk=pk)
    form = ActivityForm(request.POST or None, instance=text)
    if form.is_valid():
        form.save()
        return redirect('ru-admin:about_us_list')

    ctx = {
        'form': form
    }
    return render(request, 'dashboard_ru/about_us/form.html', ctx)


@login_required_decorator
def about_us_delete(request, pk):
    text = get_object_or_404(AboutUs2, pk=pk)
    text.delete()
    return redirect('ru-admin:about_us_list')


@login_required_decorator
def activity_list(request):
    activities = Activity2.objects.all()

    ctx = {
        "activities": activities
    }
    return render(request, 'dashboard_ru/activity_section/list.html', ctx)


@login_required_decorator
def activity_create(request):
    form = ActivityForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('ru-admin:activity_list')

    ctx = {
        'form': form,
    }
    return render(request, 'dashboard_ru/activity_section/form.html', ctx)


@login_required_decorator
def activity_update(request, pk):
    activity = get_object_or_404(Activity2, pk=pk)
    form = ActivityForm(request.POST or None, request.FILES or None, instance=activity)
    if form.is_valid():
        form.save()
        return redirect('ru-admin:activity_list')

    ctx = {
        'form': form
    }
    return render(request, 'dashboard_ru/activity_section/form.html', ctx)


@login_required_decorator
def activity_delete(request, pk):
    activity = get_object_or_404(Activity2, pk=pk)
    activity.delete()
    return redirect('ru-admin:activity_list')


@login_required_decorator
def hotel_list(request):
    hotels = Hotel2.objects.all()

    ctx = {
        'hotels': hotels
    }
    return render(request, 'dashboard_ru/hotel_section/list.html', ctx)


@login_required_decorator
def hotel_create(request):
    form = HotelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('ru-admin:hotel_list')

    ctx = {
        'form': form
    }
    return render(request, 'dashboard_ru/hotel_section/form.html', ctx)


@login_required_decorator
def hotel_update(request, pk):
    hotels = get_object_or_404(Hotel2, pk=pk)
    form = HotelForm(request.POST or None, request.FILES or None, instance=hotels)
    if form.is_valid():
        form.save()
        return redirect('ru-admin:hotel_list')

    ctx = {
        "form": form
    }
    return render(request, 'dashboard_ru/hotel_section/form.html', ctx)


@login_required_decorator
def hotel_delete(request, pk):
    hotels = get_object_or_404(Hotel2, pk=pk)
    hotels.delete()
    return redirect('ru-admin:hotel_list')


@login_required_decorator
def recreation_list(request):
    zones = RecreationZone2.objects.all()

    ctx = {
        'zones': zones
    }
    return render(request, 'dashboard_ru/recreation_section/list.html', ctx)


@login_required_decorator
def recreation_create(request):
    form = RecreationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('ru-admin:recreation_list')

    ctx = {
        'form': form,
    }
    return render(request, 'dashboard_ru/recreation_section/form.html', ctx)


@login_required_decorator
def recreation_update(request, pk):
    zones = get_object_or_404(RecreationZone2, pk=pk)
    form = RecreationForm(request.POST or None, request.FILES or None, instance=zones)
    if form.is_valid():
        form.save()
        return redirect('ru-admin:recreation_list')

    ctx = {
        'form': form
    }
    return render(request, 'dashboard_ru/recreation_section/form.html', ctx)


@login_required_decorator
def recreation_delete(request, pk):
    zones = get_object_or_404(RecreationZone2, pk=pk)
    zones.delete()
    return redirect('ru-admin:recreation_list')


@login_required_decorator
def news_list(request):
    news = News2.objects.order_by('-created_at')

    ctx = {
        "news": news
    }
    return render(request, 'dashboard_ru/news_section/list.html', ctx)


@login_required_decorator
def news_create(request):
    form = NewsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('ru-admin:news_list')

    ctx = {
        'form': form
    }
    return render(request, 'dashboard_ru/news_section/form.html', ctx)


@login_required_decorator
def news_update(request, pk):
    news = get_object_or_404(News2, pk=pk)
    form = NewsForm(request.POST or None, request.FILES or None, instance=news)
    if form.is_valid():
        form.save()
        return redirect('ru-admin:news_list')

    ctx = {
        "form": form
    }
    return render(request, 'dashboard_ru/news_section/form.html', ctx)


@login_required_decorator
def news_delete(request, pk):
    news = get_object_or_404(News2, pk=pk)
    news.delete()
    return redirect('ru-admin:news_list')


@login_required_decorator
def photo_list(request):
    photos = Photos2.objects.all()

    ctx = {
        "photos": photos
    }
    return render(request, 'dashboard_ru/photo_section/list.html', ctx)


@login_required_decorator
def photo_create(request):
    form = PhotoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('ru-admin:photo_list')

    ctx = {
        'form': form
    }
    return render(request, 'dashboard_ru/photo_section/form.html', ctx)


@login_required_decorator
def photo_update(request, pk):
    photos = get_object_or_404(Photos2, pk=pk)
    form = PhotoForm(request.POST or None, request.FILES or None, instance=photos)
    if form.is_valid():
        form.save()
        return redirect('ru-admin:photo_list')

    ctx = {
        "form": form
    }
    return render(request, 'dashboard_ru/photo_section/form.html', ctx)


@login_required_decorator
def photo_delete(request, pk):
    photo = get_object_or_404(Photos2, pk=pk)
    photo.delete()
    return redirect('ru-admin:photo_list')


@login_required_decorator
def education_list(request):
    educations = Education2.objects.all()

    ctx = {
        "educations": educations
    }
    return render(request, 'dashboard_ru/education_section/list.html', ctx)


@login_required_decorator
def education_create(request):
    form = EducationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('ru-admin:education_list')

    ctx = {
        'form': form
    }
    return render(request, 'dashboard_ru/education_section/form.html', ctx)


@login_required_decorator
def education_update(request, pk):
    education = get_object_or_404(Education2, pk=pk)
    form = EducationForm(request.POST or None, request.FILES or None, instance=education)
    if form.is_valid():
        form.save()
        return redirect('ru-admin:education_list')

    ctx = {
        "form": form
    }
    return render(request, 'dashboard_ru/education_section/form.html', ctx)


@login_required_decorator
def education_delete(request, pk):
    education = get_object_or_404(Education2, pk=pk)
    education.delete()
    return redirect('ru-admin:education_list')
