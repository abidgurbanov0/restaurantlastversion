from django.shortcuts import render, redirect
from django.views import View
from restaurant.models import Customer
from restaurant.models import Order

class OrderView(View):
	def get(self,request):
		customer_id = request.session.get('customer')
		orders = Order.objects.filter(customer=customer_id).order_by("-date").order_by("-id")
		print(orders)
		return render(request,'order.html',{"orders":orders})