from .models import *

class loginLogging:
    def logging(user, ip, agent):
        try :
            saveLog = loginLog(loginUser = user, ipaddr = ip, userAgent = agent)
            saveLog.save()
        except :
            saveLog = None
        return saveLog 

class accessLogging:
    def logging(user, prob, ip, agent):
        try :
            saveLog = probAcessLog(acessUser = user, acessProb = prob, ipaddr = ip, userAgent = agent)
            saveLog.save()
        except :
            saveLog = None
        return saveLog
