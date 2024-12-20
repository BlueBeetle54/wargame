from django.urls import path
#from django.contrib.auth import views as auth_views
from account.views import MyPasswordResetView, MyPasswordResetConfirmView

from . import views

app_name = 'account'

urlpatterns = [
    path('', views.signin, name='signin'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('password_reset/', MyPasswordResetView.as_view(), name="password_reset"),
    path('password_reset_confirm/<uidb64>/<token>/', MyPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    #path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    #path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    #path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    #path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
