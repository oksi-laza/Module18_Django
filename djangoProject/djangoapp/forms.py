from django import forms


class ContactForm(forms.Form):    # создаем класс формы, которая наследуется от класса 'forms.Form' - в нем есть все необходимые поля, укажем только нужные нам
    name = forms.CharField(max_length=100, label='Введите ваше имя:')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')    # 'widget=forms.Textarea' - чтобы поле было для больших сообщений (поле для комментария), а не просто строка
    subscribe = forms.BooleanField(required=False, label='Подписаться на рассылку')    # 'required=False' - по умолчанию, галочки нет
