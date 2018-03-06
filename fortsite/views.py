from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render

import datetime
import urllib, json

JSON_URL = "https://raw.githubusercontent.com/jasmeet17/sample-json/master/codebeautify.json"

def table(request):
    json = load_json(JSON_URL)
    search = ''
    if(request.GET.get('mybtn')):
        search = request.GET.get('search_box')
    else:
        search =''
    return render(request, 'table.html', {'json': json, 'search':search})

def load_json(json_url):
    response = urllib.urlopen(json_url)
    data = json.loads(response.read())
    return data