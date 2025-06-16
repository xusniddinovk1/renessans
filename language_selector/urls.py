from django.urls import path
from .views import select_language

urlpatterns = [
    path('', select_language, name='select_language'),
]
