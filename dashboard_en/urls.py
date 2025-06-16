from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name="login_page"),
    path('logout/', views.logout_page, name="logout_page"),

    path('account/', views.account_view, name='account_page'),
    path('settings/', views.settings_view, name='settings_page'),
    path('billing/', views.billing_view, name='billing_page'),

    path('', views.main_dashboard, name='main_dashboard'),

    path('about-us/', views.about_us_list, name='about_us_list'),
    path('about-us/yangi/', views.about_us_create, name='about_us_create'),
    path('about-us/<int:pk>/tahrirlash/', views.about_us_update, name='about_us_update'),
    path('about-us/<int:pk>/ochirish/', views.about_us_delete, name='about_us_delete'),

    path('activities/', views.activity_list, name='activity_list'),
    path('activities/yangi/', views.activity_create, name='activity_create'),
    path('activities/<int:pk>/tahrirlash/', views.activity_update, name='activity_edit'),
    path('activities/<int:pk>/ochirish/', views.activity_delete, name='activity_delete'),

    path('hotels/', views.hotel_list, name='hotel_list'),
    path('hotels/yangi/', views.hotel_create, name='hotel_create'),
    path('hotels/<int:pk>/tahrirlash/', views.hotel_update, name='hotel_edit'),
    path('hotels/<int:pk>/ochirish/', views.hotel_delete, name='hotel_delete'),

    path('recreation-zones/', views.recreation_list, name='recreation_list'),
    path('recreation-zones/yangi/', views.recreation_create, name='recreation_create'),
    path('recreation-zones/<int:pk>/tahrirlash/', views.recreation_update, name='recreation_edit'),
    path('recreation-zones/<int:pk>/ochirish/', views.recreation_delete, name='recreation_delete'),

    path('news/', views.news_list, name='news_list'),
    path('news/yangi/', views.news_create, name='news_create'),
    path('news/<int:pk>/tahrirlash/', views.news_update, name='news_edit'),
    path('news/<int:pk>/ochirish/', views.news_delete, name='news_delete'),

    path('photos/', views.photo_list, name='photo_list'),
    path('photos/yangi/', views.photo_create, name='photo_create'),
    path('photos/<int:pk>/tahrirlash/', views.photo_update, name='photo_edit'),
    path('photos/<int:pk>/ochirish/', views.photo_delete, name='photo_delete'),

    path('education/', views.education_list, name='education_list'),
    path('education/yangi/', views.education_create, name='education_create'),
    path('education/<int:pk>/tahrirlash/', views.education_update, name='education_edit'),
    path('education/<int:pk>/ochirish/', views.education_delete, name='education_delete'),
]
