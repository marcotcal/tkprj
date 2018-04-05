'''
        Project : Ticket System
        Author  : Marco Túlio Castro
        Date    : 24-03-2018
        License : GPL Ver. 3
'''

from django.urls import path

from .views import IndexView, TicketList, ShowTicket, CreateTicketMessage, CreateTicket
from .auth_views import LoginView, LogoutView
from .forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm

urlpatterns = [
	 path('', IndexView.as_view(), name='index'),  
    path('login',LoginView.as_view(form_class=LoginForm,success_url='./'),name="login"),
    path('logout',LogoutView.as_view(),name="logout"),
    path('list/group/<group_id>',TicketList.as_view(),name="list"),    
    path('ticket/<int:pk>',ShowTicket.as_view(),name="ticket-detail"),
    path('ticket/add',CreateTicket.as_view(),name="ticket-add"),
    path('ticket/message/add/<ticket_id>',CreateTicketMessage.as_view(),name="ticket-message-add"), 
]
