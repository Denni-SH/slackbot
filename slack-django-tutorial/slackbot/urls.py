from django.conf.urls import url
from django.contrib.auth import views as proj_views
from . import views

urlpatterns = [
    url(r'^$', views.TeamsListView.as_view(), name='TeamsList'),
    url(r'^oauth/$', views.slack_oauth),
    url(r'^message/$', views.post_message),
    url(r'^event/$', views.thread_event),
    url(r'^statistic/(?P<slug>[-_\w\d]+)$', views.statistic, name='Statistic'),
    url(r'^settings/(?P<slug>[-_\w\d]+)$', views.Settings.as_view(), name='Settings'),
]