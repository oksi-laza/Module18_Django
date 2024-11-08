"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from djangoapp.views import index, index2, file_static, func_response, simple_post, example
from djangoapp.views import form_post, form_post_django, data_from_model, test
# from djangoapp.views import *    # можно доставать все функции из views, а не перечислять, как у меня выше
from django.views.generic import TemplateView    # при классовом представлении (класс 'index2') в путях к названию отображаемого класса применяем метод 'as_view'



urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('index2/', index2.as_view()),
    path('index3/', TemplateView.as_view(template_name='index3.html')),
    path('', file_static),
    path('func_response/', func_response),
    path('simple_post/', simple_post),
    path('example/', example),
    path('form_post/', form_post),
    path('form_post2/', form_post_django),
    path('data_from_model/', data_from_model),
    path('test/', test),
]
