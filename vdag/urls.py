from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^api/addPPP/', views.addPPP, name='addPPP'),
	url(r'^api/addTurnover', views.addTurnover, name='addTurnover'),
	url(r'^api/addShotChart', views.addShotChart, name='addShotChart'),
	url(r'^api/addTimeLine', views.addTimeLine, name='addTimeLine'),
	url(r'^api/addDefense', views.addDefense, name='addDefense'),
	url(r'^api/addBoxScore', views.addBoxScore, name='addBoxScore'),
]
