# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
#Views for Students
def students_list(request):
    students = (
    { 'id': 4,
    'first_name': u' Андрій',
    'last_name': u'Корост',
    'tickets': 235,
    'image': 'img/guppi.jpg'
  },
      { 'id': 2,
      'first_name': u' Оленка',
      'last_name': u'Шеремета',
      'tickets': 239,
      'image': 'img/mouse.jpg'
    },
    { 'id': 5,
    'first_name': u'Олеська',
    'last_name': u'Сорока',
    'tickets': 237,
    'image': 'img/hart.jpg'
  },
    )
    return render(request, 'students/students_list.html', { 'students': students }
    )

def students_add(request):
    return HttpResponse('<h1>Students Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' %sid)
#Views for Groups
