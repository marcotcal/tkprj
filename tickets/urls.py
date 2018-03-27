'''
        Project : Ticket System
        Author  : Marco Túlio Castro
        Date    : 24-03-2018
        License : GPL Ver. 3
'''

from django.urls import path

from .views import IndexView, LoginFormView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('', LoginFormView.as_view(), name='login'),
]
