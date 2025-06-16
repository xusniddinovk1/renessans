from django.urls import path
from dashboard_en.views import *

urlpatterns = [
    path('login/', login_page, name="login_page"),
    path('logout/', logout_page, name="logout_page"),

    path('account/', account_view, name='account_page'),
    path('settings/', settings_view, name='settings_page'),
    path('billing/', billing_view, name='billing_page'),

    path('', main_dashboard, name='main_dashboard'),

    path('about-us/', about_us_list, name='about_us_list'),
    path('about-us/yangi/', about_us_create, name='about_us_create'),
    path('about-us/<int:pk>/tahrirlash/', about_us_update, name='about_us_update'),
    path('about-us/<int:pk>/ochirish/', about_us_delete, name='about_us_delete'),

    path('activities/', activity_list, name='activity_list'),
    path('activities/yangi/', activity_create, name='activity_create'),
    path('activities/<int:pk>/tahrirlash/', activity_update, name='activity_edit'),
    path('activities/<int:pk>/ochirish/', activity_delete, name='activity_delete'),

    path('hotels/', hotel_list, name='hotel_list'),
    path('hotels/yangi/', hotel_create, name='hotel_create'),
    path('hotels/<int:pk>/tahrirlash/', hotel_update, name='hotel_edit'),
    path('hotels/<int:pk>/ochirish/', hotel_delete, name='hotel_delete'),

    path('recreation-zones/', recreation_list, name='recreation_list'),
    path('recreation-zones/yangi/', recreation_create, name='recreation_create'),
    path('recreation-zones/<int:pk>/tahrirlash/', recreation_update, name='recreation_edit'),
    path('recreation-zones/<int:pk>/ochirish/', recreation_delete, name='recreation_delete'),

    path('news/', news_list, name='news_list'),
    path('news/yangi/', news_create, name='news_create'),
    path('news/<int:pk>/tahrirlash/', news_update, name='news_edit'),
    path('news/<int:pk>/ochirish/', news_delete, name='news_delete'),

    path('photos/', photo_list, name='photo_list'),
    path('photos/yangi/', photo_create, name='photo_create'),
    path('photos/<int:pk>/tahrirlash/', photo_update, name='photo_edit'),
    path('photos/<int:pk>/ochirish/', photo_delete, name='photo_delete'),

    path('education/', education_list, name='education_list'),
    path('education/yangi/', education_create, name='education_create'),
    path('education/<int:pk>/tahrirlash/', education_update, name='education_edit'),
    path('education/<int:pk>/ochirish/', education_delete, name='education_delete'),
]
