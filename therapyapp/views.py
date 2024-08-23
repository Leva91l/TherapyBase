from django.shortcuts import render
from django.views.generic import ListView

from therapyapp.models import Category


class HomePageView(ListView):
    model = Category
    template_name = 'homepage.html'
    context_object_name = 'cats'
    extra_context = {'title': 'Therapy'}