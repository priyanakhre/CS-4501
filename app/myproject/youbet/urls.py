from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    #USER CR
    url(r'^api/user/$', views.user_Create_GetAll), #Url to get all users, or create user
    url(r'^api/bet/$', views.bet_Create_GetAll),  #URL to all bets or create one 
    url(r'^api/response/$', views.response_Create_GetAll),    
    url(r'^api/user/(?P<user_id>[0-9]+)/$', views.user_get_update_delete),
    url(r'^api/bet/(?P<bet_id>[0-9]+)/$', views.bet_get_update_delete),
    url(r'^api/response/(?P<response_id>[0-9]+)/$', views.response_get_update_delete),
    # url(r'^api/responses/(?P<bet_id>[0-9]+)/$', views.getResponsesForBet),
]