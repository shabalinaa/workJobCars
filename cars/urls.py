from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.table_all, name='table_all'),
    url(r'^car/new/$', views.car_new, name='car_new'),
    url(r'^car/(?P<pk>\d+)/edit/$', views.car_edit, name='car_edit'),
    url(r'^car/delete/(?P<pk>\d+)/$', views.car_delete, name='car_delete'),
]