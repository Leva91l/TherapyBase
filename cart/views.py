from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render

from cart.cart_forms import AddQuantityForm
from cart.models import Cart, Favorite
from cart.mail import send_mail
from therapyapp.models import Product


def cart(request):
    cart_items = Cart.objects.filter(user_id=request.user.id).order_by('created_timestamp')
    total = cart_items.aggregate(Sum('price'))['price__sum']
    context = {'cart': cart_items, 'total': total}
    return render(request, 'cart/basket.html', context)


def favorite(request):
    favorite_items = Favorite.objects.filter(user_id=request.user.id)
    context = {'favorite_items': favorite_items, }
    return render(request, 'favorite.html', context)


def favorite_add(request, product_id):
    product = Product.objects.get(id=product_id)
    favorite = Favorite.objects.filter(user=request.user.id, product=product)

    if not favorite.exists():
        Favorite.objects.create(user=request.user, product=product)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def favorite_remove(request, id):
    favorite = Favorite.objects.get(id=id)
    favorite.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_remove(request, id):
    cart = Cart.objects.get(id=id)
    cart.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_add(request, product_id):
    product = Product.objects.get(id=product_id)
    price = product.price
    carts = Cart.objects.filter(user=request.user, product=product)

    if not carts.exists():
        Cart.objects.create(user=request.user, product=product, quantity=1, price=price)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        cart = carts.first()
        cart.quantity += 1
        cart.price += price
        cart.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def add_quantity(request, id):
    cart = Cart.objects.get(id=id)
    cart.quantity += 1
    cart.price += cart.product.price
    cart.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_quantity(request, id):
    cart = Cart.objects.get(id=id)
    cart.quantity -= 1
    if cart.quantity == 0:
        cart.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        cart.price -= cart.product.price
        cart.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def add_quantity_man(request):
    form = AddQuantityForm()
    return render(request, 'cart/basket.html', {'form': form})


def send_to_manager(request):
    cart_objects = Cart.objects.filter(user=request.user.id)
    user = request.user.username
    order = {}

    for cart_object in cart_objects:
        product_name = cart_object.product.name
        quantity = cart_object.quantity
        manufacturer = cart_object.product.manufacturer
        order[product_name] = [quantity, manufacturer]
    message = ''
    for key, value in order.items():
        string = f'{key}: количество - {value[0]} шт, производитель - {value[1]}\n\n'
        message += string
    send_mail(user, 'levapython@yandex.ru', message)
    cart_objects.delete()
    return render(request, 'success_order.html')
