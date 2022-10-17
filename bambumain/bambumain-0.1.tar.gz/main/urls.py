from django.urls import path , include

from main import views


app_name = "main"




urlpatterns = [

    path("set_language/<str:user_language>/", views.set_language_from_url, name="set_language_from_url"),
	path('main', views.index, name='main'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.index, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('painel/', views.painel, name='painel'),
    path('userperfil/', views.userperfil, name='userperfil')
    

]