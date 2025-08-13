from django import forms
from lager_app_en.models import AboutUs1, Photos1, Education1, Activity1, Hotel1, RecreationZone1, News1


class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs1
        fields = ['context', 'image']
        widgets = {
            "context": forms.Textarea(
                attrs={"class": "form-control", "rows": 5, "placeholder": "Biz haqimizda matn..."}),
            "image": forms.FileInput(attrs={"class": "form-control", "onchange": "loadFile(event)"}),
        }


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photos1
        fields = ['image']
        widgets = {
            "image": forms.FileInput(attrs={"class": "form-control", "onchange": "loadFile(event)"}),
        }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education1
        fields = ["title", "description", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Sarlavha kiriting"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Ta’rif yozing"}),
            "image": forms.FileInput(attrs={"class": "form-control", "onchange": "loadFile(event)"}),
        }


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity1
        fields = ["title", "description", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Faoliyat nomi"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Faoliyat haqida"}),
            "image": forms.FileInput(attrs={"class": "form-control", "onchange": "loadFile(event)"}),
        }


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel1
        fields = ["name", "description", "image"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Mehmonxona nomi"}),
            "description": forms.Textarea(
                attrs={"class": "form-control", "rows": 4, "placeholder": "Mehmonxona haqida"}),
            "image": forms.FileInput(attrs={"class": "form-control", "onchange": "loadFile(event)"}),
        }


class RecreationForm(forms.ModelForm):
    class Meta:
        model = RecreationZone1
        fields = ["title", "description", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Zona nomi"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Zona haqida"}),
            "image": forms.FileInput(attrs={"class": "form-control", "onchange": "loadFile(event)"}),
        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News1
        fields = ["title", "content", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Yangilik sarlavhasi"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Yangilik matni"}),
            "image": forms.FileInput(attrs={"class": "form-control", "onchange": "loadFile(event)"}),
        }
