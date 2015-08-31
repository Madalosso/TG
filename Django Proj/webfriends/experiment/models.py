from django.db import models
from django.contrib.auth.models import User
from registration.models import RegistrationProfile

# Create your models here.
# class UserProfile(models.Model):
# 	nameUser = models.CharField(max_length=30, blank=False, null=True)
# 	usuario = models.OneToOneField(RegistrationProfile)
# 	def __unicode__(self):
# 		return "batata"

class UsuarioFriends(models.Model):
	nickname = models.CharField(max_length=30, blank=False, null = True)
	usuario = models.OneToOneField(User)
	def __unicode__(self):
		return "nome do usuario nick :%s" % self.nickname

class Execution(models.Model):
	request_by = models.ForeignKey(UsuarioFriends)
	date_requisition = models.DateField(auto_now=False, auto_now_add=True)
	status = models.IntegerField()
	def __unicode__(self):
		return "%s at %s"%request_by.nickname, date_requisition