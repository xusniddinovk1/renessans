from django.urls import path
from django.conf.urls.i18n import set_language
from lager_app.views import activity_page, home_page, news_page, education_page, hotel_section_page, \
    recreation_zone_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('set-language/', set_language, name='set_language'),
    path('set-language/', set_language, name='set_language'),
    path('faoliyat/', activity_page, name='activity_page'),
    path('oquvbolim/', education_page, name='education_page'),
    path('mexmonxonalar/', hotel_section_page, name='hotel_section_page'),
    path('yangiliklar/', news_page, name='news_page'),
    path('istirohatzona/', recreation_zone_page, name='recreation_zone_page'),
]
