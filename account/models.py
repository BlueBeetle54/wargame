import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.contrib.auth.signals import user_logged_in
from importlib import import_module


class UserManager(BaseUserManager):

    def create_user(self, uid, nick, email, password = None):
        if not uid:
            raise ValueError('ID is essential')

        user = self.model(
            uid = uid,
            nick = nick,
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using = self._db)
        return user


    def create_superuser(self, uid, nick, email, password):
        user = self.create_user(
            uid = uid,
            nick = nick,
            email = email,
            password = password,
        )

        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)
        return user

class Meta:
    db_table = 'users'
    verbose_name = '유저'
    verbose_name_plural = '유저들'


class User(AbstractBaseUser):
    
    uuid = models.UUIDField(
        primary_key = True,
        unique = True,
        editable = False,
        default = uuid.uuid4,
        verbose_name = 'PK',
    )
    uid = models.CharField(
        max_length = 32,
        unique = True,
        null = False,
        verbose_name = 'ID',
    )
    nick = models.CharField(
        max_length = 20,
        unique = True,
        null = False,
    )
    email = models.EmailField(
        unique = True,
        null = True,
    )
    score = models.IntegerField( default = 0 )
    last_solved = models.DateTimeField( null = True)
    lastIP = models.GenericIPAddressField( protocol = 'IPv4', null = True )
    is_active = models.BooleanField( default = True )
    is_admin = models.BooleanField( default = False )
    is_superuser = models.BooleanField( default = False )
    is_staff = models.BooleanField( default = False )

    objects = UserManager()

    USERNAME_FIELD = 'uid'
    REQUIRED_FIELDS = [
        'nick',
        'email',
    ]

    def __str__(self):
        return self.uid

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, editable = False)
    session_key = models.CharField(max_length = 40, editable = False)
    create_at = models.DateTimeField(auto_now_add = True)

SessionStore = import_module(settings.SESSION_ENGINE).SessionStore

def kicked_my_other_sessions(sender, request, user, **kwargs):
    for user_session in UserSession.objects.filter(user=user):
        session_key = user_session.session_key
        session = SessionStore(session_key)
        session['kicked'] = True
        session.save()
        user_session.delete()

    if not request.session.session_key:
        request.sesseion.create()

    session_key = request.session.session_key
    UserSession.objects.create(user=user, session_key=session_key)

user_logged_in.connect(kicked_my_other_sessions, dispatch_uid='user_logged_in')
