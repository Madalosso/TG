from django.contrib import admin
from .models import UsuarioFriends, Execution, Algorithms

class UsuarioFriendsAdmin(admin.ModelAdmin):
	fields = ['nickname', 'usuario', 'resultsPerPage']
	list_display = ('nickname', 'usuario', 'date_register', 'last_access', 'resultsPerPage')

class ExecutionAdmin(admin.ModelAdmin):
	fields = ['status','request_by', 'algorithm']
	list_display = ['request_by', 'algorithm', 'time', 'date_requisition', 'status', 'inputFile', 'outputFile']

class AlgAdmin(admin.ModelAdmin):
	fields = ['nameAlg', 'desc', 'command']
	list_display = ['idAlg', 'nameAlg', 'desc']

# class NotesAdmin(admin.ModelAdmin):
# 	fields = ['user', 'execution']
# 	list_display = ['id','user',' executions']

admin.site.register(UsuarioFriends, UsuarioFriendsAdmin)
admin.site.register(Execution, ExecutionAdmin)
admin.site.register(Algorithms, AlgAdmin)
