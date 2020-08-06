from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.hashers import check_password
from django.middleware.csrf import get_token
from log.logging import accessLogging,authLogging
from .check import listCheck,scoring
from .models import prob

import json

def ListProb(request):
    probList = listCheck(request.user)
    context = { 'problist' : probList }
    return render(request, 'challenge/listProb.html', context)

@require_POST
def DetailProb(request):
    pk = request.POST.get('pk', None)
    probcon = get_object_or_404(prob, id=pk)
    probData=prob.objects.get(title=probcon)
    context = {
        'title':probData.title,
        'description':probData.description,
        'score':probData.pscore,
        'token':get_token(request),
    }
    if probData.link:
        context['link'] = probData.link
    if probData.file:
        context['file'] = probData.file.url
    print(context)
    if not request.user.is_admin:
        accessLogging(request.user,probData,request.META['REMOTE_ADDR'],request.META['HTTP_USER_AGENT'])
    return HttpResponse(json.dumps(context), content_type="application/json")

def flagProb(request):
    pk = request.POST.get('pk', None)
    probcon = get_object_or_404(prob, id=pk)
    probData=prob.objects.get(title=probcon)
    solve = check_password(request.POST.get('flag', None),probData.flag)
    if not request.user.is_admin:
        if solve:
            scoring(request,probData)
        authLogging(request.user,probData,request.POST.get('flag', None),request.META['REMOTE_ADDR'],request.META['HTTP_USER_AGENT'], solve)
    context = {}
    context['auth'] = solve
    return HttpResponse(json.dumps(context), content_type="application/json")

