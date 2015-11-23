from django.db import models
from django.contrib.auth.models import User


class Algorithms(models.Model):
    idAlg = models.AutoField(primary_key=True)
    nameAlg = models.CharField(null=False, blank=False, max_length=100)
    desc = models.CharField(null=True, blank=False, max_length=500)
    command = models.CharField(null=False, blank=False, max_length=100)

    def __unicode__(self):
        return self.nameAlg


class UsuarioFriends(models.Model):
    nickname = models.CharField(
        default='default', max_length=30, blank=False, null=True)
    company = models.CharField(
        default='default', max_length=50, blank=False, null=True)
    usuario = models.OneToOneField(User)
    date_register = models.DateTimeField('date_register', auto_now_add=True)
    last_access = models.DateTimeField('last_access', auto_now=True)
    resultsPerPage = models.IntegerField(default=10)

    def __unicode__(self):
        return self.nickname


def user_directory_path_in(instance, filename):
    return './users/user_{0}/{1}/input'.format(instance.request_by.usuario.id, instance.id)


def user_directory_path_out(instance, filename):
    return './users/user_{0}/{1}/output'.format(instance.request_by.usuario.id, instance.id)


class Execution(models.Model):
    request_by = models.ForeignKey(UsuarioFriends)
    date_requisition = models.DateTimeField(
        'date_requisition', auto_now_add=True)
    status = models.IntegerField(default=1)
    algorithm = models.ForeignKey(Algorithms, null=True, blank=False)
    inputFile = models.FileField(upload_to=user_directory_path_in, null=True)
    outputFile = models.FileField(upload_to=user_directory_path_out, null=True)
    time = models.FloatField(default=-1)

    def __unicode__(self):
        return self.request_by.id  # arrumar
