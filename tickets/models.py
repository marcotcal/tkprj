'''
	Project	: Ticket System
	Author 	: Marco Túlio Castro
	Date 	: 26-03-2018
	License	: GPL Ver. 3

	Notes	: You must create the database witha schema tickets before migrate
'''
from django.db import models


class TicketPriority(models.Model):
	
	description = models.CharField(max_length=50)
	display_order = models.PositiveIntegerField()

	class Meta:
		db_table = '"tickets"."ticket_priority"'
		ordering = (['display_order'])

class TicketType(models.Model):
	
	description = models.CharField(max_length=50)
	display_order = models.PositiveIntegerField()

	class Meta:
		db_table = '"tickets"."ticket_type"'
		ordering = (['display_order'])

class TicketStatus(models.Model):
	
	description = models.CharField(max_length=50)
	display_order = models.PositiveIntegerField()

	class Meta:
		db_table = '"tickets"."ticket_status"'
		ordering = (['display_order'])

class Client(models.Model):

	client_name = models.CharField(max_length=100)
	is_active = models.BooleanField()
	logo = models.BinaryField()

	class Meta:
		db_table = '"tickets"."client"'
		ordering = (['client_name'])

class User(models.Model):
	
	user_login = models.CharField(max_length=20)
	user_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	client = models.ForeignKey(Client, on_delete=models.PROTECT)

	def __str__(self):
		return "{} {}".format(self.user_name, self.last_name)
	
	class Meta:
		db_table = '"tickets"."user"'
		ordering = (['user_name','last_name'])

class Ticket(models.Model):

	creation_time = models.DateTimeField()
	begin_time = models.DateTimeField()
	close_time = models.DateTimeField()
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	description = models.CharField(max_length=50)
	detailed = models.TextField()
	status = models.ForeignKey(TicketStatus, on_delete=models.PROTECT)
	priority = models.ForeignKey(TicketPriority, on_delete=models.PROTECT)
	ticket_type = models.ForeignKey(TicketType, on_delete=models.PROTECT)
	
	class Meta:
		db_table = '"tickets"."ticket"'
		ordering = (['creation_time'])

class TicketMessage(models.Model):
	
	ticket = models.ForeignKey(Ticket, on_delete=models.PROTECT)
	creation_time = models.DateTimeField()
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	message = models.TextField() 

	class Meta:
		db_table = '"tickets"."ticket_message"'
		ordering = (['creation_time'])


