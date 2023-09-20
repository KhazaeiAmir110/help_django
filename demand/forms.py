from django import forms
from .models import Demand


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Demand
        fields = ['title', 'slug', 'category', 'description', 'short_description', 'image', 'video']
