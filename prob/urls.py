from django.urls import path

from . import views

app_name = 'chall'

urlpatterns = [
   path('', views.ListProb, name='challenge'),
   path('select/', views.DetailProb, name='prob_select'),
   #path('flag/<char:Flag>/'views.flagProb, name='flag_auth'),
]
