from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from mapa import  views


app_name = "mapa"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('grupubambu/', views.grupubambu, name='grupubambu'),
    path('input/grupubambu/', views.inputgrupubambu, name='inputgrupubambu'),
    path('edit/grupubambu/<int:id>', views.editgrupubambu, name='editgrupubambu'),
    path('delete/grupubambu/<int:id>', views.deletegrupubambu, name='deletegrupubambu'),
    path('delete/detallugrupubambu/<int:id>', views.detallugrupubambu, name='detallugrupubambu'),
    path('rejistu/importasaunbambu/<int:id>', views.rejistuimportasaunbambu, name='rejistuimportasaunbambu'),
    path('input/importasaunbambu/<int:id>', views.inputimportasaunbambu, name='inputimportasaunbambu'),
    path('edit/importasaungrupubambu/<int:id>', views.editimportasaungrupubambu, name='editimportasaungrupubambu'),
    path('delete/importasaungrupubambu/<int:id>', views.deleteimportasaungrupubambu, name='deleteimportasaungrupubambu'),






    
    path('grupuviveirus/', views.grupuviveirus, name='grupuviveirus'),
    path('input/grupuviveirus/', views.inputgrupuviveirus , name='inputgrupuviveirus'),
    path('edit/grupuviveirus/<int:id>', views.editgrupuviveirus, name='editgrupuviveirus'),
    path('delete/grupuviveirus/<int:id>', views.deletegrupuviveirus, name='deletegrupuviveirus'),
    path('delete/detallugrupuviveirus/<int:id>', views.detallugrupuviveirus, name='detallugrupuviveirus'),



    path('areabambu/', views.areabambu, name='areabambu'),
    path('input/areabambu/', views.inputareabambu , name='inputareabambu'),
    path('edit/areabambu/<int:id>', views.editareabambu, name='editareabambu'),
    path('delete/areabambu/<int:id>', views.deleteareabambu, name='deleteareabambu'),
    path('detallu/areabambu/<int:id>', views.detalluareabambu, name='detalluareabambu'),





    
    # path('atualizadokumentu/<int:pk>/', views.atualizadokumentu, name = 'atualizadokumentu'),
    # path('dokumentudetallu/<int:pk>/', views.dokumentudetallu, name = 'dokumentudetallu'),




    # path('dashboard/', views.dashboard, name='dashboard'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
