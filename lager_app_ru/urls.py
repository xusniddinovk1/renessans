from django.urls import path
from lager_app_ru.views import activity_page, home_page, news_page, education_page, hotel_section_page, \
    recreation_zone_page, education_detail

urlpatterns = [
    path('', home_page, name='основной'),
    path('деятельность/', activity_page, name='деятельность'),
    path('академический-отдел/', education_page, name='академический_отдел'),
    path('академический-отдел/<int:id>/', education_detail, name='академический_отдел_1'),
    path('гостиницы/', hotel_section_page, name='гостиницы'),
    path('новости/', news_page, name='новости'),
    path('зона-отдыха/', recreation_zone_page, name='зона_отдыха'),
]
