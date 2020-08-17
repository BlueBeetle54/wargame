from django.db import models
from account.models import User

import uuid

'''
class probManager(models.Manager):
    def setData(self, flag, **kwargs):
        if not is_password_usable(flag):
            flag = make_password(flag)
'''

class prob(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True})
    link = models.URLField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    date_add = models.DateTimeField(auto_now_add=True)
    pscore = models.IntegerField()
    tag = models.ForeignKey('probTag', on_delete=models.CASCADE, null = True)
    flag = models.CharField(max_length=100)
    break_thru = models.IntegerField(default=0, null=False)
    is_active = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.title

    @property
    def pretty_name(self):
        return "{0}.{1}".format(slugify(self.title),get_extension(self.file.name))

class probTag(models.Model):
    title = models.CharField(max_length=150)
    prob_1st = models.ForeignKey(prob, on_delete=models.CASCADE, blank = True, null=True, related_name='prob_1st_50')
    prob_2nd = models.ForeignKey(prob, on_delete=models.CASCADE, blank = True, null=True, related_name='prob_2nd_100')
    prob_3rd = models.ForeignKey(prob, on_delete=models.CASCADE, blank = True, null=True, related_name='prob_3rd_150')
    prob_4th = models.ForeignKey(prob, on_delete=models.CASCADE, blank = True, null=True, related_name='prob_4th_200')
    prob_5th = models.ForeignKey(prob, on_delete=models.CASCADE, blank = True, null=True, related_name='prob_5th_300')

    def __str__(self):
        return self.title

