from django.conf.urls import patterns, url

from quiz import views

urlpatterns = patterns('',
                       url(r'^$', views.get_user_detail,
                           name='get_user_detail'),
                       url(r'^quiz/$', views.quiz, name='quiz'),
                       url(r'^result/$', views.result, name='result'),
                       )
