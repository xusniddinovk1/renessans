from django.urls import path
from lager_app.views import activity_page, home_page, news_page, education_page, hotel_section_page, \
    recreation_zone_page, education_detail

urlpatterns = [
    path('', home_page, name='home_page'),
    path('en/faoliyat/', activity_page, name='activity_page'),
    path('en/oquvbolim/', education_page, name='education_page'),
    path('en/oquvbolim/<int:id>/', education_detail, name='education_detail'),
    path('en/mexmonxonalar/', hotel_section_page, name='hotel_section_page'),
    path('en/yangiliklar/', news_page, name='news_page'),
    path('en/istirohatzona/', recreation_zone_page, name='recreation_zone_page'),
]
