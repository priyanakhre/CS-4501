#from django.shortcuts import render
import urllib.request
import urllib.parse
from django.shortcuts import render, Http404
#import requests
import json
#from json import JSONEncoder
#from django.template import loader
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse, HttpRequest
#from django.conf import settings
#from django.core.urlresolvers import reverse
#from django.contrib import messages

#def index(request):
# return HttpResponse("success")
exp_endpoint = 'http://exp-api:8000/api/'

def index(request):
    #data_encoded = urllib.parse.urlencode(data)
    url = urllib.request.Request('http://exp-api:8000/api/index')

    #if data_encoded:
    #   url = data_encoded
    raw = urllib.request.urlopen(url).read().decode('utf-8')
    home_res = json.loads(raw)
    if not home_res['success']:
        return render(request, 'home/error.html')
    else:
        return render(request, 'home/index.html', home_res["data"])


def bet_detail(request, id):
    url = urllib.request.Request('http://exp-api:8000/api/bet/' + id + '/')
    raw = urllib.request.urlopen(url).read().decode('utf-8')
    home_res = json.loads(raw)
    if not home_res['success']:
        return render(request, 'home/error.html')
    else:
        return render(request, 'home/bet_detail.html', home_res["data"])