from django.shortcuts import render , get_object_or_404
from .forms import OrderForm , MultiplePizzaForm 
from django.forms import formset_factory
from .models import Pizza
from django.contrib.auth.decorators import login_required

@login_required
def order(request):
  multiple_form = MultiplePizzaForm()
  if request.method == 'POST':
    filled_form = OrderForm(request.POST)
    if filled_form.is_valid():
      CreatedPizza = filled_form.save(commit = False)
      CreatedPizza.user = request.user
      CreatedPizza.save()
      CreatedPizza_pk = CreatedPizza.id
      note = "thanks for order :) your %s %s and %s is on it's way" % (filled_form.cleaned_data['Size'], filled_form.cleaned_data['topping1'], filled_form.cleaned_data['topping2'])
      filled_form = OrderForm()
    else :
      CreatedPizza_pk = None
      note = "Pizza order has been failed :("
    return render(request, 'order/order.html', {'createdpizza_pk':CreatedPizza_pk ,'OrderForm': filled_form , 'note': note , 'multipleForm': multiple_form})  
  else :
    form = OrderForm()
    return render(request, 'order/order.html', {'OrderForm': form ,'multipleForm': multiple_form })

@login_required
def pizzas (request):
  number_of_pizza = 2
  filled_multiple_pizza_form = MultiplePizzaForm(request.GET)
  if filled_multiple_pizza_form.is_valid():
    number_of_pizza = filled_multiple_pizza_form.cleaned_data['number']
  OrderFormSet = formset_factory(OrderForm , extra= number_of_pizza)  
  formset = OrderFormSet() 
  if request.method == 'POST':
    filled_formset = OrderFormSet(request.POST)
    if filled_formset.is_valid():
      for form in filled_formset :
        pizza = form.save(commit=False)
        pizza.user = request.user 
        pizza.save()
      note = "pizzas have been ordered :)"
    else :
      note = "order didnt registered :( , please try again "    
    return render(request, 'order/multiple_pizza.html',{'note':note , 'formset':formset})
  else :
    return render(request, 'order/multiple_pizza.html',{'formset': formset})

@login_required  
def edit_order(request , pk ):
  pizza = get_object_or_404(Pizza, pk=pk, user=request.user)
  pizza = Pizza.objects.get(pk = pk) 
  form = OrderForm(instance=pizza)
  if request.method == 'POST':
    filled_form = OrderForm(request.POST, instance=pizza)
    if filled_form.is_valid():
      filled_form.save()
      form = filled_form
      note = "Order has been updated "
      return render(request, 'order/edit_order.html',{'note': note,'OrderForm':form ,'pizza':pizza})
  return render(request, 'order/edit_order.html',{'OrderForm':form ,'pizza':pizza})  