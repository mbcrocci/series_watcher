from django.conf.urls import patterns, url

from tracker import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<serie_id>\d+)/$',
                           views.details, name='details'),

                       url(
                           r'^(?P<serie_id>\d+)/(?P<season_id>\d+)/$',
                           views.episode, name='episode'),
                       )
