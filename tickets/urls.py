'''
        Project : Ticket System
        Author  : Marco Túlio Castro
        Date    : 24-03-2018
        License : GPL Ver. 3
'''

from django.urls import path

from .views import IndexView
from .auth_views import LoginView, LogoutView
from .forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm

urlpatterns = [
	 path('', IndexView.as_view(), name='index'),  
    path('login',LoginView.as_view(form_class=LoginForm,success_url='./'),name="login"),
    path('logout',LogoutView.as_view(),name="logout"),
]
