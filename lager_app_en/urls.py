from django.urls import path
from lager_app_en.views import contact, about, photos
from lager_app_en.views import activity_page, home_page, news_page, education_page, hotel_section_page, \
    recreation_zone_page, education_detail

urlpatterns = [
    path('', home_page, name='home_page'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('photos/', photos, name='photos'),
    path('activities/', activity_page, name='activity_page'),
    path('educations/', education_page, name='education_page'),
    path('educations/<int:id>/', education_detail, name='education_detail'),
    path('hotels/', hotel_section_page, name='hotel_section_page'),
    path('news/', news_page, name='news_page'),
    path('recreation-zones/', recreation_zone_page, name='recreation_zone_page'),
]
