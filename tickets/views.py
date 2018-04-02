'''
        Project : Ticket System
        Author  : Marco Túlio Castro
        Date    : 24-03-2018
        License : GPL Ver. 3
'''
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, TicketForm
from django.views.generic import FormView, RedirectView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .models import Ticket
from django.shortcuts import get_object_or_404

class TicketList(ListView):
	template_name = 'list.html'
	model = Ticket 
	context_object_name = "ticket_list"	
	paginate_by = 5
								
	def get_queryset(self):			 	
		return Ticket.objects.filter(group=self.kwargs['group_id']).order_by('priority','creation_time')					
					
	def get_context_data(self, **kwargs):
		context = super(ListView, self).get_context_data(**kwargs)
		group_id	= self.kwargs['group_id']
		user = self.request.user
		
		users_in_group = Group.objects.get(pk=group_id).user_set.all()		
		
		if user in users_in_group:
			context.update({"valid_group":True})
			name = Group.objects.get(pk=group_id).name									
		else:
			context.update({"valid_group":False})
			name = ""
									
		context.update({'group_name':name})
		return context

class IndexView(TemplateView):
	template_name = 'index.html'
	        
	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)		
		return context  	
	
		
	