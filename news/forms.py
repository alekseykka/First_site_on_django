from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'photo', 'category', 'is_published']
        widgets = {'title': forms.TextInput(attrs={"class": "form-control"}),
                   'content': forms.Textarea(attrs={"class": "form-control"}),
                   'photo': forms.FileInput(attrs={"class": "form-control",
                                                   "type": "file",
                                                   "enctype ": "multipart/form-data",
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


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя:', help_text='Минимум 8 символов',
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.CharField(label='Email:', widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label='Пароль:', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Подтверждение пароля:',
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop('autofocus')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя:', widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label='Пароль:', widget=forms.PasswordInput(attrs={"class": "form-control"}))
