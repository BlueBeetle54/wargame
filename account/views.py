from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy


def signin(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        form = LoginForm(request.POST)
        uid = request.POST['uid']
        password = request.POST['password']
        client_ip = request.META['REMOTE_ADDR']
        user = authenticate(uid = uid, password = password)
        if user is not None:
            login(request, user)
            user.lastIP = client_ip
            user.save()
            return redirect('index')
        else:
            return HttpResponse('Login Failed')
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('index')

class MyPasswordResetView(PasswordResetView):
    success_url = reverse_lazy('login')
    template_name = 'account/password_reset_form.html'
    email_template_name = 'account/password_reset.html'

    def form_valid(self, form):
        messages.info(self.request, '암호 변경 메일 발송')
        return super().form_volid(form)

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('login')
    #template_name = 'account/password_reset_confirm.html'

    def form_valid(self, form):
        messages.info(self.request, '암호 변경 완료')
        return super().form_volid(form)
    
