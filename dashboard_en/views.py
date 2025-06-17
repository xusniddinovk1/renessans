from django.shortcuts import get_object_or_404
from dashboard_en.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def login_required_decorator(func):
    return login_required(func, login_url='en-admin:login_page')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("en-admin:main_dashboard")
        else:
            context = {'error': "Username yoki parol noto'g'ri"}
            return render(request, "dashboard_en/login.html", context)
    return render(request, "dashboard_en/login.html")


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("en-admin:login_page")


@login_required_decorator
def account_view(request):
    return render(request, 'dashboard_en/account.html')


@login_required_decorator
def settings_view(request):
    return render(request, 'dashboard_en/settings.html')


@login_required_decorator
def billing_view(request):
    return render(request, 'dashboard_en/billing.html')


@login_required_decorator
def main_dashboard(request):
    stats = [
        {
            "label": "Photos",
            "count": Photos1.objects.count(),
            "icon": "fa-user",
            "color": "c2"
        },
        {
            "label": "O'quv bo'limi",
            "count": Education1.objects.count(),
            "icon": "fa-user",
            "color": "c2"
        },
        {
            "label": "Faoliyatlar",
            "count": Activity1.objects.count(),
            "icon": "fa-list-alt",
            "color": "c1"
        },
        {
            "label": "Mehmonxona",
            "count": Hotel1.objects.count(),
            "icon": "fa-list-alt",
            "color": "c2"
        },
        {
            "label": "Istirohat Zona",
            "count": RecreationZone1.objects.count(),
            "icon": "fa-list-alt",
            "color": "c1"
        },
        {
            "label": "Yangiliklar",
            "count": News1.objects.count(),
            "icon": "fa-user",
            "color": "c2"
        },
    ]

    # Chart uchun counts dictionary
    counts = {
        "photos": stats[0]["count"],
        "educations": stats[1]["count"],
        "activities": stats[2]["count"],
        "hotels": stats[3]["count"],
        "rest_area": stats[4]["count"],
        "news": stats[5]["count"],
    }

    return render(request, 'dashboard_en/index.html', {
        "stats": stats,
        "counts": counts
    })


@login_required_decorator
def about_us_list(request):
    text = AboutUs1.objects.all()

    ctx = {
        "text": text
    }
    return render(request, 'dashboard_en/about_us/list.html', ctx)


@login_required_decorator
def about_us_create(request):
    form = AboutUsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('en-admin:about_us_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard_en/about_us/form.html', ctx)


@login_required_decorator
def about_us_update(request, pk):
    text = get_object_or_404(AboutUs1, pk=pk)
    form = ActivityForm(request.POST or None, instance=text)
    if form.is_valid():
        form.save()
        return redirect('en-admin:about_us_list')

    ctx = {
        'form': form
    }
    return render(request, 'dashboard_en/about_us/form.html', ctx)


@login_required_decorator
def about_us_delete(request, pk):
    text = get_object_or_404(AboutUs1, pk=pk)
    text.delete()
    return redirect('en-admin:about_us_list')


@login_required_decorator
def activity_list(request):
    activities = Activity1.objects.all()

    ctx = {
        "activities": activities
    }
    return render(request, 'dashboard_en/activity_section/list.html', ctx)


@login_required_decorator
def activity_create(request):
    form = ActivityForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('en-admin:activity_list')

    ctx = {
        'form': form,
    }
    return render(request, 'dashboard_en/activity_section/form.html', ctx)


@login_required_decorator
def activity_update(request, pk):
    activity = get_object_or_404(Activity1, pk=pk)
    form = ActivityForm(request.POST or None, request.FILES or None, instance=activity)
    if form.is_valid():
        form.save()
        return redirect('en-admin:activity_list')

    ctx = {
        'form': form
    }
    return render(request, 'dashboard_en/activity_section/form.html', ctx)


@login_required_decorator
def activity_delete(request, pk):
    activity = get_object_or_404(Activity1, pk=pk)
    activity.delete()
    return redirect('en-admin:activity_list')


@login_required_decorator
def hotel_list(request):
    hotels = Hotel1.objects.all()

    ctx = {
        'hotels': hotels
    }
    return render(request, 'dashboard_en/hotel_section/list.html', ctx)


@login_required_decorator
def hotel_create(request):
    form = HotelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('en-admin:hotel_list')

    ctx = {
        'form': form
    }
    return render(request, 'dashboard_en/hotel_section/form.html', ctx)


