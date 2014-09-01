from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^ajax/', views.indexAjax, name='indexajax'),
    url(r'^$', views.index, name='home'),
)