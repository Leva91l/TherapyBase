from unicodedata import category

from django.views.generic import ListView, FormView

from therapyapp.forms import CooperationForm
from therapyapp.models import Category, Product, Worker, CooperationRequest


class HomePageView(ListView):
    model = Category
    template_name = 'homepage.html'
    context_object_name = 'cats'
    extra_context = {'title': 'Therapy'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat1'] = Category.objects.filter(pk__gte=1, pk__lte=5)
        context['cat2'] = Category.objects.filter(pk__gte=6, pk__lte=10)
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    extra_context = {'title': 'Therapy'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.all()
        return context

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['prod_slug'])


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
