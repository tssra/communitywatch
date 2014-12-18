from django.conf.urls import patterns, url
from mainapp import views

urlpatterns = patterns('',
	url(r'^senti/$', views.senti, name='senti'),
	url(r'^$', views.index, name='index'),
)
