from django.views.generic import TemplateView
# def home(request):
#   return render(request , 'home/home.html',{})

class HomeView(TemplateView):
  template_name = 'home/home.html'
  

