from itertools import product

from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, CreateView

from therapyapp.forms import CooperationForm, RegisterUserForm, LoginUserForm
from therapyapp.models import Category, Product, Worker, CooperationRequest, Direction


class HomePageView(ListView):
    model = Category
    template_name = 'homepage.html'
    context_object_name = 'cats'
    extra_context = {'title': 'Therapy'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat1'] = Category.objects.filter(pk__gte=1, pk__lte=4)
        context['cat2'] = Category.objects.filter(pk__gte=5, pk__lte=8)
        return context


class CategoryView(ListView):
    model = Category
    template_name = 'categories.html'
    context_object_name = 'categories'
    extra_context = {'title': 'Направление товаров'}

    def get_queryset(self):
        return Category.objects.filter(direction__slug=self.kwargs['dir_slug'])

class ProductListView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    extra_context = {'title': 'Therapy'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['cats'] = Category.objects.all()
        return context

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['prod_slug'])


class ProductInfoView(ListView):
    model = Product
    template_name = 'product_info.html'
    context_object_name = 'products'
    extra_context = {'title': 'Therapy'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.filter(slug=self.kwargs['prod_slug'])
        return context


class ContactsView(ListView):
    model = Worker
    template_name = 'contacts.html'
    context_object_name = 'workers'
    extra_context = {'title': 'Сотрудники'}


class CooperationView(FormView):
    form_class = CooperationForm
    template_name = 'cooperation.html'
    success_url = '/'

    def form_valid(self, form):
        new_request = form.cleaned_data
        new_request_add = CooperationRequest(
            name=new_request['name'],
            company_name=new_request['company_name'],
            e_mail=new_request['e_mail'],
            phone=new_request['phone'],
            content=new_request['content']
        )
        new_request_add.save()
        return super().form_valid(form)


class RegistrationView(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration.html'
    success_url = '/'


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


