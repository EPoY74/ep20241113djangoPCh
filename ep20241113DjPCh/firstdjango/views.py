"""
Представление страниц
Учебный проект
Автор: Евгений Петров
Почта: p174@mail.ru
Урок: https://www.youtube.com/watch?v=KH3eobiFhGA&t=1179s
"""


from django.shortcuts import render
from firstdjango.models import Workers


# Create your views here.
def index_page(request):
    """
    Вывод основной страницы в браузер
    :param request:
    :return:
    """

    all_workers = Workers.objects.all()
    for worker in all_workers:
        print(f"{worker}")
    return render(request, "index.html")
