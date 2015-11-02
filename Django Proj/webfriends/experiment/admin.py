from django.contrib import admin
from .models import UsuarioFriends, Execution, Algorithms, ExecModel

class UsuarioFriendsAdmin(admin.ModelAdmin):
	fields = ['nickname', 'usuario', 'resultsPerPage', 'notes']
	list_display = ('nickname', 'register_date', 'last_access', 'resultsPerPage')

class ExecutionAdmin(admin.ModelAdmin):
	fields = ['status','request_by', 'algorithm', 'opt']
	list_display = ['request_by', 'algorithm', 'time', 'date_requisition', 'status', 'inputFile', 'outputFile']

class AlgAdmin(admin.ModelAdmin):
	fields = ['nameAlg', 'desc', 'command']
	list_display = ['idAlg', 'nameAlg', 'desc']

class PresetsAdmin(admin.ModelAdmin):
	fields = ['algorithm', 'opt', 'inputFile', 'desc']
	list_display = ['algorithm', 'opt', 'inputFile', 'desc']

admin.site.register(UsuarioFriends, UsuarioFriendsAdmin)
admin.site.register(Execution, ExecutionAdmin)
admin.site.register(Algorithms, AlgAdmin)
admin.site.register(ExecModel, PresetsAdmin)
