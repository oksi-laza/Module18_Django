from django.shortcuts import render
from django.views.generic import TemplateView    # базовый шаблон, от которого наследуются классы представления


# Create your views here.
def index(request):    # функциональное представление
    return render(request, 'index.html')


# Классовое представление. Удобно тем, что можно в дальнейшем друг от друга наследовать
class index2(TemplateView):    # наследуется от класса django 'TemplateView'
    template_name = 'index2.html'    # 'template_name' - это встроенная переменная. Указываем в ней имя нашего шаблона


