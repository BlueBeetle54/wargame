from .models import *

def loginLogging(user, ip, agent):
    try :
        saveLog = loginLog(loginUser = user, ipaddr = ip, userAgent = agent)
        saveLog.save()
    except :
        saveLog = None
    return saveLog 

def accessLogging(user, prob, ip, agent):
    try :
        saveLog = probAcessLog(acessUser = user, acessProb = prob, ipaddr = ip, userAgent = agent)
        saveLog.save()
    except :
        saveLog = None
    return saveLog

def authLogging(user, prob, iflag, ip, agent, auth):
    try :
        saveLog = authLog(authUser = user, authProb = prob, flag = iflag, ipaddr = ip, userAgent = agent,is_solved = auth)
        saveLog.save()
    except :
        saveLog = None
    return saveLog
