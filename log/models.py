from django.db import models
from account.models import User
from prob.models import prob

class loginLog(models.Model):
    loginUser = models.ForeignKey(User, on_delete=models.CASCADE)
    ipaddr = models.GenericIPAddressField(protocol='IPv4', null=True)
    userAgent = models.CharField(max_length=500)
    onTime = models.DateTimeField(auto_now_add=True)


class downloadLog(models.Model):
    downloadUser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    downloadProb = models.ForeignKey(prob, on_delete=models.CASCADE)
    ipaddr = models.GenericIPAddressField(protocol='IPv4', null=True)
    userAgent = models.CharField(max_length=500)
    onTime = models.DateTimeField(auto_now_add=True)

class probAcessLog(models.Model):
    acessUser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    acessProb = models.ForeignKey(prob, on_delete=models.CASCADE)
    ipaddr = models.GenericIPAddressField(protocol='IPv4', null=True)
    userAgent = models.CharField(max_length=500)
    onTime = models.DateTimeField(auto_now_add=True)

class authLog(models.Model):
    authUser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    authProb = models.ForeignKey(prob, on_delete=models.CASCADE)
    flag = models.CharField(max_length=300, null=True)
    ipaddr = models.GenericIPAddressField(protocol='IPv4', null=True)
    userAgent = models.CharField(max_length=500)
    is_solved = models.BooleanField(default=False)
    onTime = models.DateTimeField(auto_now_add=True)



