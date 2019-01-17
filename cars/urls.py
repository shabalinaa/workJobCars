from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.table_all, name='table_all')
]