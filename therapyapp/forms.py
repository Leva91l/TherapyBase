from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CooperationForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ваше имя')
    company_name = forms.CharField(max_length=120, label='Название вашей компании', required=False)
    e_mail = forms.CharField(max_length=100, label='Ваш email')
    phone = forms.CharField(max_length=12, label='Номер телефона')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':40, 'rows':5}), label='Для доп.информации/вопроса')

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class MailingOfPromoForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=30)