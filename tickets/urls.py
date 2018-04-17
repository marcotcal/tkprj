'''
        Project : Ticket System
        Author  : Marco Túlio Castro
        Date    : 24-03-2018
        License : GPL Ver. 3
'''
from django.urls import path

from .views import IndexView, IndexStatusView, TicketList, ShowTicket, CreateTicketMessage, CreateTicket, ChangeTicketStatus
from .auth_views import LoginView, LogoutView
from .forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm

urlpatterns = [
	 
	 path('', IndexView.as_view(), name='index'),  
	 path('<int:days>/<int:status_id>', IndexStatusView.as_view(), name='index_status'),	 

	 path('list/group/<ei_group>/<int:group_id>/<ei_status>/<int:status_id>',TicketList.as_view(),name="list"),
	 path('list/<ei_days>/<int:days>/<ei_group>/<int:group_id>/<ei_status>/<int:status_id>', TicketList.as_view(), name="list_with_status"),
	 
    path('login',LoginView.as_view(form_class=LoginForm,success_url='./'),name="login"),
    path('logout',LogoutView.as_view(),name="logout"),
        
    path('ticket/<int:pk>',ShowTicket.as_view(),name="ticket-detail"),
    path('ticket/add',CreateTicket.as_view(),name="ticket-add"),
    path('ticket/message/add/<ticket_id>',CreateTicketMessage.as_view(),name="ticket-message-add"),
    path('ticket/status/<int:pk>/<int:status_id>',ChangeTicketStatus.as_view(),name="ticket-message-start"),     
]
