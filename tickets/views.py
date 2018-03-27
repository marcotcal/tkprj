'''
        Project : Ticket System
        Author  : Marco Túlio Castro
        Date    : 24-03-2018
        License : GPL Ver. 3
'''
from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages

class IndexView(TemplateView):
		template_name = 'index.html'
		
class LoginFormView(FormView):
	template_name='loginform.html'
	form_class=LoginForm


