from django.shortcuts import render
from django.http import HttpResponse
from account.models import User

def ListRank(request):
    rank_list = User.objects.order_by('-score','-last_solved')
    user_list = []
    for user in rank_list:
        if not user.is_admin:
            user_list += [user]
    context = { 'rank_list' : user_list}
    return render(request, 'rank/listRank.html', context)
