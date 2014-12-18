from django.conf.urls import patterns, url
from mainapp import views

urlpatterns = patterns('',
	url(r'^senti/$', views.senti, name='senti'),
	url(r'^story/(?P<storyid>\d+)/$', views.show_story, name='story'),
	url(r'^$', views.index, name='index'),
	url(r'^login/', views.login, name='login'),
	url(r'^logout/', views.logout, name='logout'),
)
