__author__ = 'acercado'
from django.conf.urls import url
from . import views

urlpatterns = [
	# url(r'', views.location_accounts, name='location_accounts'),
    url(r'^edit/(?P<pk>[0-9]+)$', views.manage_books, name='manage_books'),
]
