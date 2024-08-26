from unicodedata import category

from django.views.generic import ListView

from therapyapp.models import Category, Product, Worker


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