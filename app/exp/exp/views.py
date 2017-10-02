import json
from django.shortcuts import render
import urllib.request
import urllib.parse
from django.http import HttpResponse, JsonResponse, Http404
from django.conf import settings
from datetime import datetime

models_endpoint = 'http://localhost:8001'

#def index(requests):
#
#	recommended_res = request_get("/youbet/api/bet")
#	active_items = []
#	if recommended_res["success"] != "success":
#		recommended_items = []
#	else:
#		recommended_items = recommended_res["data"]
#	return recommended_items

def index(request):
	#data_encoded = urllib.parse.urlencode(data)
	url = urllib.request.Request('http://models-api:8000/youbet/api/bet/')

	#if data_encoded:
	#	url = data_encoded
	raw = urllib.request.urlopen(url).read().decode('utf-8')
	bets_to_display = json.loads(raw)
	
	if bets_to_display['success'] != True:
		recommended_items=[]
	else:
		recommended_items = bets_to_display["data"]
	return JsonResponse({"success": True, "data": {"recommended_items": 
		recommended_items}})




def get_bet(request, id):
	url = urllib.request.Request('http://models-api:8000/youbet/api/bet/' + id + '/')
	raw = urllib.request.urlopen(url).read().decode('utf-8')
	bet_to_display = json.loads(raw)
	if bet_to_display['success'] != True:
		recommended_items = []
	else:
		recommended_items = bet_to_display['data']
	return JsonResponse({"success": True, "data": {"recommended_items": 
		recommended_items}}) # FIX THIS!!