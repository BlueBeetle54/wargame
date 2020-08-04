from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Notice

def ListNotice(request):
    notice_list = Notice.objects.order_by('-date_add')
    context = { 'notice_list' : notice_list}
    return render(request, 'notice/listNotice.html',context)
def DetailNotice(request, N_id):
    notice_con = get_object_or_404(Notice, pk=N_id)
    return render(request, 'notice/detailNotice.html',{'context':notice_con})
