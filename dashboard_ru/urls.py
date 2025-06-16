from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name="login_page"),
    path('logout/', views.logout_page, name="logout_page"),

    path('account/', views.account_view, name='account_page'),
    path('settings/', views.settings_view, name='settings_page'),
    path('billing/', views.billing_view, name='billing_page'),

    path('', views.main_dashboard, name='main_dashboard'),

    path('о-нас/', views.about_us_list, name='about_us_list'),
    path('о-нас/yangi/', views.about_us_create, name='about_us_create'),
    path('о-нас/<int:pk>/tahrirlash/', views.about_us_update, name='about_us_update'),
    path('о-нас/<int:pk>/ochirish/', views.about_us_delete, name='about_us_delete'),

    path('деятельность/', views.activity_list, name='activity_list'),
    path('деятельность/yangi/', views.activity_create, name='activity_create'),
    path('деятельность/<int:pk>/tahrirlash/', views.activity_update, name='activity_edit'),
    path('деятельность/<int:pk>/ochirish/', views.activity_delete, name='activity_delete'),

    path('гостиницы/', views.hotel_list, name='hotel_list'),
    path('гостиницы/yangi/', views.hotel_create, name='hotel_create'),
    path('гостиницы/<int:pk>/tahrirlash/', views.hotel_update, name='hotel_edit'),
    path('гостиницы/<int:pk>/ochirish/', views.hotel_delete, name='hotel_delete'),

    path('зона-отдыха/', views.recreation_list, name='recreation_list'),
    path('зона-отдыха/yangi/', views.recreation_create, name='recreation_create'),
    path('зона-отдыха/<int:pk>/tahrirlash/', views.recreation_update, name='recreation_edit'),
    path('зона-отдыха/<int:pk>/ochirish/', views.recreation_delete, name='recreation_delete'),

    path('новости/', views.news_list, name='news_list'),
    path('новости/yangi/', views.news_create, name='news_create'),
    path('новости/<int:pk>/tahrirlash/', views.news_update, name='news_edit'),
    path('новости/<int:pk>/ochirish/', views.news_delete, name='news_delete'),

    path('rasmlar/', views.photo_list, name='photo_list'),
    path('rasmlar/yangi/', views.photo_create, name='photo_create'),
    path('rasmlar/<int:pk>/tahrirlash/', views.photo_update, name='photo_edit'),
    path('rasmlar/<int:pk>/ochirish/', views.photo_delete, name='photo_delete'),

    path('академический-отдел/', views.education_list, name='education_list'),
    path('академический-отдел/yangi/', views.education_create, name='education_create'),
    path('академический-отдел/<int:pk>/tahrirlash/', views.education_update, name='education_edit'),
    path('академический-отдел/<int:pk>/ochirish/', views.education_delete, name='education_delete'),
]
