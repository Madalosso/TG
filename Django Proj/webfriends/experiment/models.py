from django.db import models
from django.contrib.auth.models import User


class UsuarioFriends(models.Model):
    nickname = models.CharField(max_length=30, blank=False, null=True)
    usuario = models.OneToOneField(User)
    date_register = models.DateTimeField('date_register', auto_now_add=True)
    last_acess = models.DateTimeField('last_acess', auto_now=True)

    def __unicode__(self):
        return self.nickname


class Algorithms(models.Model):
    idAlg = models.AutoField(primary_key=True)
    nameAlg = models.CharField(null=False, blank=False, max_length=100)
    desc = models.CharField(null=True, blank=False, max_length=500)
    command = models.CharField(null=False, blank=False, max_length=100)

    def __unicode__(self):
        return self.nameAlg

class ExecModel(models.Model):
    opt = models.CharField(null=True, max_length=100)
    algorithm = models.ForeignKey(Algorithms, null=True, blank=False)
    inputFile = models.FileField(null=True)
    desc = models.CharField(null=True, blank=False, max_length=500)

    def __unicode__(self):
        return self.algorithm.nameAlg


class Execution(models.Model):
    request_by = models.ForeignKey(UsuarioFriends)
    date_requisition = models.DateTimeField(
        'date_requisition', auto_now_add=True)
    status = models.IntegerField(default=1)
    opt = models.CharField(null=True, max_length=100)
    algorithm = models.ForeignKey(Algorithms, null=True, blank=False)
    inputFile = models.FileField(null=True)
    # outputFile = models.FileField(null=True)
    # infile
    # outfile

    def __unicode__(self):
        return self.request_by.nickname