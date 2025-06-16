from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.urls import path, include

def redirect_to_default_admin(request):
    # Bu yerda default tilni uz deb qo'ydim, xohlasangiz 'en' yoki 'ru' ham bo'lishi mumkin
    return redirect('/uz/admin/')

urlpatterns = [
    path('', include('language_selector.urls')),
    path('admin/', redirect_to_default_admin),  # /admin/ kiritilsa avtomatik uz/admin/ ga yo'naltiradi
    path('uz/', include('lager_app.urls')),
    path('ru/', include('lager_app_ru.urls')),
    path('en/', include('lager_app_en.urls')),
    path('uz/admin/', include('dashboard.urls')),
    path('ru/admin/', include('dashboard_ru.urls')),
    path('en/admin/', include('dashboard_en.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
