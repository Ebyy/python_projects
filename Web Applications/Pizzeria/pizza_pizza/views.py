from django.shortcuts import render
from .models import Pizza

# Create your views here.


def index(request):
    """Pizza-pizza Homepage set script"""
    return render(request, 'pizza_pizza/index.html')


def pizza(request):
    pizza_types = Pizza.objects.all()
    context = {'pizza_types': pizza_types}
    return render(request, 'pizza_pizza/pizza.html', context)


def topping(request, pizza_id):
    """"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizza_pizza/topping.html', context)
