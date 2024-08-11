from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.shortcuts import redirect , render
from django.contrib.auth import logout as auth_logout
class HomeView(TemplateView):
  template_name = 'home/home.html'
class LoginInterfaceView(LoginView):
  template_name = 'home/login.html'
  form_class = AuthenticationForm  

def signup(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
    else :
      return render(request, 'home/signup.html', {'form': form})
      note = "Access denied please try again "
  else:
    form = UserCreationForm()
    return render(request, 'home/signup.html', {'form': form})

def logout(request):
  auth_logout(request)
  return redirect('home')