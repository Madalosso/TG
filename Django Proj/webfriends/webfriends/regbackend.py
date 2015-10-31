# from registration.views import RegistrationView
from registration.backends.default.views import RegistrationView
from experiment.forms import UsuarioFriendsForm
from experiment.models import UsuarioFriends

class MyRegistrationView(RegistrationView):

	form_class = UsuarioFriendsForm

	def register(self,request,form_class):
		new_user = super(MyRegistrationView,self).register(request, form_class)
		user_profile = UsuarioFriends()
		user_profile.usuario = new_user
		user_profile.nickname = form_class.cleaned_data['nickname']
		user_profile.company = form_class.cleaned_data['company']
		user_profile.save()
		return user_profile