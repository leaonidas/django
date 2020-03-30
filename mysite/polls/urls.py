from django.urls import path

from . import views

"""
path() has four arguments, two required and two optional

Required:
	route: 
		string that contains url pattern
		when processing a request starts at first pattern
		and makes it down the list until it finds one that
		matches

	view:
		when it finds a matching pattern, calls the specified
		view with and HttpRequest object

Optional:
	kwargs:
		arbitrary keyword arguments can be passed in a
		dictionary to get the target view

	name:
		naming urls allows to refer to it unambiguosly from
		elsewhere in Django
"""

urlpatterns = [
	path('', views.index, name='index')
]