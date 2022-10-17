from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# from population.models import Population,DetailFamily,Family,Religion,Profession,Citizen,Aldeia,Village,User,Migration,Death,Migrationout,Temporary,ChangeFamily
# from population.utils import getnewidp,getnewidf
# from population.forms import Family_form,Family_form,FamilyPosition,Population_form,DetailFamily_form,CustumDetailFamily_form,Death_form,Migration_form,Migrationout_form,Changefamily_form
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone

from django.core.paginator import Paginator

# from mapa.forms import *
# from custom.utils import getnewid, getjustnewid, hash_md5, getlastid
from django.db.models import Count
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Q
from datetime import date
from django.http import JsonResponse
# from employee.models import *
# from datetime import datetime, timedelta
# from vizitor.forms import CustomAuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from mapa.models import *
from mapa.forms import *
from informasaun.models import *
from informasaun.forms import *
from django.contrib.auth.models import User
from jeral.utils import getlastid
from main.decorators import login_ona, seidauk_login, allowed_users




@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def produtu(request):
    buka = False
    bukatitle = "mamuk"
    if request.GET.__contains__('page') :
        page_num = request.GET.get('page')
    else:
        page_num = 1
    if request.GET.__contains__('pesquiza'):
        buka = True
        paginator = Paginator(KonteuduProdutu.objects.order_by('-id').filter(titulu__icontains=request.GET['pesquiza']), 1)

    else:
        paginator = Paginator(KonteuduProdutu.objects.order_by('-id'), 10)

    page_range = []
    for i in range(paginator.num_pages):
        page_range.append(i+1)
        data_Produtu = paginator.page(page_num)
        page_num_int = int(page_num)

    if buka :
        bukatitle = "Rezultadu Pesquiza husi <i>' (" + request.GET['pesquiza'] + ") '</i>"

    data = []
    lingua = Lingua.objects.all()
    titulu = ""
    for dadosinfo in data_Produtu :
        statuslingua = ""
        for dadoslingua in lingua : 
            konteudu = KonteuduProdutu.objects.filter(produtu = dadosinfo.produtu.id , lingua = dadoslingua.id).count()
            if konteudu > 0 :
                konteudu = KonteuduProdutu.objects.filter(produtu = dadosinfo.produtu.id , lingua = dadoslingua.id).last()
                # konteudu2 = KonteuduInformasaun.objects.filter(informasaun = dadosinfo.id , lingua = 1).last()
                titulu = konteudu.titulu
                statuslingua = statuslingua +  " <i><b>   <img src=" +dadoslingua.icon.url + " width='20px'> &nbsp; </b> </i> " + konteudu.titulu + "<br>"
            else :
                statuslingua = statuslingua +  "<i><b>   <img src=" +dadoslingua.icon.url + " width='20px'> &nbsp; </b> </i>  <font color ='red'> Laiha</font> <br>"
        data.append({'foun' : dadosinfo.produtu.foun,'presu' : dadosinfo.produtu.presu, 'kategoriaprodutu' : dadosinfo.produtu.kategoriaprodutu, 'imagen' : dadosinfo.produtu.imagen_main ,'lingua':dadoslingua.naran,'linguaicon' : dadoslingua.icon,'linguaid' : dadoslingua.id, 'statuslingua': statuslingua , 'data' : dadosinfo.produtu.data ,'titulu' : titulu , "id" : dadosinfo.produtu.id })


    context = {
        "pajina_produtu" : "active",
        "produtu" : data,
        'bukatitle' : bukatitle,
        'page_range' : page_range,
        'current_page' : page_num_int,
    }
    return render(request, 'informasaun/produtu/lista.html',context)




@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def inputprodutu(request):

    dataagora = timezone.now()
    if request.method == 'POST':
        hashed = getlastid(KonteuduProdutu)
        forms = KonteuduProdutuForm(request.POST)
        forms2 = ProdutuForm(request.POST)


        if forms.is_valid() &  forms2.is_valid():

            instance2 = forms2.save(commit=False)
            instance2.presu = request.POST['presu']
            instance2.kategoriaprodutu = KategoriaProdutu.objects.get(id = request.POST['kategoriaprodutu'])
            instance2.id = hashed[0]
            instance2.data = request.POST['data_produsaun']
            instance2.date_created = dataagora
            instance2.user_created = User.objects.get(id = request.user.id)
            instance2.save()


            instance = forms.save(commit=False)
            instance.produtu = Produtu.objects.get(id=hashed[0])
            # instance.id = hashed[0]
            # instance.hashed = hashed[1] 
            instance.save()
            messages.success(request,"Dados Rejistu  ho Susessu..!")
            return redirect('informasaun:produtu')


    produtuform = KonteuduProdutuForm()
    produtuform2 = ProdutuForm()
    context = {
        "asaun" : "input",
        "pajina_produtu" : "active",
        # "dokumentu" : dokumentu,
        "pajina_titulu" : "Rejistu Perfil",
        "button" : "Rejistu",
        "forms" : produtuform,
        "forms2" : produtuform2
    }
    return render(request, 'informasaun/produtu/input.html',context)




