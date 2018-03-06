from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render

import datetime

def hello(request):
    return HttpResponse("Hello world")

def my_homepage_view(request):
    return HttpResponse("Home Page")

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})

def table(request):
    t = get_template('table.html')
    html = t.render()
    return HttpResponse(html)