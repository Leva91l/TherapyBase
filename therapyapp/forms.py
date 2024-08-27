from django import forms


class CooperationForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ваше имя')
    company_name = forms.CharField(max_length=120, label='Название вашей компании', required=False)
    e_mail = forms.CharField(max_length=100, label='Ваш email')
    phone = forms.CharField(max_length=12, label='Номер телефона')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':40, 'rows':5}), label='Для доп.информации/вопроса')
