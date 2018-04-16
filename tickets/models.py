'''
	Project	: Ticket System
	Author 	: Marco Túlio Castro
	Date 	: 26-03-2018
	License	: GPL Ver. 3

	Notes	: You must create the database witha schema tickets before migrate
'''
from django.db import models
from django.contrib.auth.models import Group, User
from django.utils.translation import gettext as _


class TicketPriority(models.Model):
	
	description = models.CharField(max_length=50, verbose_name=_("Description"))
	display_order = models.PositiveIntegerField()
	
	def __str__(self):
		return self.description

	class Meta:
		db_table = '"tickets"."ticket_priority"'
		ordering = (['display_order'])

class TicketType(models.Model):
	
	description = models.CharField(max_length=50, verbose_name=_("Description"))
	display_order = models.PositiveIntegerField()

	def __str__(self):
		return self.description

	class Meta:
		db_table = '"tickets"."ticket_type"'
		ordering = (['display_order'])

class TicketStatus(models.Model):
	
	description = models.CharField(max_length=50, verbose_name=_("Description"))
	display_order = models.PositiveIntegerField()
	
	def __str__(self):
		return self.description

	class Meta:
		db_table = '"tickets"."ticket_status"'
		ordering = (['display_order'])

class Ticket(models.Model):

	creation_time = models.DateTimeField(verbose_name=_("Creation Time"))
	begin_time = models.DateTimeField(null=True, verbose_name=_("Begin Time"))
	close_time = models.DateTimeField(null=True, verbose_name=_("Close Time"))
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
	group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name=_("Group"))	
	description = models.CharField(max_length=50, verbose_name=_("Description"))
	detailed = models.TextField(verbose_name=_("Detailed Description"))
	status = models.ForeignKey(TicketStatus, on_delete=models.PROTECT,verbose_name=_("State"))
	priority = models.ForeignKey(TicketPriority, on_delete=models.PROTECT, verbose_name=_("Priority"))
	ticket_type = models.ForeignKey(TicketType, on_delete=models.PROTECT, verbose_name=_("Ticket Type"))
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='update_user', verbose_name=_("User"))
	
	class Meta:
		db_table = '"tickets"."ticket"'
		ordering = (['creation_time'])

class TicketMessage(models.Model):
	
	ticket = models.ForeignKey(Ticket, on_delete=models.PROTECT)
	creation_time = models.DateTimeField()	
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	message = models.TextField() 

	class Meta:
		db_table = '"tickets"."ticket_message"'
		ordering = (['creation_time'])
		
class TicketStatusChangeLog(models.Model):
	ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
	log_time = models.DateTimeField()	
	status_from = models.ForeignKey(TicketStatus, related_name='status_status_from', on_delete=models.PROTECT,verbose_name=_("State"))
	status_to = models.ForeignKey(TicketStatus, related_name='status_status_to', on_delete=models.PROTECT,verbose_name=_("State"))
	user = models.ForeignKey(User, on_delete=models.CASCADE) 	

	class Meta:
		db_table = '"tickets"."ticket_change_log"'
		ordering = (['log_time'])
