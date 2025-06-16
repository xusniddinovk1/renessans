from django.urls import path
from lager_app.views import activity_page, home_page, news_page, education_page, hotel_section_page, \
    recreation_zone_page, education_detail

app_name = 'lager_app'


urlpatterns = [
    path('', home_page, name='asosiy_sahifa'),
    path('faoliyat/', activity_page, name='faoliyat'),
    path('oquvbolim/', education_page, name='oquvbolim'),
    path('oquvbolim/<int:id>/', education_detail, name='oquvbolim_sahifa'),
    path('mexmonxonalar/', hotel_section_page, name='mexmonxonalar'),
    path('yangiliklar/', news_page, name='yangiliklar'),
    path('istirohatzona/', recreation_zone_page, name='istirohat_zona'),
]
