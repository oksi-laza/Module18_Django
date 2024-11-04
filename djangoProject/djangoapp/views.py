from django.shortcuts import render, redirect
from django.views.generic import TemplateView    # базовый шаблон, от которого наследуются классы представления
from django.http import HttpResponse    # для возврата HTTP-ответа пользователю
from .forms import ContactForm    # импортировали нужный класс для создания объекта формы. Если файл находится в той же директории приложения, то перед названием файла ставим точку.


# Пояснение к функции ниже:
# 'request.GET' - реагирование на запрос GET от пользователя. А '.get' - это специальный метод получения информации.
# В скобках - первое - параметр, второе - его значение по умолчанию
# Вся информация с GET-запроса отображается в браузерной строке (в отличие от POST-запроса), например, так:
# 'http://127.0.0.1:8000/func_response/?name=Join&age27' после знака вопроса указываются переменная и её значение (при GET-запросе)
def func_response(request):
    name = request.GET.get('name', 'Guest')
    age = request.GET.get('age', '27')
    return HttpResponse(f'Hello, {name} {age}!')


# Пояснение к функции ниже:
# 'request.POST' - скрывает информацию, не показывает ее в адресной строке браузера
# Если request.metod=POST (метод указан в форме, в которую пользователь будет вводить информацию
# (в данном примере это в шаблоне 'simple_post.html'). При этом методе указываем шифрование - (у нас это в Django или везде?) - {% csrf_token %} - смотреть наш шаблон.
# ТО мы обрабатываем сообщение через 'request.POST' - достаем информацию о сообщение, которое пользователь передал
# в форме (при этом в браузерной строке этой информации видно не будет). Параметр указываем 'message', значение будет то, что введет пользователь.
# возвращаем пользователю HTTP-ответ, указали, что это будет его же сообщение.
# Последняя строчка функции (это как else, то есть если метод 'GET' - пользователь просто обновил страницу по этому пути
# - то генерируем шаблон пользователю, чтобы он мог ввести сообщение в какую-то строку или форму.
def simple_post(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        return HttpResponse(f'You said: {message}')
    return render(request, 'simple_post.html')


# HTTP-ответ может быть в таком формате, вне зависимости от вида запроса 'POST' или 'GET'.
# Пользователь получает шаблон или информацию сразу же, как попадает на соответствующую страницу.
# def example(request):
#     return HttpResponse('Hello!')


# Можно пользователю вывести ответ или шаблон, а нам вернуть статус запроса и указать причину, если статус запроса, который мы ожидали.
# Статус с ошибкой это 400.
# reason - это указание причины, по которой произошла ошибкa. Так можно отследить, в каком месте произошел сбой,
# а пользователю при этом вывести какое-то сообщение на экран. Нам же в консоль будет сообщение об ошибке и в какой функции это произошло.
# Это можно использовать с помощью условий внутри наших функций.
def example(request):
    return HttpResponse('Hello!', status=400, reason='Error')


# Функция по обработке отправки формы на сервер от пользователя,
# а также получение формы пользователем
def form_post(request):
    if request.method == 'POST':
        # Получаем данные
        name = request.POST.get('name')    # в скобках название параметра - это то название в файле html, которое указано в поле 'name'
        email = request.POST.get('email')    # в скобках название параметра - это то название в файле html, которое указано в поле 'name'
        message = request.POST.get('message')    # в скобках название параметра - это то название в файле html, которое указано в поле 'name'
        subscribe = request.POST.get('subscribe') == 'on'    # в скобках название параметра - это то название в файле html, которое указано в поле 'name'. Проверяем параметр 'on' - был ли нажат чекбокс.

        # Проверим выводом в консоли, что данные, отправленные пользователем, обработаны и получены сервером (проверка для себя)
        print(f'Name: {name}')
        print(f'Email: {email}')
        print(f'Message: {message}')
        print(f'Subscribe: {subscribe}')

        # Http-ответ пользователю
        return HttpResponse('Форма успешно отправлена')

    # Если это GET
    return render(request, 'form_post_in_html.html')


# Форма Django
# Eсли запрос 'POST', то форма будет объектом класса 'ContactForm' с обработкой данных через 'request.POST'.
# Иначе (если запрос 'GET' - ничего не отправлялось в форме), то будет отображение пустой формы.
def form_post_django(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():    # проверка формы на валидацию (доп.параметр, но желательно его применять)
            # Обработка данных формы
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subscribe = form.cleaned_data['subscribe']    # Если нажат, то True
            # Дальнейшая логика (например, отправка email)

            # Проверим выводом в консоли, что данные, отправленные пользователем, обработаны и получены сервером (проверка для себя)
            print(f'Name: {name}')
            print(f'Email: {email}')
            print(f'Message: {message}')
            print(f'Subscribe: {subscribe}')
            return HttpResponse('Форма успешно отправлена!')
    else:
        form = ContactForm()
    return render(request, 'form_post_in_django.html', {'form': form})


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
