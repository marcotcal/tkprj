from .models import Ticket, TicketMessage, TicketStatus, TicketStatusChangeLog
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
from datetime import datetime, timedelta
from django.utils.translation import gettext as _

@receiver(post_save, sender=Ticket)
def create_ticket(sender, instance, created, **kwargs):
	if created:
		# generate email for the support team		
		mail_to = [settings.DEFAULT_FROM_EMAIL]
		mail_from = settings.DEFAULT_FROM_EMAIL
						
		message = _("The ticket ") + instance.description + \
					 _(" was created by ") + instance.user.username + " : " + instance.group.name +  _(" at ") + datetime.now().strftime("%d-%m-%Y %H:%M")
		message += "\n"
		message += instance.detailed			
		send_mail(_("Ticket created") + " : " + instance.description , message, mail_from, mail_to, fail_silently=False)
		
	
	
	
