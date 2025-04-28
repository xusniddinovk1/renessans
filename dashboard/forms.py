from django import forms
from lager_app.models import *


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = ['image']
        widgets = {
            "image": forms.FileInput(attrs={"class": "form-control",
                                            "onchange": "loadFile(event)"})
        }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ["title", "description", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control",
                                            "onchange": "loadFile(event)"})
        }


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ["title", "description", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control",
                                            "onchange": "loadFile(event)"})
        }


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ["name", "description", "image"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control",
                                            "onchange": "loadFile(event)"})
        }


class RecreationForm(forms.ModelForm):
    class Meta:
        model = RecreationZone
        fields = ["title", "description", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control",
                                            "onchange": "loadFile(event)"})
        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ["title", "content", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control",
                                            "onchange": "loadFile(event)"})
        }
