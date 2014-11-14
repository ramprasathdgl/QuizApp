from django.conf.urls import patterns, url

from quiz import views

urlpatterns = patterns('',
                       url(r'^index$', views.index, name='index'),
                       url(r'^next/$', views.next, name='next'),
                       url(r'^$', views.get_user_detail,
                           name='get_user_detail'),
                       )
