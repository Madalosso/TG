from django.contrib import admin
from .models import UsuarioFriends, Execution

class UsuarioFriendsAdmin(admin.ModelAdmin):
	fields = ['nickname', 'usuario']
	list_display = ('nickname', 'date_register', 'last_acess')

class ExecutionAdmin(admin.ModelAdmin):
	fields = ['status','request_by']
	list_display = ['request_by', 'date_requisition', 'status']

admin.site.register(UsuarioFriends, UsuarioFriendsAdmin)
admin.site.register(Execution, ExecutionAdmin)