@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def editprodutu(request, id):

    konteuduprodutu = KonteuduProdutu.objects.get(id = id)
    produtu = Produtu.objects.get(id = konteuduprodutu.produtu.id)

    dataagora = timezone.now()
    if request.method == 'POST':

        forms = KonteuduProdutuForm(request.POST , instance = konteuduprodutu)
        forms2 = ProdutuForm(request.POST , instance = produtu)


        if forms.is_valid() &  forms2.is_valid():

            instance2 = forms2.save(commit=False)
            instance2.data = request.POST['data_produsaun']
            instance2.save()


            instance = forms.save(commit=False)
            # instance.id = hashed[0]
            # instance.hashed = hashed[1] 
            instance.save()
            messages.success(request,"Dados Rejistu  ho Susessu..!")
            return redirect('informasaun:produtu')


    produtuform = KonteuduProdutuForm(instance = konteuduprodutu)
    produtuform2 = ProdutuForm( instance = produtu)

    context = {
        "asaun" : "edit",
        "pajina_produtu" : "active",
        # "dokumentu" : dokumentu,
        "pajina_titulu" : "Rejistu Perfil",
        "button" : "Rejistu",
        "forms" : produtuform,
        "forms2" : produtuform2
    }
    return render(request, 'informasaun/produtu/input.html',context)


# def editinformasaun(request,id):
#     informasaun = Informasaun.objects.get(id=id)
#     if request.method == 'POST':
#         forms = InformasaunForm(request.POST, instance=informasaun)
#         if forms.is_valid():
#             instance = forms.save(commit=False)
#             instance.save()
#             messages.success(request,"Dados Rejistu  ho Susessu..!")
#             return redirect('informasaun:informasaun')

#     informasaunform = InformasaunForm(instance = informasaun)
#     context = {
#         "asaun" : "input",
#         "pajina_informasaun" : "active",
#         # "dokumentu" : dokumentu,
#         "pajina_titulu" : "Rejistu Perfil",
#         "button" : "Rejistu",
#         "forms" : informasaunform,
#     }
#     return render(request, 'informasaun/informasaun/input.html',context)



# def detalluinformasaun(request,id):
#     imageinformasaun =  ImagenInformasaun.objects.filter(informasaun = id)
#     forms = ImagenInformasaunForm()
#     informasaun = Informasaun.objects.filter(id = id)
#     mainimagen = Informasaun.objects.get(id = id)

#     lingua = Lingua.objects.all()
#     imagen = ImagenInformasaun.objects.filter(informasaun = id)

#     # data = []

#     # for dados in imagen.iterator() :
#     #     statuslingua = ""
#     #     for dados2 in lingua.iterator() :
#     #         konteudu = KonteuduImagenInformasaun.objects.filter(imageinformasaun = dados.id , lingua = dados2.id).count()
#     #         if konteudu > 0 :
#     #             statuslingua = "Lingua :  " + str(dados2.naran) + " <font color ='red'>Laiha</fonr> <br>"
#     #         else :
#     #             konteudu = KonteuduImagenInformasaun.objects.filter(imageinformasaun = dados.id , lingua = dados2.id)
#     #             statuslingua = "Lingua :  " +  str(konteudu.deskrisaun) + "<br>"

#     #     data.append({'imagen' : dados.imagen ,'lingua':dados2.naran,'linguaicon' : dados2.icon,'linguaid' : dados.id, 'status': 'laiha' , 'data' : "Mamuk" ,'titulu' : "Mamuk" , "id" : int(id) })



#     if request.method == 'POST':
#         forms = ImagenInformasaunForm(request.POST, request.FILES)
#         if forms.is_valid():
#             instance = forms.save(commit=False)
#             instance.informasaun = Informasaun.objects.get(id=id)
#             instance.save()
#             messages.success(request,"Dadus Rejistu  ho Susessu..!")
#             return redirect('informasaun:detalluinformasaun', id = id)



