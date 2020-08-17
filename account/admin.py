from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User, UserSession

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    
    readonly_fields = ('score',)
    list_display = ('uid', 'nick', 'last_login', 'lastIP', 'last_solved', 'score')
    list_filter = ()

    fieldsets = (
        (None, {'fields' : ('uid', 'password', 'nick', 'email', 'score')}),
        ('Permissions', {'fields' : ('is_active', 'is_admin', 'is_superuser', 'is_staff')}),
    )

    add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': ('uid', 'password', 'nick', 'email', 'score', 'is_active')}
            ),
        )

    search_fields = ('uid', 'nick')
    ordering = ('uid',)
    filter_horizontal = ()

class MstSessionAdmin(admin.ModelAdmin):
    readonly_fields = ('user','session_key','create_at',)

    fieldsets = [
        ('sessionkey', {'fields' : ('user', 'session_key', 'create_at')}),
    ]
    list_display = ('user','session_key','create_at',)
    search_fields = ('user',)
    ordering = ('user',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
#admin.site.register(User)
admin.site.register(UserSession, MstSessionAdmin)
admin.site.unregister(Group)
