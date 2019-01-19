from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.table_all, name='table_all'),
    url(r'^car/new/$', views.car_new, name='car_new'),
    url(r'^car/(?P<pk>\d+)/edit/$', views.car_edit, name='car_edit'),
    url(r'^car/delete/(?P<pk>\d+)/$', views.car_delete, name='car_delete'),
    url(r'^driver/new/$', views.driver_new, name='driver_new'),
    url(r'^driver/(?P<pk>\d+)/edit/$', views.driver_edit, name='driver_edit'),
    url(r'^driver/delete/(?P<pk>\d+)/$', views.driver_delete, name='driver_delete'),
    url(r'^crew/new/$', views.crew_new, name='crew_new'),
    url(r'^crew/(?P<pk>\d+)/edit/$', views.crew_edit, name='crew_edit'),
    url(r'^crew/delete/(?P<pk>\d+)/$', views.crew_delete, name='crew_delete'),
]