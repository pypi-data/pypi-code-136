from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from informasaun import  views


app_name = "informasaun"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('perfil/', views.perfil, name='perfil'),
    path('input/perfil/', views.inputperfil, name='inputperfil'),
    path('edit/perfil/<int:id>', views.editperfil, name='editperfil'),
    # path('delete/grupubambu/<int:id>', views.deletegrupubambu, name='deletegrupubambu'),
    path('maneza/konteuduperfil/<int:id>', views.manezakonteuduperfil, name='manezakonteuduperfil'),
    path('input/konteuduperfil/<int:id>/<int:lingua>', views.inputkonteuduperfil, name='inputkonteuduperfil'),
    path('edit/konteuduperfil/<int:id>/<int:lingua>', views.editkonteuduperfil, name='editkonteuduperfil'),
    path('delete/perfil/<int:id>', views.deleteperfil, name='deleteperfil'),
    path('apaga/konteudu/perfil/<int:id>', views.apagakonteuduperfil, name='apagakonteuduperfil'),
    # path('input/konteudu/perfil/<int:id>/<int:lingua>', views.inputkonteuduperfil, name='inputkonteuduperfil'),




    path('informasaun/', views.informasaun, name='informasaun'),
    path('input/informasaun/', views.inputinformasaun, name='inputinformasaun'),
    path('edit/informasaun/<int:id>', views.editinformasaun, name='editinformasaun'),
    path('detallu/informasaun/<int:id>', views.detalluinformasaun, name='detalluinformasaun'),
    path('aoaga/informasaun/imagen/<int:id>', views.apagaimageninformasaun, name='apagaimageninformasaun'),
    path('set/informasaun/imagen/<int:id>', views.setimageninformasaun, name='setimageninformasaun'),
    path('delete/informasaun/<int:id>', views.deleteinformasaun, name='deleteinformasaun'),
    path('detallu/publika/<int:id>', views.detallupublika, name='detallupublika'),
    path('maneza/konteudu/informasaun/<int:id>', views.manezakonteuduinformasaun, name='manezakonteuduinformasaun'),

    path('input/konteudu/informasaun/<int:id>/<int:lingua>', views.inputkonteuduinformasaun, name='inputkonteuduinformasaun'),
    path('edit/konteudu/informasaun/<int:id>/<int:lingua>', views.editkonteuduinformasaun, name='editkonteuduinformasaun'),
    path('apaga/konteudu/informasaun/<int:id>', views.apagakonteuduinformasaun, name='apagakonteuduinformasaun'),

    

    path('produtu/', views.produtu, name='produtu'),
    path('input/produtu/', views.inputprodutu, name='inputprodutu'),
    path('edit/produtu/<int:id>', views.editprodutu, name='editprodutu'),
    path('maneza/konteudu/produtu/<int:id>', views.manezakonteuduprodutu, name='manezakonteuduprodutu'),
    path('input/konteudu/produtu/<int:id>/<int:lingua>', views.inputkonteuduprodutu, name='inputkonteuduprodutu'),
    path('edit/konteudu/produtu/<int:id>/<int:lingua>', views.editkonteuduprodutu, name='editkonteuduprodutu'),
    path('apaga/konteudu/produtu/<int:id>', views.apagakonteuduprodutu, name='apagakonteuduprodutu'),
    path('set/produtu/imagen/<int:id>', views.setimagenprodutu, name='setimagenprodutu'),
    path('apaga/produtu/imagen/<int:id>', views.apagaimagenprodutu, name='apagaimagenprodutu'),




    path('parceiru/', views.parceiru, name='parceiru'),
    path('input/parceiru/', views.inputparceiru, name='inputparceiru'),
    path('edit/parceiru/<int:id>/', views.editparceiru, name='editparceiru'),
    path('delete/parceiru/<int:id>', views.deleteparceiru, name='deleteparceiru'),



    
    # path('grupuviveirus/', views.grupuviveirus, name='grupuviveirus'),
    # path('input/grupuviveirus/', views.inputgrupuviveirus , name='inputgrupuviveirus'),
    # path('edit/grupuviveirus/<int:id>', views.editgrupuviveirus, name='editgrupuviveirus'),
    # path('delete/grupuviveirus/<int:id>', views.deletegrupuviveirus, name='deletegrupuviveirus'),
    # path('delete/detallugrupuviveirus/<int:id>', views.detallugrupuviveirus, name='detallugrupuviveirus'),



    # path('areabambu/', views.areabambu, name='areabambu'),
    # path('input/areabambu/', views.inputareabambu , name='inputareabambu'),
    # path('edit/areabambu/<int:id>', views.editareabambu, name='editareabambu'),
    # path('delete/areabambu/<int:id>', views.deleteareabambu, name='deleteareabambu'),
    # path('detallu/areabambu/<int:id>', views.detalluareabambu, name='detalluareabambu'),





    
    # path('atualizadokumentu/<int:pk>/', views.atualizadokumentu, name = 'atualizadokumentu'),
    # path('dokumentudetallu/<int:pk>/', views.dokumentudetallu, name = 'dokumentudetallu'),




    # path('dashboard/', views.dashboard, name='dashboard'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
