from django.conf.urls import url
from usuario.views import RegistrarUsuarioView
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
	url(r'^admin/registrar/$', RegistrarUsuarioView.as_view(), name='registrar'),
	url(r'^admin/login/$', login, {'template_name':'login.html'}, name='login'),
    url(r'^admin/logout/$', logout_then_login, {'login_url':'/admin/login/'}, name='logout')
]

	



	