from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('language_selector.urls')),
    path('uz/', include('lager_app.urls')),
    path('ru/', include('lager_app_ru.urls')),
    path('en/', include('lager_app_en.urls')),
    path('admin/', include('dashboard.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
