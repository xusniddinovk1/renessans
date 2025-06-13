from django.urls import path
from lager_app.views import activity_page, home_page, news_page, education_page, hotel_section_page, \
    recreation_zone_page, education_detail

urlpatterns = [
    path('', home_page, name='home_page'),
    path('faoliyat/', activity_page, name='activity_page'),
    path('oquvbolim/', education_page, name='education_page'),
    path('oquvbolim/<int:id>/', education_detail, name='education_detail'),
    path('mexmonxonalar/', hotel_section_page, name='hotel_section_page'),
    path('yangiliklar/', news_page, name='news_page'),
    path('istirohatzona/', recreation_zone_page, name='recreation_zone_page'),
]