#     context = {
#         "asaun" : "input",
#         "pajina_informasaun" : "active",
#         "mainimagen" : mainimagen.imagen_main,
#         "forms" : forms,
#         "informasaun" : informasaun,
#         "imageinformasaun" : imageinformasaun,
#         "pajina_titulu" : "Rejistu Perfil",
#         "button" : "Rejistu",
#         "id" : id,
#     }
#     return render(request, 'informasaun/informasaun/detallu.html',context)




@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def manezakonteuduprodutu(request,id):

    #konteudu lingua 

    konteuduprodutu =  KonteuduProdutu.objects.filter(produtu = id)
    lingua = Lingua.objects.all()
    data = []

    for dados in lingua.iterator() :
        konteudu = KonteuduProdutu.objects.filter(lingua=dados.id,produtu = id).count()
        if konteudu > 0 :
            konteudu = KonteuduProdutu.objects.filter(lingua=dados.id,produtu = id).last()
            data.append({'lingua':dados.naran,'linguaicon' : dados.icon,'linguaid' : dados.id,  'status': 'iha' , 'data' : konteudu.data_produsaun,'titulu' : konteudu.titulu , "id" : konteudu.id })
        else :
            data.append({'lingua':dados.naran,'linguaicon' : dados.icon,'linguaid' : dados.id, 'status': 'laiha' , 'data' : "Mamuk" ,'titulu' : "Mamuk" , "id" : int(id) })

    #konteudu imagen

    imagenprodutu =  ImagenProdutu.objects.filter(produtu = id)
    forms = ImagenProdutuForm()
    produtu = Produtu.objects.filter(id = id)
    mainimagen = Produtu.objects.get(id = id)
    lingua = Lingua.objects.all()
    imagen = ImagenProdutu.objects.filter(produtu = id)


    if request.method == 'POST':
        forms = ImagenProdutuForm(request.POST, request.FILES)
        if forms.is_valid():
            instance = forms.save(commit=False)
            instance.produtu = Produtu.objects.get(id=id)
            instance.save()
            messages.success(request,"Dadus Rejistu  ho Susessu..!")
            return redirect('informasaun:manezakonteuduprodutu', id = id)

    context = {
        "asaun" : "input",
        "pajina_produtu" : "active",
        "konteuduprodutu" : data,
        "pajina_titulu" : "Maneza Konteudu",
        "button" : "Rejistu",
        "id" : id,

        "mainimagen" : mainimagen.imagen_main,
        "forms" : forms,
        "produtu" : produtu,
        "imagenprodutu" : imagenprodutu,


    }
    return render(request, 'informasaun/produtu/manezakonteudu.html',context)


@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def inputkonteuduprodutu(request,id,lingua):
    if request.method == 'POST':
        hashed = getlastid(KonteuduProdutu)
        forms = KonteuduProdutuForm(request.POST)
        if forms.is_valid():
   
            instance = forms.save(commit=False)
            instance.produtu = Produtu.objects.get(id = id)
            instance.lingua = Lingua.objects.get(id=lingua)
            # instance.id = hashed[0]
            # instance.hashed = hashed[1]
            Produtu.objects.filter(pk=id).update(data=request.POST['data_produsaun']) 
            instance.save()
            messages.success(request,"dados Rejistu  ho Susessu..!")
            return redirect('informasaun:manezakonteuduprodutu' , id =  id)

    konteuduprodutuform = KonteuduProdutuForm()
    context = {
        "asaun" : "input",
        "pajina_produtu" : "active",
        # "dokumentu" : dokumentu,
        "pajina_titulu" : "Rejistu Perfil",
        "button" : "Rejistu",
        "forms" : konteuduprodutuform,
    }
    return render(request, 'informasaun/produtu/inputkonteuduprodutu.html',context)




@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def editkonteuduprodutu(request,id,lingua):
    konteuduprodutu = KonteuduProdutu.objects.get(id=id, lingua = lingua)


    if request.method == 'POST':
        hashed = getlastid(KonteuduProdutu)
        forms = KonteuduProdutuForm2(request.POST, instance = konteuduprodutu)


        if forms.is_valid():
            instance = forms.save(commit=False)
            # instance.id = hashed[0]
            # instance.hashed = hashed[1] 
            instance.lingua = Lingua.objects.get(id=lingua)
            instance.save()
            hilifoun = ''
            if request.POST.__contains__('foun') :
                hilifoun = True
            else :
                hilifoun =False

            Produtu.objects.filter(pk=konteuduprodutu.produtu.id).update(data=request.POST['data_produsaun'], kategoriaprodutu = request.POST['kategoria'], foun = hilifoun , presu= request.POST['presu']) 
            messages.success(request,"dados Rejistu  ho Susessu..!")
            return redirect('informasaun:manezakonteuduprodutu' , id =  konteuduprodutu.produtu.id)

    konteuduprodutuform = KonteuduProdutuForm2(instance = konteuduprodutu)
    context = {
        "asaun" : "edit",
        "pajina_produtu" : "active",
        # "dokumentu" : dokumentu,
        "pajina_titulu" : "Atualiza Konteudu",
        "button" : "Atualiza",
        "foun"  : konteuduprodutu.produtu.foun,
        "presu"  : konteuduprodutu.produtu.presu,
        "forms" : konteuduprodutuform,
    }
    return render(request, 'informasaun/informasaun/inputkonteuduinformasaun.html',context)


