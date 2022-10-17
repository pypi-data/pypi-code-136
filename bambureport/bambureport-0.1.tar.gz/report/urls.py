from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from report import  views


app_name = "report"

urlpatterns = [


    path('report/', views.report, name='report'),
    path('printareabambu/<int:id>', views.printareabambu, name='printareabambu'),
    path('printprefabrika/<int:id>', views.printprefabrika, name='printprefabrika'),
    path('printviveirus/<int:id>', views.printviveirus, name='printviveirus')
    # path('input/informasaun/', views.inputinformasaun, name='inputinformasaun'),
    # path('edit/informasaun/<int:id>', views.editinformasaun, name='editinformasaun'),
    # path('detallu/informasaun/<int:id>', views.detalluinformasaun, name='detalluinformasaun'),
    # path('aoaga/informasaun/imagen/<int:id>', views.apagaimageninformasaun, name='apagaimageninformasaun'),
    # path('set/informasaun/imagen/<int:id>', views.setimageninformasaun, name='setimageninformasaun'),
    # path('delete/informasaun/<int:id>', views.deleteinformasaun, name='deleteinformasaun'),
    # path('detallu/publika/<int:id>', views.detallupublika, name='detallupublika'),
    # path('maneza/konteudu/informasaun/<int:id>', views.manezakonteuduinformasaun, name='manezakonteuduinformasaun'),
    # path('input/konteudu/informasaun/<int:id>/<int:lingua>', views.inputkonteuduinformasaun, name='inputkonteuduinformasaun'),
    # path('edit/konteudu/informasaun/<int:id>/<int:lingua>', views.editkonteuduinformasaun, name='editkonteuduinformasaun'),
    # path('apaga/konteudu/informasaun/<int:id>', views.apagakonteuduinformasaun, name='apagakonteuduinformasaun'),

    
    







    
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
