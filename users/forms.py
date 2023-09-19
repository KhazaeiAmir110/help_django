from django import forms
from django.forms.widgets import ClearableFileInput
from demand.models import Demand
from multiupload.fields import MultiFileField


class DemandForm(forms.ModelForm):
    class Meta:
        model = Demand
        fields = ['title', 'slug', 'category', 'description']
        labels = {
            'title': 'عنوان',
            'slug': 'اسلاگ',
            'category': 'دسته‌بندی',
            'description': 'توضیحات',
        }

    image = MultiFileField()
    video = MultiFileField()


class DemandFormm(forms.Form):
    title = forms.CharField(max_length=100)
    slug = forms.SlugField()
    category = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    video = MultiFileField()
    image = MultiFileField()
