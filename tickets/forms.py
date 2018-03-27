'''
        Project : Ticket System
        Author  : Marco Túlio Castro
        Date    : 24-03-2018
        License : GPL Ver. 3
'''
from __future__ import unicode_literals

from django import forms
from django.forms.formsets import BaseFormSet, formset_factory


class LoginForm(forms.Form):
	user = forms.CharField(required=True, label='User')
	password = forms.CharField(widget=forms.PasswordInput(), required=True, label='Password')
	 
