from django.contrib import admin
from .models import *
from django.contrib.auth.hashers import make_password, is_password_usable

class probAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not obj.flag[0:21] == 'pbkdf2_sha256$180000$':
            obj.flag = make_password(obj.flag)

        super().save_model(request, obj, form, change)

admin.site.register(prob,probAdmin)
admin.site.register(probTag)
