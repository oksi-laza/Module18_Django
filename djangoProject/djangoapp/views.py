from django.shortcuts import render
from django.views.generic import TemplateView    # базовый шаблон, от которого наследуются классы представления


# Create your views here.
def index(request):    # функциональное представление
    title_h1 = 'Заголовок первого уровня'    # у нас есть некоторая переменная, которую мы передаем в context
    text = 'В этой переменной мы указали некоторый текст'
    list_in_context = ['Я первый в списке', 'Я второй в списке', 'Я третий в списке']
    list_number = [25.1, 1.86, 5.3]
    len_list_number = len(list_number)
    context = {
        'title_h1': title_h1,
        'text': text,
        'list_in_context': list_in_context,
        'list_number': list_number,
        'len_list_number': len_list_number
    }    # ключ к переменной для меньшей путаницы должен носить название переменной, по ключу будем передавать данные в html-шаблон, данные будут браться из переменной, которая указана в значении к этому ключу (в html-шаблоне указываем двойные фигурные скобки {{ title_h1 }})
    return render(request, 'index.html', context)    # контекст передаем в функцию рендер


# Классовое представление. Удобно тем, что можно в дальнейшем друг от друга наследовать
class index2(TemplateView):    # наследуется от класса django 'TemplateView'
    template_name = 'index2.html'    # 'template_name' - это встроенная переменная. Указываем в ней имя нашего шаблона


def file_static(request):
    return render(request, 'file_static.html')
