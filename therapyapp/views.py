from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, CreateView

from therapyapp.forms import CooperationForm, RegisterUserForm, LoginUserForm
from therapyapp.models import Category, Product, Worker, CooperationRequest


class HomePageView(ListView):
    model = Category
    template_name = 'homepage.html'
    context_object_name = 'cats'
    extra_context = {'title': 'Therapy'}


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

# class MailingView(FormView):
#     form_class = MailingOfPromoForm
#     template_name = 'homepage.html'
#     success_url = '/'


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


class Search(ListView):
    template_name = 'search_page.html'
    context_object_name = 'searchproduct'

    def get_queryset(self):
        return Product.objects.filter(name__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


def delivery(request):
    return render(request, 'delivery.html')

def about(request):
    return render(request, 'about.html')


class FoundNothing(FormView):
    form_class = CooperationForm
    template_name = 'found_nothing.html'
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
