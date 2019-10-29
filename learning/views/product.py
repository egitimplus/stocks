from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET
from learning.models import Product
from django.db import transaction
from django.views import View
from django.views.generic import ListView, DetailView

@require_GET
def product(request, pk=None):
    queryset = Product.objects.get(pk=pk)
    content = {
        'product_detail': queryset
    }
    return render(request=request, template_name='product/detail.html', context=content)

@transaction.non_atomic_requests
def products(request):
    queryset = Product.objects.all()[:2]
    content = {
        'products': queryset
    }
    return render(request=request, template_name='product/list.html', context=content)

def product_archieve(request, year=None, month=None):

    queryset = Product.objects.filter(created__year=year, created__month=month)

    content = {
        'year': year,
        'month': month,
        'products': queryset
    }
    return render(request=request, template_name='product/archieve.html', context=content)


class ProductView(View):

    def get(self, request):
        product_list = Product.objects.all()[:2]

        content = {
            'products' : product_list
        }

        return render(request=request, template_name='product/list.html', context=content)

    def post(self, request):
        pass


class ProductListView(ListView):
    model = Product
    template_name = 'product/list.html'
    context_object_name = 'products' #object_list
    queryset = Product.objects.all()[:2]


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/detail.html'
    context_object_name = 'product_detail'
