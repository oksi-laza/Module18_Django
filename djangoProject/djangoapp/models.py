from django.db import models
# Каждый класс - это отдельная таблица. Создаем переменную под каждое поле.


# Модели с отношением "один ко многим"
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name    # будет отображаться по умолчанию в БД для пользователя (или в панели администрирования, например)


class Book(models.Model):
    GENRE_CHOICES = [
        ('FIC', 'Fiction'),
        ('NON', 'Non-Fiction'),
        ('SCI', 'Science Fiction'),
        ('FAN', 'Fantasy'),
        ('MYS', 'Mystery'),
        ('THR', 'Thriller'),
        ('ROM', 'Romance'),
        ('HIS', 'Historical'),
    ]    # мы создаем такую переменную в том случае, если хотим чтобы поле было без ввода, только из представленных вариантов. Представили в двух вариантах, в сокращенном виде, для вывода при выборе или в полном виде в панели администрирования, как пример

    title = models.CharField(max_length=200)

    # В поле author есть метод ForeignKey - указывает на связь нашей таблицы Book с таблицей Author - и связь у них один ко многим, один автору может быть связан со многими книгами.
    # 'on_delete=models.CASCADE' - означает, что если удалю автора, то и все книги, связанные с этим автором также удалятся.
    # related_name='books'  - имя, которое будет отображаться пользователем, что связано с этим пользователем? Можно написать любое здесь имя.
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_date = models.DateField()    # поле с вводом даты
    genre = models.CharField(
        max_length=3,
        choices=GENRE_CHOICES,
        default='FIC',
    )    # указываем откуда будут браться значения choices - выбор из ранее созданного списка GENRE_CHOICES, ограничение в три символа - значит будет отобращаться сокращенный вариант жанра, по умолчанию установлен 'FIC'

    def __str__(self):
        return self.title    # пользователю возвращается заголовок. Метод '__str__' не является обязательным


# Модели с отношением "многие ко многим"
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    students = models.ManyToManyField(Student, related_name='courses')
    # 'ManyToManyField' -это указание, что связь "многие ко многим", в аргументах указываем имя таблицы, с которой хотим связать, и предпочтительное имя для отобрадения на сайте и не только(related_name='courses')
    # При связи "многие ко многим" создается дополнительная таблица, благодаря которой реализуется эта связь.
    # С доп. таблицей непосредственно в БД мы не работаем, не изменяем и не удаляем!

    def __str__(self):
        return self.name
