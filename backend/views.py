from django.shortcuts import render
from django.http import HttpResponse
from prob.models import prob

def index(request):
    content = "개발중인 서버입니다."
    return render(request, 'index.html',{'content': content})

def beforeStart(request):
    return render(request, 'before.html')

def download(requset,prob_id):
    loadProb = prob.objects.get(id=prob_id)
    response = HttpResponse()
    response["Content-Disposition"] = "attachment; filename=[0]".format(prob.pretty_name)
    response['X-Accel-Redirect'] = "/protected/{0}".format(prob.file.name)
    return response

from django.conf import settings
from django.contrib.auth.signals import user_logged_in
from django.db import models
from importlib import import_module

SessionStore = import_module(settings.SESSION_ENGINE).SessionStore

def kicked_my_other_sessions(sender, request, user, **kwargs):
    for user_session in UserSession.objects.filter(user=user):
        session_key = user_session.session_key
        session = SessionStore(session_key)
        session.delete()

    session_key = request.session.session_key
    UserSession.objects.create(user=user, session_key=session_key)

user_logged_in.connect(kicked_my_other_sessions, dispatch_uid='user_logged_in')
