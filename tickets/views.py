'''
        Project : Ticket System
        Author  : Marco Tulio Castro
        Date    : 24-03-2018
        License : GPL Ver. 3
'''

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, TicketForm, TicketMessageForm, ChangeTicketStatusForm
from django.views.generic import FormView, RedirectView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile

from django.contrib import messages
from django.contrib.auth.models import Group, User

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView

from .models import Ticket, TicketMessage, TicketStatus, TicketStatusChangeLog
from django.shortcuts import get_object_or_404
from django.urls import reverse

from datetime import datetime, timedelta

##
## Index Views - Shows the groups assigned to the user
## 
class IndexView(TemplateView):
	template_name = "index.html"
	        
	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)		
		return context  	
	
class IndexStatusView(TemplateView):
	template_name = "index_status.html"
	        
	def get_context_data(self, **kwargs):
		context = super(IndexStatusView, self).get_context_data(**kwargs)
		status_id = self.kwargs["status_id"]
		description = TicketStatus.objects.get(pk=status_id).description
		context['status_description'] = description  		
		return context  	

class TicketList(ListView):
	template_name = "list.html"
	model = Ticket 
	context_object_name = "ticket_list"	
	paginate_by = 10
								
	def get_queryset(self):
		filters = {}
		excludes = {}
		
		if "group_id" in self.kwargs:
			if self.kwargs["ei_group"] == 'i':
				filters["group_id"] = self.kwargs["group_id"]
			else:
				excludes["group_id"] = self.kwargs["group_id"]				
		if "status_id" in self.kwargs:
			if self.kwargs["ei_status"] == 'i':				
				filters["status_id"] = self.kwargs["status_id"]
			else:	
				excludes["status_id"] = self.kwargs["status_id"]
		if "days" in self.kwargs:
			if self.kwargs["ei_days"] == 'i':
				filters["creation_time__gte"] = datetime.now() - timedelta(days=self.kwargs["days"])
			else:
				excludes["creation_time__gte"] = datetime.now() - timedelta(days=self.kwargs["days"])
						
		if filters != {} and excludes != {}:										
			tk = Ticket.objects.filter(**filters).exclude(**excludes)
		elif filters == {} and excludes != {}:
			tk = Ticket.objects.exclude(**excludes)
		else:						
			tk = Ticket.objects.filter(**filters)
								
		return tk.order_by("priority","creation_time")
					
	def get_context_data(self, **kwargs):
		context = super(ListView, self).get_context_data(**kwargs)
		if "group_id" in self.kwargs:		
			group_id = str(abs(int(self.kwargs["group_id"])))
			user = self.request.user
		
			users_in_group = Group.objects.get(pk=group_id).user_set.all()		
		
			if user in users_in_group:
				context.update({"valid_group":True})
				name = Group.objects.get(pk=group_id).name									
			else:
				context.update({"valid_group":False})
				name = ""
			context.update({"group_name":name})
		else:							
			context.update({"group_name":""})
			
		return context
	
class ShowTicket(DetailView):
	template_name = "ticket.html"
	model = Ticket
	
	def get_context_data(self, **kwargs):
		context = super(ShowTicket, self).get_context_data(**kwargs)
		context['ticket_messages'] = TicketMessage.objects.filter(ticket=self.kwargs['pk']).order_by('creation_time')
		context['ticket_status_log'] = TicketStatusChangeLog.objects.filter(ticket=self.kwargs['pk']).order_by('log_time')       
		return context	
	
class CreateTicket(CreateView):
	form_class = TicketForm
	template_name = 'ticketform.html'

	def __init__(self):
		self.group_id = None

	def get_initial(self):
		fields = super(CreateTicket, self).get_initial()		
		fields['creation_time'] = datetime.now()
		fields['begin_time'] = None
		fields['close_time'] = None
		fields['status'] = 1
		fields['priority'] = 1
		fields['group'] = self.request.user.groups.all()[0]	 
		fields['user'] = self.request.user
		fields['updated_by'] = self.request.user

		return fields		
					
	def form_valid(self, form):
		self.object = form.save()
		self.group_id = self.object.group.id
		return HttpResponseRedirect(self.get_success_url())					
					
	def get_success_url(self):		
		if self.group_id == None:
			return reverse('index')
		else:			
			return reverse('list',kwargs = {'ei_group':'i','group_id':self.group_id,'ei_status':'e','status_id':6})
			
class CreateTicketMessage(CreateView):
	form_class = TicketMessageForm	
	template_name = 'ticketmessageform.html'
	
	def get_initial(self):
		fields = super(CreateTicketMessage, self).get_initial()
		fields['ticket'] = self.kwargs["ticket_id"]
		fields['creation_time'] = datetime.now()
		fields['user'] = self.request.user

		return fields		
	
	def get_success_url(self):		
		return reverse('ticket-detail',kwargs = {'pk':self.kwargs["ticket_id"]})
		
class ChangeTicketStatus(UpdateView):
	form_class = ChangeTicketStatusForm
	template_name = 'ticketformstatus.html'
	model = Ticket 
	
	def get_initial(self):
			fields = super(ChangeTicketStatus, self).get_initial()
			fields['begin_time'] = datetime.now()			
			fields['status'] = self.kwargs["status_id"]		
			fields['updated_by'] = self.request.user							
			return fields;
			
	def get_form(self, *args, **kwargs):
		form = super(ChangeTicketStatus, self).get_form(*args, **kwargs)
		form.new_status = TicketStatus.objects.get(pk=self.kwargs["status_id"]).description
		form.fields['description'].widget.attrs['readonly'] = True
		form.fields['detailed'].widget.attrs['readonly'] = True
		return form
					
	def get_success_url(self):		
		return reverse('ticket-detail',kwargs = {'pk':self.kwargs["pk"]})	
		
	
