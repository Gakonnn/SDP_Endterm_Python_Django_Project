from django.shortcuts import render, get_object_or_404 ,redirect
from .models import Product, Order
from .decorators.product_decorator import ProductDecorator
from .observers.notification_observer import OrderObserver
from .forms import ProductForm, OrderForm

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    decorator = ProductDecorator(product)
    decorator.add_discount(10)
    decorator.add_tag("Featured")

    product.save()
    return render(request, 'product_detail.html', {'product': product})


def update_order_status(request, order_id, new_status):
    order = get_object_or_404(Order, id=order_id)
    order.status = new_status
    order.save()

    observer = OrderObserver()
    observer.update(order)

    return render(request, 'order_status.html', {'order': order})


def main_page(request):
    # Retrieve all products and orders
    products = Product.objects.all()
    orders = Order.objects.all()

    # Initialize forms
    product_form = ProductForm()
    order_form = OrderForm()

    # Handle form submissions
    if request.method == 'POST':
        if 'product_form' in request.POST:
            product_form = ProductForm(request.POST)
            if product_form.is_valid():
                product_form.save()
                return redirect('main_page')
        elif 'order_form' in request.POST:
            order_form = OrderForm(request.POST)
            if order_form.is_valid():
                order_form.save()
                return redirect('main_page')

    # Render the main page template with products, orders, and forms
    return render(request, 'index.html', {
        'products': products,
        'orders': orders,
        'product_form': product_form,
        'order_form': order_form,
    })