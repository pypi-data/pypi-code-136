from django.http import HttpResponse

from django.shortcuts import redirect 

def seidauk_login(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('vizitor:index')
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_func

def login_ona(view_func):
	def wrapper_func(request, *args, **kwargs):
		if not request.user.is_authenticated:
			return redirect('vizitor:index')
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_func


def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):
			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name
			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return redirect('vizitor:index')
				# return HttpResponse("<h1 align='center' style='margin-top:50px'>Ita bo'ot laiha autorizasaun hodi asesu ba iha content refere...! <a href='main/login/'>Fila</a></h1>")

		return wrapper_func
	return decorator
