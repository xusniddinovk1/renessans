from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('', include('language_selector.urls')),
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
