from django.urls import path
from dashboard.views import *


app_name = 'dashboard'


urlpatterns = [
    path('login/', login_page, name="login_page"),
    path('logout/', logout_page, name="logout_page"),

    path('account/', account_view, name='account_page'),
    path('settings/', settings_view, name='settings_page'),
    path('billing/', billing_view, name='billing_page'),

    path('', main_dashboard, name='main_dashboard'),

    path('bizhaqimizda/', about_us_list, name='bizhaqimizda'),
    path('bizhaqimizda/yangi/', about_us_create, name='bizhaqimizda_create'),
    path('bizhaqimizda/<int:pk>/tahrirlash/', about_us_update, name='bizhaqimizda_update'),
    path('bizhaqimizda/<int:pk>/ochirish/', about_us_delete, name='bizhaqimizda_delete'),

    path('faoliyatlar/', activity_list, name='faoliyatlar_list'),
    path('faoliyatlar/yangi/', activity_create, name='faoliyatlar_create'),
    path('faoliyatlar/<int:pk>/tahrirlash/', activity_update, name='faoliyatlar_edit'),
    path('faoliyatlar/<int:pk>/ochirish/', activity_delete, name='faoliyatlar_delete'),

    path('mehmonxonalar/', hotel_list, name='mehmonxonalar_list'),
    path('mehmonxonalar/yangi/', hotel_create, name='mehmonxonalar_create'),
    path('mehmonxonalar/<int:pk>/tahrirlash/', hotel_update, name='mehmonxonalar_edit'),
    path('mehmonxonalar/<int:pk>/ochirish/', hotel_delete, name='mehmonxonalar_delete'),

    path('istirohat-zonalari/', recreation_list, name='istirohat_list'),
    path('istirohat-zonalari/yangi/', recreation_create, name='istirohat_create'),
    path('istirohat-zonalari/<int:pk>/tahrirlash/', recreation_update, name='istirohat_edit'),
    path('istirohat-zonalari/<int:pk>/ochirish/', recreation_delete, name='istirohat_delete'),

    path('yangiliklar/', news_list, name='yangiliklar_list'),
    path('yangiliklar/yangi/', news_create, name='yangiliklar_create'),
    path('yangiliklar/<int:pk>/tahrirlash/', news_update, name='yangiliklar_edit'),
    path('yangiliklar/<int:pk>/ochirish/', news_delete, name='yangiliklar_delete'),

    path('rasmlar/', photo_list, name='rasmlar_list'),
    path('rasmlar/yangi/', photo_create, name='rasmlar_create'),
    path('rasmlar/<int:pk>/tahrirlash/', photo_update, name='rasmlar_edit'),
    path('rasmlar/<int:pk>/ochirish/', photo_delete, name='rasmlar_delete'),

    path('oquvbolim/', education_list, name='oquvbolim_list'),
    path('oquvbolim/yangi/', education_create, name='oquvbolim_create'),
    path('oquvbolim/<int:pk>/tahrirlash/', education_update, name='oquvbolim_edit'),
    path('oquvbolim/<int:pk>/ochirish/', education_delete, name='oquvbolim_delete'),
]
