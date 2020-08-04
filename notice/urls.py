from django.urls import path

from . import views

urlpatterns = [
   path('', views.ListNotice, name='notice'),
   path('<int:N_id>/', views.DetailNotice, name='detail'),
]
