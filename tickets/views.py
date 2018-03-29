'''
        Project : Ticket System
        Author  : Marco Túlio Castro
        Date    : 24-03-2018
        License : GPL Ver. 3
'''
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm
from django.views.generic import FormView, RedirectView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.views.generic.base import TemplateView
from django.contrib import messages

class IndexView(TemplateView):
		template_name = 'index.html'
		def __init__(self):
			self.teste_var = 'Isto é um teste'
        
		def get_context_data(self, **kwargs):
			context = super(IndexView, self).get_context_data(**kwargs)
			context.update({'teste_var': self.teste_var})
			return context  	
