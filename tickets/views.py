'''
        Project : Ticket System
        Author  : Marco Túlio Castro
        Date    : 24-03-2018
        License : GPL Ver. 3
'''
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, TicketForm, TicketMessageForm
from django.views.generic import FormView, RedirectView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile

from django.contrib import messages
from django.contrib.auth.models import Group, User

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView

from .models import Ticket, TicketMessage
from django.shortcuts import get_object_or_404
from django.urls import reverse

import datetime

class TicketList(ListView):
	template_name = "list.html"
	model = Ticket 
	context_object_name = "ticket_list"	
	paginate_by = 10
								
	def get_queryset(self):			 	
		return Ticket.objects.filter(group=self.kwargs["group_id"]).order_by("priority","creation_time")					
					
	def get_context_data(self, **kwargs):
		context = super(ListView, self).get_context_data(**kwargs)
		group_id	= self.kwargs["group_id"]
		user = self.request.user
		
		users_in_group = Group.objects.get(pk=group_id).user_set.all()		
		
		if user in users_in_group:
			context.update({"valid_group":True})
			name = Group.objects.get(pk=group_id).name									
		else:
			context.update({"valid_group":False})
			name = ""
									
		context.update({"group_name":name})
		return context

class IndexView(TemplateView):
	template_name = "index.html"
	        
	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)		
		return context  	
	
class ShowTicket(DetailView):
	template_name = "ticket.html"
	model = Ticket
	
	def get_context_data(self, **kwargs):
		context = super(ShowTicket, self).get_context_data(**kwargs)
		context['ticket_messages'] = TicketMessage.objects.filter(ticket=self.kwargs['pk']).order_by('creation_time')        
		return context	
	
class CreateTicket(CreateView):
	form_class = TicketForm
	template_name = 'ticketform.html'

	def __init__(self):
		self.group_id = None

	def get_initial(self):
		fields = super(CreateTicket, self).get_initial()		
		fields['creation_time'] = datetime.datetime.now()
		fields['begin_time'] = None
		fields['close_time'] = None
		fields['status'] = 1
		fields['priority'] = 1
		fields['group'] = self.request.user.groups.all()[0]	 
		fields['user'] = self.request.user

		return fields		
					
	def form_valid(self, form):
		self.object = form.save()
		self.group_id = self.object.group.id
		return HttpResponseRedirect(self.get_success_url())					
					
	def get_success_url(self):		
		return reverse('list',kwargs = {'group_id':self.group_id})
			
class CreateTicketMessage(CreateView):
	form_class = TicketMessageForm	
	template_name = 'ticketmessageform.html'
	
	def get_initial(self):
		fields = super(CreateTicketMessage, self).get_initial()
		fields['ticket'] = self.kwargs["ticket_id"]
		fields['creation_time'] = datetime.datetime.now()
		fields['user'] = self.request.user

		return fields		
	
	def get_success_url(self):		
		return reverse('ticket-detail',kwargs = {'pk':self.kwargs["ticket_id"]})
		
	