from django.urls import path
from dashboard_ru.views import *

urlpatterns = [
    path('login/', login_page, name="login_page"),
    path('logout/', logout_page, name="logout_page"),

    path('account/', account_view, name='account_page'),
    path('settings/', settings_view, name='settings_page'),
    path('billing/', billing_view, name='billing_page'),

    path('', main_dashboard, name='main_dashboard'),

    path('о-нас/', about_us_list, name='about_us_list'),
    path('о-нас/yangi/', about_us_create, name='about_us_create'),
    path('о-нас/<int:pk>/tahrirlash/', about_us_update, name='about_us_update'),
    path('о-нас/<int:pk>/ochirish/', about_us_delete, name='about_us_delete'),

    path('деятельность/', activity_list, name='activity_list'),
    path('деятельность/yangi/', activity_create, name='activity_create'),
    path('деятельность/<int:pk>/tahrirlash/', activity_update, name='activity_edit'),
    path('деятельность/<int:pk>/ochirish/', activity_delete, name='activity_delete'),

    path('гостиницы/', hotel_list, name='hotel_list'),
    path('гостиницы/yangi/', hotel_create, name='hotel_create'),
    path('гостиницы/<int:pk>/tahrirlash/', hotel_update, name='hotel_edit'),
    path('гостиницы/<int:pk>/ochirish/', hotel_delete, name='hotel_delete'),

    path('зона-отдыха/', recreation_list, name='recreation_list'),
    path('зона-отдыха/yangi/', recreation_create, name='recreation_create'),
    path('зона-отдыха/<int:pk>/tahrirlash/', recreation_update, name='recreation_edit'),
    path('зона-отдыха/<int:pk>/ochirish/', recreation_delete, name='recreation_delete'),

    path('новости/', news_list, name='news_list'),
    path('новости/yangi/', news_create, name='news_create'),
    path('новости/<int:pk>/tahrirlash/', news_update, name='news_edit'),
    path('новости/<int:pk>/ochirish/', news_delete, name='news_delete'),

    path('rasmlar/', photo_list, name='photo_list'),
    path('rasmlar/yangi/', photo_create, name='photo_create'),
    path('rasmlar/<int:pk>/tahrirlash/', photo_update, name='photo_edit'),
    path('rasmlar/<int:pk>/ochirish/', photo_delete, name='photo_delete'),

    path('академический-отдел/', education_list, name='education_list'),
    path('академический-отдел/yangi/', education_create, name='education_create'),
    path('академический-отдел/<int:pk>/tahrirlash/', education_update, name='education_edit'),
    path('академический-отдел/<int:pk>/ochirish/', education_delete, name='education_delete'),
]