@login_required_decorator
def hotel_update(request, pk):
    hotels = get_object_or_404(Hotel1, pk=pk)
    form = HotelForm(request.POST or None, request.FILES or None, instance=hotels)
    if form.is_valid():
        form.save()
        return redirect('en-admin:hotel_list')

    ctx = {
        "form": form
    }
    return render(request, 'dashboard_en/hotel_section/form.html', ctx)


@login_required_decorator
def hotel_delete(request, pk):
    hotels = get_object_or_404(Hotel1, pk=pk)
    hotels.delete()
    return redirect('en-admin:hotel_list')


@login_required_decorator
def recreation_list(request):
    zones = RecreationZone1.objects.all()

    ctx = {
        'zones': zones
    }
    return render(request, 'dashboard_en/recreation_section/list.html', ctx)


@login_required_decorator
def recreation_create(request):
    form = RecreationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('en-admin:recreation_list')

    ctx = {
        'form': form,
    }
    return render(request, 'dashboard_en/recreation_section/form.html', ctx)


@login_required_decorator
def recreation_update(request, pk):
    zones = get_object_or_404(RecreationZone1, pk=pk)
    form = RecreationForm(request.POST or None, request.FILES or None, instance=zones)
    if form.is_valid():
        form.save()
        return redirect('en-admin:recreation_list')

    ctx = {
        'form': form
    }
    return render(request, 'dashboard_en/recreation_section/form.html', ctx)


@login_required_decorator
def recreation_delete(request, pk):
    zones = get_object_or_404(RecreationZone1, pk=pk)
    zones.delete()
    return redirect('en-admin:recreation_list')


@login_required_decorator
def news_list(request):
    news = News1.objects.order_by('-created_at')

    ctx = {
        "news": news
    }
    return render(request, 'dashboard_en/news_section/list.html', ctx)


@login_required_decorator
def news_create(request):
    form = NewsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('en-admin:news_list')

    ctx = {
        'form': form
    }
    return render(request, 'dashboard_en/news_section/form.html', ctx)


@login_required_decorator
def news_update(request, pk):
    news = get_object_or_404(News1, pk=pk)
    form = NewsForm(request.POST or None, request.FILES or None, instance=news)
    if form.is_valid():
        form.save()
        return redirect('en-admin:ews_list')

    ctx = {
        "form": form
    }
    return render(request, 'dashboard_en/news_section/form.html', ctx)


@login_required_decorator
def news_delete(request, pk):
    news = get_object_or_404(News1, pk=pk)
    news.delete()
    return redirect('en-admin:news_list')


@login_required_decorator
def photo_list(request):
    photos = Photos1.objects.all()

    ctx = {
        "photos": photos
    }
    return render(request, 'dashboard_en/photo_section/list.html', ctx)


@login_required_decorator
def photo_create(request):
    form = PhotoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('en-admin:photo_list')

    ctx = {
        'form': form
    }
    return render(request, 'dashboard_en/photo_section/form.html', ctx)


@login_required_decorator
def photo_update(request, pk):
    photos = get_object_or_404(Photos1, pk=pk)
    form = PhotoForm(request.POST or None, request.FILES or None, instance=photos)
    if form.is_valid():
        form.save()
        return redirect('en-admin:photo_list')

    ctx = {
        "form": form
    }
    return render(request, 'dashboard_en/photo_section/form.html', ctx)


@login_required_decorator
def photo_delete(request, pk):
    photo = get_object_or_404(Photos1, pk=pk)
    photo.delete()
    return redirect('en-admin:photo_list')


@login_required_decorator
def education_list(request):
    educations = Education1.objects.all()

    ctx = {
        "educations": educations
    }
    return render(request, 'dashboard_en/education_section/list.html', ctx)


@login_required_decorator
def education_create(request):
    form = EducationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('en-admin:education_list')

    ctx = {
        'form': form
    }
    return render(request, 'dashboard_en/education_section/form.html', ctx)


@login_required_decorator
def education_update(request, pk):
    education = get_object_or_404(Education1, pk=pk)
    form = EducationForm(request.POST or None, request.FILES or None, instance=education)
    if form.is_valid():
        form.save()
        return redirect('en-admin:education_list')

    ctx = {
        "form": form
    }
    return render(request, 'dashboard_en/education_section/form.html', ctx)


@login_required_decorator
def education_delete(request, pk):
    education = get_object_or_404(Education1, pk=pk)
    education.delete()
    return redirect('en-admin:education_list')
