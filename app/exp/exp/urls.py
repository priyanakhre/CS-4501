"""exp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/index/$', views.index, name='index'),
    # Bets

    #url(r'^api/bets/$', views.get_all_bets, name='get_all_bets'),
    url(r'^api/bet/(?P<id>[0-9]+)/$', views.get_bet, name='get_bet'),
    #url(r'^api/bets/recently_posted/$', views.get_recently_posted_bets, name='get_recently_posted_bets'),
]
