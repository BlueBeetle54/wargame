from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from log.logging import accessLogging
from .check import listCheck
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
    #probcon = get_object_or_404(prob, title="test")
    probData=prob.objects.get(title=probcon)
    context = {
        'title':probData.title,
        'description':probData.description,
        'score':probData.pscore,
    }
    if probData.link:
        context['link'] = probData.link
    if probData.file:
        context['file'] = probData.file
    accessLogging.logging(request.user,probData,request.META['REMOTE_ADDR'],request.META['HTTP_USER_AGENT'])
    return HttpResponse(json.dumps(context), content_type="application/json")

#def flagProb(requset):

