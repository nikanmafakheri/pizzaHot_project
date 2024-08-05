from django.urls import path
from . import views

urlpatterns = [
  path('', views.order,name = 'order'),
  path('pizzas', views.pizzas,name ='pizzas'),
  path('<int:pk>', views.edit_order,name ='edit'),

]
