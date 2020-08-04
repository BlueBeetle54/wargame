from django.contrib import admin
from .models import *

class loginLogAdmin(admin.ModelAdmin):
    readonly_fields = ('loginUser','ipaddr','userAgent','onTime',)
    list_display = ('loginUser', 'ipaddr', 'userAgent','onTime',)
    list_filter = ('ipaddr','loginUser',)

class accessLogAdmin(admin.ModelAdmin):
    readonly_fields = ('acessUser','acessProb','ipaddr','userAgent','onTime',)
    list_display = ('acessUser','acessProb','ipaddr', 'userAgent','onTime',)
    list_filter = ('ipaddr','acessUser',)

admin.site.register(loginLog, loginLogAdmin)
admin.site.register(probAcessLog, accessLogAdmin)