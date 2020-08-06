from .models import *
from log.models import authLog
from account.models import User



def logCheck(user):
    solveList = []
    authList = authLog.objects.filter(authUser=user)
    for auth in authList:
        if auth.is_solved:
            if not auth.authProb in solveList:
                solveList += [auth.authProb]
    return solveList

def listCheck(user):
    tag_list = probTag.objects.order_by('id')
    solvedList = logCheck(user)
    prob_list = []
    if tag_list:
        for tag in tag_list:
            if tag.prob_1st:
                if tag.prob_1st.is_active:
                    prob_list += prob.objects.filter(title=tag.prob_1st)
            if tag.prob_1st in solvedList and tag.prob_2nd:
                if tag.prob_2nd.is_active:
                    prob_list += prob.objects.filter(title=tag.prob_2nd)
            if tag.prob_2nd in solvedList and tag.prob_3rd:
                if tag.prob_3rd.is_active:
                    prob_list += prob.objects.filter(title=tag.prob_3rd)
            if tag.prob_3rd in solvedList and tag.prob_4th:
                if tag.prob_4th.is_active:
                    prob_list += prob.objects.filter(title=tag.prob_4th)
            if tag.prob_4th in solvedList and tag.prob_5th:
                if tag.prob_5th.is_active:
                    prob_list += prob.objects.filter(title=tag.prob_5th)
    if prob_list:
        return prob_list
    else:
        return False

def scoring(request, prob):
    if not request.user.is_admin:
        if not prob in logCheck(request.user):
            userinfo = User.objects.get(uid=request.user)
            userinfo.score += prob.pscore
            if prob.break_thru:
                userinfo.score += prob.break_thru
                prob.break_thru -= 1
                prob.save()
            userinfo.save()
