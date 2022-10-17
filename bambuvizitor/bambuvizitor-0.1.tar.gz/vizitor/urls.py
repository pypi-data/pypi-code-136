from django.urls import path 

from vizitor import views


app_name = "vizitor"





urlpatterns = [
	path('', views.index, name='index'),
	path('mapa', views.mapa, name='mapa'),
	path('konabaami', views.konabaami, name='konabaami'),
	path('produtu', views.produtu, name='produtu'),
	path('informasaun', views.informasaun, name='informasaun'),
	path('detalluinformasaun/<int:id>', views.detalluinformasaun, name='detalluinformasaun'),
	path('detalluprodutu/<int:id>', views.detalluprodutu, name='detalluprodutu'),
	path('detalluprodutu2', views.detalluprodutu2, name='detalluprodutu2'),
	path('detallumapa/<int:id>', views.detallumapa, name='detallumapa'),
	path('informasaun/grupu/<int:id>', views.informasaungrupu, name='informasaungrupu'),	
]

