from django import forms
from lager_app_en.models import *


class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs1
        fields = ['context']
        widgets = {
            "context": forms.TextInput(attrs={"class": "form-control"})
        }


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photos1
        fields = ['image']
        widgets = {
            "image": forms.FileInput(attrs={"class": "form-control",
                                            "onchange": "loadFile(event)"})
        }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education1
        fields = ["title", "description", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control",
                                            "onchange": "loadFile(event)"})
        }


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity1
        fields = ["title", "description", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control",
                                            "onchange": "loadFile(event)"})
        }


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel1
        fields = ["name", "description", "image"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control",
                                            "onchange": "loadFile(event)"})
        }


class RecreationForm(forms.ModelForm):
    class Meta:
        model = RecreationZone1
        fields = ["title", "description", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control",
                                            "onchange": "loadFile(event)"})
        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News1
        fields = ["title", "content", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control",
                                            "onchange": "loadFile(event)"})
        }
