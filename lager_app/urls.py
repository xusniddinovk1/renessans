from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from lager_app.views import activity_page

urlpatterns = [
    path('faoliyat/', activity_page, name='activity_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
