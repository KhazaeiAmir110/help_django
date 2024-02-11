from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
import datetime

from django.views import View
from cor.cart import Cart
from products.models import Product
from .forms import CartAddForm, CouponForm
from .models import Order, OrderItem, Coupon


class CartView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'orders/cart.html', {'cart': cart})


class CartAddView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddForm(request.POST)
        if form.is_valid():
            cart.add(product, form.cleaned_data['quantity'])
        return redirect('orders:carts')


class CartRemoveView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('orders:carts')


"""
    :keyword
"""


# Orders Detail
class OrderDetailView(LoginRequiredMixin, View):
    form = CouponForm()

    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        return render(request, 'orders/order_detail.html', {'order': order, 'form': self.form})


# Order Create
class OrderCreateView(LoginRequiredMixin, View):
    def get(self, request, ):
        cart = Cart(request)
        order = Order.objects.create(user=request.user)

        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], price=item['price'],
                                     quantity=item['quantity'])
        cart.clear()
        return redirect('orders:order_detail', order.id)


"""
    :Pay
"""


# Zarin pal
class OrderPayView(LoginRequiredMixin, View):
    def get(self, request, order_id):
        pass


# Verify
class OrderVerifyView(LoginRequiredMixin, View):
    def get(self, request):
        pass


# Apply
class CouponApplyView(LoginRequiredMixin, View):
    form_class = CouponForm

    def post(self, request, order_id):
        now = datetime.datetime.now()
        form = self.form_class(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                coupon = Coupon.objects.get(code__exact=code, valid_form__lte=now,
                                            valid_to__gte=now, active=True)
            except Coupon.DoesNotExist:
                messages.error(request, 'this coupon does not exists', 'danger')
                return redirect('orders:order_detail', order_id)
            order = Order.objects.get(id=order_id)
            order.discount = coupon.discount
            order.save()
        return redirect('orders:order_detail', order_id)
