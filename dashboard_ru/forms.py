from django import forms
from lager_app_ru.models import AboutUs2, Photos2, Education2, Activity2, Hotel2, RecreationZone2, News2


class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs2
        fields = ['context']
        widgets = {
            "context": forms.Textarea(
                attrs={"class": "form-control", "rows": 5, "placeholder": "Biz haqimizda matn..."}),
        }


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photos2
        fields = ['image']
        widgets = {
            "image": forms.FileInput(attrs={"class": "form-control", "onchange": "loadFile(event)"}),
        }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education2
        fields = ["title", "description", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Sarlavha kiriting"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Ta’rif yozing"}),
            "image": forms.FileInput(attrs={"class": "form-control", "onchange": "loadFile(event)"}),
        }


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity2
        fields = ["title", "description", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Faoliyat nomi"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Faoliyat haqida"}),
            "image": forms.FileInput(attrs={"class": "form-control", "onchange": "loadFile(event)"}),
        }


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel2
        fields = ["name", "description", "image"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Mehmonxona nomi"}),
            "description": forms.Textarea(
                attrs={"class": "form-control", "rows": 4, "placeholder": "Mehmonxona haqida"}),
            "image": forms.FileInput(attrs={"class": "form-control", "onchange": "loadFile(event)"}),
        }


class RecreationForm(forms.ModelForm):
    class Meta:
        model = RecreationZone2
        fields = ["title", "description", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Zona nomi"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Zona haqida"}),
            "image": forms.FileInput(attrs={"class": "form-control", "onchange": "loadFile(event)"}),
        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News2
        fields = ["title", "content", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Yangilik sarlavhasi"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Yangilik matni"}),
            "image": forms.FileInput(attrs={"class": "form-control", "onchange": "loadFile(event)"}),
        }
