from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Product, Rating


# Create your views here.


class ProductList(ListView):
    model = Product
    template_name = 'shop/index.html'
    context_object_name = 'products'
    extra_context = {
        'categories': Category.objects.filter(parent=None),
        'title': "Barcha Produclar",
        'all_products': Product.objects.all()
    }


class AllProductList(ProductList):
    template_name = 'shop/all_products.html'


def detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    context = {
        'categories': Category.objects.filter(parent=None),
        'product': product
    }
    rating = Rating.objects.filter(post=product, user=request.user.id).first()  # Requestdan foydalanish
    product.user_rating = rating.rating if rating else 0
    return render(request, 'shop/detail.html', context=context)


def product_by_category(request, pk):
    category = Category.objects.get(pk=pk)
    products = Product.objects.filter(category=category)
    context = {
        'categories': Category.objects.filter(parent=None),
        'products': products,
        'all_products': Product.objects.all()
    }
    return render(request, 'shop/all_products.html', context=context)


def rate(request: HttpRequest, post_id: int, rating: int) -> HttpResponse:
    post = Product.objects.get(id=post_id)
    Rating.objects.filter(post=post, user=request.user).delete()
    post.rating_set.create(user=request.user, rating=rating)
    return detail(request, post_id)
