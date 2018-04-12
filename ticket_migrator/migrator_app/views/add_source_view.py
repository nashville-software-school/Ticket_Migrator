from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def addSource(request):
    	"""
		# This view allows a user to add a source repo they can import tickets from
		# Author: Garrett Ward
	    """
    template = loader.get_template('migrator_app/add_source.html')
    
        