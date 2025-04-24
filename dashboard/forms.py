from django import forms
from lager_app.models import *


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['title', 'description', 'image']


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'description', 'image']


class RecreationForm(forms.ModelForm):
    class Meta:
        model = RecreationZone
        fields = ['title', 'description', 'image']


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'image']
