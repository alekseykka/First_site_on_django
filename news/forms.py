from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'photo', 'category', 'is_published']
        widgets = {'title': forms.TextInput(attrs={"class": "form-control"}),
                   'content': forms.Textarea(attrs={"class": "form-control"}),
                   'photo': forms.FileInput(attrs={"class": "form-control",
                                                   "type": "file",
                                                   "id": "formFileMultiple"}),
                   'category': forms.Select(attrs={"class": "form-select"}),
                   'is_published': forms.CheckboxInput(attrs={
                       "class": "form-check-input",
                       "id": "flexSwitchCheckReverse"})
                   }


    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError("Название не должно начинаться с цифры")
        return title
