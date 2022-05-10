from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    print(Student.objects.all())
    context = {'students': Student.objects.all()}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)

def teachers_list(request, id):
    context={'student': Student.objects.get(id=id)}

    template = 'school/teachers_list.html'
    return render(request, template, context)
