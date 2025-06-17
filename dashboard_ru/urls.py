from django.urls import path
from dashboard_ru.views import *


app_name = 'dashboard_ru'


urlpatterns = [
    path('login/', login_page, name="login_page"),
    path('logout/', logout_page, name="logout_page"),

    path('account/', account_view, name='account_page'),
    path('settings/', settings_view, name='settings_page'),
    path('billing/', billing_view, name='billing_page'),

    path('', main_dashboard, name='main_dashboard'),

    path('о-нас/', about_us_list, name='about_us_list'),
    path('о-нас/новый/', about_us_create, name='about_us_create'),
    path('о-нас/<int:pk>/редактировать /', about_us_update, name='about_us_update'),
    path('о-нас/<int:pk>/удалить/', about_us_delete, name='about_us_delete'),

    path('события/', activity_list, name='activity_list'),
    path('события/новый/', activity_create, name='activity_create'),
    path('события/<int:pk>/редактировать /', activity_update, name='activity_edit'),
    path('события/<int:pk>/удалить/', activity_delete, name='activity_delete'),

    path('гостиницы/', hotel_list, name='hotel_list'),
    path('гостиницы/новый/', hotel_create, name='hotel_create'),
    path('гостиницы/<int:pk>/редактировать /', hotel_update, name='hotel_edit'),
    path('гостиницы/<int:pk>/удалить/', hotel_delete, name='hotel_delete'),

    path('зона-отдыха/', recreation_list, name='recreation_list'),
    path('зона-отдыха/новый/', recreation_create, name='recreation_create'),
    path('зона-отдыха/<int:pk>/редактировать /', recreation_update, name='recreation_edit'),
    path('зона-отдыха/<int:pk>/удалить/', recreation_delete, name='recreation_delete'),

    path('новости/', news_list, name='news_list'),
    path('новости/новый/', news_create, name='news_create'),
    path('новости/<int:pk>/редактировать /', news_update, name='news_edit'),
    path('новости/<int:pk>/удалить/', news_delete, name='news_delete'),

    path('фотографии/', photo_list, name='photo_list'),
    path('фотографии/новый/', photo_create, name='photo_create'),
    path('фотографии/<int:pk>/редактировать /', photo_update, name='photo_edit'),
    path('фотографии/<int:pk>/удалить/', photo_delete, name='photo_delete'),

    path('академический-отдел/', education_list, name='education_list'),
    path('академический-отдел/новый/', education_create, name='education_create'),
    path('академический-отдел/<int:pk>/редактировать /', education_update, name='education_edit'),
    path('академический-отдел/<int:pk>/удалить/', education_delete, name='education_delete'),
]
