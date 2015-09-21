from django.contrib import admin
from .models import UsuarioFriends, Execution, Algorithms, ExecModel # Notification

class UsuarioFriendsAdmin(admin.ModelAdmin):
	fields = ['nickname', 'usuario', 'resultsPerPage']
	list_display = ('nickname', 'date_register', 'last_acess', 'resultsPerPage')

class ExecutionAdmin(admin.ModelAdmin):
	fields = ['status','request_by', 'algorithm', 'opt']
	list_display = ['request_by', 'algorithm', 'opt', 'date_requisition', 'status', 'inputFile', 'outputFile']

class AlgAdmin(admin.ModelAdmin):
	fields = ['nameAlg', 'desc', 'command']
	list_display = ['idAlg', 'nameAlg', 'desc']

class PresetsAdmin(admin.ModelAdmin):
	fields = ['algorithm', 'opt', 'inputFile', 'desc']
	list_display = ['algorithm', 'opt', 'inputFile', 'desc']


# class NotesAdmin(admin.ModelAdmin):
# 	fields = ['user', 'execution']
# 	list_display = ['id','user',' executions']

admin.site.register(UsuarioFriends, UsuarioFriendsAdmin)
admin.site.register(Execution, ExecutionAdmin)
admin.site.register(Algorithms, AlgAdmin)
admin.site.register(ExecModel, PresetsAdmin)
# admin.site.register(Notification, NotesAdmin)
