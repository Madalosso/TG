from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class UserProfile(models.Model):
# 	nameUser = models.CharField(max_length=30, blank=False, null=True)
# 	usuario = models.OneToOneField(RegistrationProfile)
# 	def __unicode__(self):
# 		return "batata"


class UsuarioFriends(models.Model):
    nickname = models.CharField(max_length=30, blank=False, null=True)
    usuario = models.OneToOneField(User)
    date_register = models.DateTimeField('date_register', auto_now_add=True)
    last_acess = models.DateTimeField('last_acess', auto_now=True)
    def __unicode__(self):
        return self.nickname


class Execution(models.Model):
    request_by = models.ForeignKey(UsuarioFriends)
    date_requisition = models.DateField('date_requisition', auto_now_add=True)
    status = models.IntegerField()

    def __unicode__(self):
        return self.request_by.nickname
