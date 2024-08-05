from django import forms
from .models import Pizza , Size

# class OrderForm(forms.Form):
#   Topping1 = forms.CharField (label= 'Topping1', max_length= 30 ) 
#   Topping2 = forms.CharField (label= 'Topping2', max_length= 30 )
#   Size = forms.ChoiceField (label= 'Size', choices=[("Small","Small"), ("Medium","Medium"),("Large","Large")])

class OrderForm (forms.ModelForm) :
  
  Size = forms.ModelChoiceField( queryset = Size.objects)
  class Meta :
    model = Pizza
    fields = ['topping1', 'topping2', 'Size']
    labels = {'topping1': 'Topping 1', 'topping2': 'Topping 2'}
    
    
class MultiplePizzaForm (forms.Form):
  number = forms.IntegerField(min_value = 2 , max_value = 5 )    