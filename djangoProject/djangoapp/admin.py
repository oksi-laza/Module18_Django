from django.contrib import admin
from .models import Category, News   # импортируем модели, которые будем администрировать
# Админ-панель позволяет нам изменяь данные, не используя код - регистрировать сами модели,
# добавлять туда объекты, изменять их и так далее. Очень удобно для администрирования сайта,
# добавлять туда какой-то контент, его удалять и модерировать.
# Чтобы попасть в панель администрирования, нужно зарегистрировать администратора.


# Админка для модели Category
@admin.register(Category)    # в декораторе указываем нашу модель
class CategoryAdmin(admin.ModelAdmin):    # назовем класс с названием, отражающем нашу модель Category. 'list_display' - обязательное поле
    list_display = ('name',)    # Поля для отображения в списке (в виде кортежа), можно указывать из модели не все поля, можно все или часть
    search_fields = ('name',)    # Поля для поиска (в виде кортежа)


@admin.register(News)    # в декораторе указываем нашу модель
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_ad', 'is_published')    # Поля для отображения в списке
    list_filter = ('category', 'is_published')    # Фильтрация по категории и статусу публикации
    search_fields = ('title', 'content')    # Поля для поиска
    list_per_page = 10    # Количество новостей на странице

    # Разделение полей на секции. None - это поля, которые не нужно разбивать на секции
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'category')
        }),
        ('Дополнительные настройки', {
            'classes': ('collapse',),    # Скрытие секции по умолчанию - если указали 'classes': ('collapse',) - в последний раз не сработало
            'fields': ('is_published', 'created_ad', 'updated_ad')
        }),
    )

    # Поля только для ЧТЕНИЯ - указываем те, которые нельзя редактировать
    readonly_fields = ('created_ad', 'updated_ad')
