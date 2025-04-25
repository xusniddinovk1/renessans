from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from lager_app.views import activity_page, home_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('faoliyat/', activity_page, name='activity_page'),
    path('oquvbolim/', activity_page, name='education_page'),
    path('mexmonxonalar/', activity_page, name='hotel_section_page'),
    path('yangiliklar/', activity_page, name='news_page'),
    path('istirohatzona/', activity_page, name='recreation_zone_page'),
]
