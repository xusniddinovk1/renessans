from django.urls import path
from dashboard.views import *

urlpatterns = [
    path('login/', login_page, name="login_page"),
    path('logout/', logout_page, name="logout_page"),

    path('account/', account_view, name='account_page'),
    path('settings/', settings_view, name='settings_page'),
    path('billing/', billing_view, name='billing_page'),

    path('', main_dashboard, name='main_dashboard'),

    path('bizhaqimizda/', about_us_list, name='about_us_list'),
    path('bizhaqimizda/yangi/', about_us_create, name='about_us_create'),
    path('bizhaqimizda/<int:pk>/tahrirlash/', about_us_update, name='about_us_update'),
    path('bizhaqimizda/<int:pk>/ochirish/', about_us_delete, name='about_us_delete'),

    path('faoliyatlar/', activity_list, name='activity_list'),
    path('faoliyatlar/yangi/', activity_create, name='activity_create'),
    path('faoliyatlar/<int:pk>/tahrirlash/', activity_update, name='activity_edit'),
    path('faoliyatlar/<int:pk>/ochirish/', activity_delete, name='activity_delete'),

    path('mehmonxonalar/', hotel_list, name='hotel_list'),
    path('mehmonxonalar/yangi/', hotel_create, name='hotel_create'),
    path('mehmonxonalar/<int:pk>/tahrirlash/', hotel_update, name='hotel_edit'),
    path('mehmonxonalar/<int:pk>/ochirish/', hotel_delete, name='hotel_delete'),

    path('istirohat-zonalari/', recreation_list, name='recreation_list'),
    path('istirohat-zonalari/yangi/', recreation_create, name='recreation_create'),
    path('istirohat-zonalari/<int:pk>/tahrirlash/', recreation_update, name='recreation_edit'),
    path('istirohat-zonalari/<int:pk>/ochirish/', recreation_delete, name='recreation_delete'),

    path('yangiliklar/', news_list, name='news_list'),
    path('yangiliklar/yangi/', news_create, name='news_create'),
    path('yangiliklar/<int:pk>/tahrirlash/', news_update, name='news_edit'),
    path('yangiliklar/<int:pk>/ochirish/', news_delete, name='news_delete'),

    path('rasmlar/', photo_list, name='photo_list'),
    path('rasmlar/yangi/', photo_create, name='photo_create'),
    path('rasmlar/<int:pk>/tahrirlash/', photo_update, name='photo_edit'),
    path('rasmlar/<int:pk>/ochirish/', photo_delete, name='photo_delete'),

    path('oquvbolim/', education_list, name='education_list'),
    path('oquvbolim/yangi/', education_create, name='education_create'),
    path('oquvbolim/<int:pk>/tahrirlash/', education_update, name='education_edit'),
    path('oquvbolim/<int:pk>/ochirish/', education_delete, name='education_delete'),
]