@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def apagakonteuduprodutu(request,id):

    konteudu = Produtu.objects.get(id=id)
    konteudu.delete()
    messages.success(request,"Dados Apaga  Susessu..!")
    return redirect('informasaun:produtu')




@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def apagaimagenprodutu(request,id):
    imagen = ImagenProdutu.objects.get(id=id)
    idprod = imagen.produtu.id
    imagen.delete()
    messages.success(request,"Dados Apaga  Susessu..!")
    return redirect('informasaun:manezakonteuduprodutu', id = idprod)





# def detallupublika(request,id):
#     imageinformasaun =  ImagenInformasaun.objects.filter(informasaun = id)
#     informasaun = Informasaun.objects.filter(id = id)
#     context = {
#         "asaun" : "input",
#         "pajina_informasaun" : "active",
#         "forms" : forms,
#         "informasaun" : informasaun,
#         "imageinformasaun" : imageinformasaun,
#         "pajina_titulu" : "Rejistu Perfil",
#         "button" : "Rejistu",
#     }
#     return render(request, 'informasaun/informasaun/detallupublika.html',context)




# def apagaimageninformasaun(request,id):
#     imagen = ImagenInformasaun.objects.get(id=id)
#     idinfo = imagen.informasaun.id
#     imagen.delete()
#     messages.success(request,"Dados Apaga  Susessu..!")
#     return redirect('informasaun:manezakonteuduinformasaun', id = idinfo)





@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def setimagenprodutu(request,id):
    imagen = ImagenProdutu.objects.get(id=id)
    Produtu.objects.filter(pk=imagen.produtu.id).update(imagen_main=str(imagen.imagen))
    idinfo = imagen.produtu.id
    messages.success(request,"Imagen set  Susessu..!")
    return redirect('informasaun:manezakonteuduprodutu', id = idinfo)









# def inputkonteuduperfil(request, id):
#     pajina = Pajina.objects.get(id=id)
#     if request.method == 'POST':
#         forms = KonteuduPajinaForm(request.POST,request.FILES)
#         if forms.is_valid():
#             instance = forms.save(commit=False)
#             instance.pajina = pajina
#             instance.save()
#             messages.success(request,"Dados Rejistu  ho Susessu..!")
#             return redirect('informasaun:manezakonteuduperfil', id = id)


#     konteudupajinaform = KonteuduPajinaForm()
#     context = {
#         "asaun" : "input",
#         "pajina_perfil" : "active",
#         # "dokumentu" : dokumentu,
#         "pajina_titulu" : "Rejistu Perfil",
#         "button" : "Rejistu",
#         "forms" : konteudupajinaform,
#     }
#     return render(request,'informasaun/perfil/inputkonteuduperfil.html',context)



# def editkonteuduperfil(request, id):
#     kontedudpajina = KonteuduPajina.objects.get(id=id)
#     pajina = Pajina.objects.get(id=kontedudpajina.pajina.id)
#     if request.method == 'POST':
#         forms = KonteuduPajinaForm(request.POST,request.FILES, instance = kontedudpajina )
#         if forms.is_valid():
#             instance = forms.save(commit=False)
#             instance.pajina = pajina
#             instance.save()
#             messages.success(request,"Dados Rejistu  ho Susessu..!")
#             return redirect('informasaun:manezakonteuduperfil', id = pajina.id)
#     konteudupajinaform = KonteuduPajinaForm(instance = kontedudpajina)
#     context = {
#         "asaun" : "edit",
#         "pajina_perfil" : "active",
#         # "dokumentu" : dokumentu,
#         "pajina_titulu" : "Rejistu Perfil",
#         "button" : "Rejistu",
#         "forms" : konteudupajinaform,
#     }
#     return render(request,'informasaun/perfil/inputkonteuduperfil.html',context)





# def deleteinformasaun(request,id):
#     info = Informasaun.objects.get(id=id)
#     info.delete()
#     messages.success(request,"Dados Apaga  Susessu..!")
#     return redirect('informasaun:informasaun')


