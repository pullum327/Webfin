from django.shortcuts import render, redirect
from .models import Product, CartItem
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import JsonResponse
from django.contrib import messages
def product_list(request):
    products = Product.objects.all()
    return render(request, 'menu.html', {'products': products})
 
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})



def view_payment(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'payment.html', {'cart_items': cart_items, 'total_price': total_price})
def payment(request,product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, 
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:view_payment')


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, 
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    messages.add_message(request, messages.SUCCESS, '成功添加到购物车')

    # 返回一个简单的HttpResponse
    return render(request, 'menu.html', {})
 
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart:view_cart')
 
def details(request, id):
    book = Product.objects.get(id=id)
    template = loader.get_template('detail.html')
    context = {
      'book': book,
    }
    return HttpResponse(template.render(context, request))

def wishl(request):
      template = loader.get_template('wishl.html')
      return HttpResponse(template.render())
def manage(request):
      template = loader.get_template('manage.html')
      return HttpResponse(template.render())
def personal(request):
      template = loader.get_template('personal.html')
      return HttpResponse(template.render())
def product_search(request):
    search_query = request.GET.get('search', '')
    products = Product.objects.all()
    if search_query:
        products = products.filter(name__icontains=search_query)
    
    return render(request, 'detail.html', {'products': products})