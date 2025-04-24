# camp/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_page, name="login_page"),
    path('logout/', views.logout_page, name="logout_page"),

    path('', views.dashboard, name='dashboard'),

    path('faoliyatlar/', views.activity_list, name='activity_list'),
    path('faoliyatlar/yangi/', views.activity_create, name='activity_create'),
    path('faoliyatlar/<int:pk>/tahrirlash/', views.activity_update, name='activity_update'),
    path('faoliyatlar/<int:pk>/ochirish/', views.activity_delete, name='activity_delete'),

    path('mehmonxonalar/', views.hotel_list, name='hotel_list'),
    path('mehmonxonalar/yangi/', views.hotel_create, name='hotel_create'),
    path('mehmonxonalar/<int:pk>/tahrirlash/', views.hotel_update, name='hotel_update'),
    path('mehmonxonalar/<int:pk>/ochirish/', views.hotel_delete, name='hotel_delete'),

    path('istirohat-zonalari/', views.recreation_list, name='recreation_list'),
    path('istirohat-zonalari/yangi/', views.recreation_create, name='recreation_create'),
    path('istirohat-zonalari/<int:pk>/tahrirlash/', views.recreation_update, name='recreation_update'),
    path('istirohat-zonalari/<int:pk>/ochirish/', views.recreation_delete, name='recreation_delete'),

    path('yangiliklar/', views.news_list, name='news_list'),
    path('yangiliklar/yangi/', views.news_create, name='news_create'),
    path('yangiliklar/<int:pk>/tahrirlash/', views.news_update, name='news_update'),
    path('yangiliklar/<int:pk>/ochirish/', views.news_delete, name='news_delete'),
]
