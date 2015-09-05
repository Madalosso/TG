from django.contrib import admin
from .models import UsuarioFriends, Execution, Algorithms

class UsuarioFriendsAdmin(admin.ModelAdmin):
	fields = ['nickname', 'usuario']
	list_display = ('nickname', 'date_register', 'last_acess')

class ExecutionAdmin(admin.ModelAdmin):
	fields = ['status','request_by', 'algorithm', 'opt']
	list_display = ['request_by', 'algorithm', 'opt', 'date_requisition', 'status']

class AlgAdmin(admin.ModelAdmin):
	fields = ['nameAlg', 'desc', 'command']
	list_display = ['idAlg', 'nameAlg', 'desc']

admin.site.register(UsuarioFriends, UsuarioFriendsAdmin)
admin.site.register(Execution, ExecutionAdmin)
admin.site.register(Algorithms, AlgAdmin)
