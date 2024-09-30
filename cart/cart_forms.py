from django import forms


class AddQuantityForm(forms.Form):
    quantity = forms.IntegerField()
    name = forms.CharField(max_length=100)