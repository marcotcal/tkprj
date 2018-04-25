'''
        Project : Ticket System
        Author  : Marco Tulio Castro
        Date    : 24-03-2018
        License : GPL Ver. 3
'''
from __future__ import unicode_literals
from django import forms
from django.forms import ModelForm
from django.forms.formsets import BaseFormSet, formset_factory
from django.contrib.auth import authenticate
from django.utils.translation import gettext as _
from .models import Ticket, TicketMessage
import logging

class LoginForm(forms.Form):
	username = forms.CharField(required=True, label=_('User Name'))
	password = forms.CharField(widget=forms.PasswordInput(), required=True, label=_('Password'))
	user = None
	def get_user(self):
		return self.user   	

	def clean(self):      
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')   
		self.user = authenticate(username=username, password=password)	 
		if not self.user or not self.user.is_active:
			raise forms.ValidationError(_("Sorry, that login was invalid. Please try again."))
			return self.cleaned_data
			
class TicketForm(ModelForm):
	
	class Meta:
		model = Ticket
		fields = ["id","creation_time","group","user","status","priority","ticket_type","description","detailed","updated_by"]
		widgets = {			
			'creation_time' : forms.HiddenInput,
			'status': forms.HiddenInput,
			'user' : forms.HiddenInput,
			'updated_by' : forms.HiddenInput,				
		}				

class ChangeTicketStatusForm(ModelForm):
	
	new_status = "teste" 	
		
	class Meta:
		model = Ticket
		fields = ["id","status","description","detailed","updated_by"]
		widgets = {							 							
			'status' : forms.HiddenInput, 	
			'updated_by' : forms.HiddenInput,	
		}			
		
		
class TicketMessageForm(ModelForm):
	
	class Meta:
		model = TicketMessage
		fields = "__all__"
		widgets = {
			'ticket': forms.HiddenInput,
			'creation_time' : forms.HiddenInput,
			'user' : forms.HiddenInput,		
		}		
			
		
