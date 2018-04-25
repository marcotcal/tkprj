from django.apps import AppConfig
from django.db.models.signals import post_migrate
from tickets.db_partition_triggers import create_partition_triggers

class TicketsConfig(AppConfig):
	name = 'tickets'
	verbose_name = 'Tickets'
	
	def ready(self):
		import tickets.signals
		post_migrate.connect(create_partition_triggers, sender=self)
		