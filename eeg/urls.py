from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from eeg import views

urlpatterns = patterns('',
    
	url(r'^api/$', views.EegList.as_view()),
	url(r'^api/(?P<pk>[0-9]+)/$', views.EegDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)