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
def parceiru(request):
    buka = False
    bukatitle = "mamuk"
    if request.GET.__contains__('page') :
        page_num = request.GET.get('page')
    else:
        page_num = 1
    if request.GET.__contains__('pesquiza'):
        buka = True
        paginator = Paginator(Parceiru.objects.order_by('-id').filter(naran__icontains=request.GET['pesquiza']), 1)

    else:
        paginator = Paginator(Parceiru.objects.order_by('-id'), 10)

    page_range = []
    for i in range(paginator.num_pages):
        page_range.append(i+1)
        data_Parceiru = paginator.page(page_num)
        page_num_int = int(page_num)

    if buka :
        bukatitle = "Rezultadu Pesquiza husi <i>' (" + request.GET['pesquiza'] + ") '</i>"

   
    context = {
        "pajina_parceiru" : "active",
        "parceiru" : data_Parceiru,
        'bukatitle' : bukatitle,
        'page_range' : page_range,
        'current_page' : page_num_int,
    }
    return render(request, 'informasaun/parceiru/lista.html',context)




@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def inputparceiru(request):

    dataagora = timezone.now()
    if request.method == 'POST':
        forms = ParceiruForm(request.POST, request.FILES)
  
        if forms.is_valid():
            instance = forms.save(commit=False)
            instance.save()
            messages.success(request,"Dados Rejistu  ho Susessu..!")
            return redirect('informasaun:parceiru')


    pareceiruform = ParceiruForm()
    context = {
        "asaun" : "input",
        "pajina_parceiru" : "active",
        # "dokumentu" : dokumentu,
        "pajina_titulu" : "Rejistu Perfil",
        "button" : "Rejistu",
        "forms" : pareceiruform,
    }
    return render(request, 'informasaun/parceiru/input.html',context)

@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def editparceiru(request, id):

    parceiru = Parceiru.objects.get(id=id)


    dataagora = timezone.now()
    if request.method == 'POST':
        forms = ParceiruForm(request.POST, request.FILES, instance=parceiru)
        if forms.is_valid():
            instance = forms.save(commit=False)
            instance.save()
            messages.success(request,"Dados Rejistu  ho Susessu..!")
            return redirect('informasaun:parceiru')


    pareceiruform = ParceiruForm(instance=parceiru)
    context = {
        "asaun" : "edit",
        "pajina_parceiru" : "active",
        # "dokumentu" : dokumentu,
        "pajina_titulu" : "Rejistu Perfil",
        "button" : "Rejistu",
        "forms" : pareceiruform,
        "naran_parceiru" :  parceiru.naran,
     }
    return render(request, 'informasaun/parceiru/update.html',context)


@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def deleteparceiru(request,id):
    parceiru = Parceiru.objects.get(id=id)
    parceiru.delete()
    messages.success(request,"Dados Apaga  Susessu..!")
    return redirect('informasaun:parceiru')


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





# def manezakonteuduprodutu(request,id):

#     #konteudu lingua 

#     konteuduprodutu =  KonteuduProdutu.objects.filter(produtu = id)
#     lingua = Lingua.objects.all()
#     data = []

#     for dados in lingua.iterator() :
#         konteudu = KonteuduProdutu.objects.filter(lingua=dados.id,produtu = id).count()
#         if konteudu > 0 :
#             konteudu = KonteuduProdutu.objects.filter(lingua=dados.id,produtu = id).last()
#             data.append({'lingua':dados.naran,'linguaicon' : dados.icon,'linguaid' : dados.id,  'status': 'iha' , 'data' : konteudu.data_produsaun,'titulu' : konteudu.titulu , "id" : konteudu.id })
#         else :
#             data.append({'lingua':dados.naran,'linguaicon' : dados.icon,'linguaid' : dados.id, 'status': 'laiha' , 'data' : "Mamuk" ,'titulu' : "Mamuk" , "id" : int(id) })

#     #konteudu imagen

#     imagenprodutu =  ImagenProdutu.objects.filter(produtu = id)
#     forms = ImagenProdutuForm()
#     produtu = Produtu.objects.filter(id = id)
#     mainimagen = Produtu.objects.get(id = id)
#     lingua = Lingua.objects.all()
#     imagen = ImagenProdutu.objects.filter(produtu = id)


#     if request.method == 'POST':
#         forms = ImagenProdutuForm(request.POST, request.FILES)
#         if forms.is_valid():
#             instance = forms.save(commit=False)
#             instance.produtu = Produtu.objects.get(id=id)
#             instance.save()
#             messages.success(request,"Dadus Rejistu  ho Susessu..!")
#             return redirect('informasaun:manezakonteuduprodutu', id = id)

#     context = {
#         "asaun" : "input",
#         "pajina_produtu" : "active",
#         "konteuduprodutu" : data,
#         "pajina_titulu" : "Maneza Konteudu",
#         "button" : "Rejistu",
#         "id" : id,

#         "mainimagen" : mainimagen.imagen_main,
#         "forms" : forms,
#         "produtu" : produtu,
#         "imagenprodutu" : imagenprodutu,


#     }
#     return render(request, 'informasaun/produtu/manezakonteudu.html',context)



# def inputkonteuduprodutu(request,id,lingua):
#     if request.method == 'POST':
#         hashed = getlastid(KonteuduProdutu)
#         forms = KonteuduProdutuForm(request.POST)
#         if forms.is_valid():
   
#             instance = forms.save(commit=False)
#             instance.produtu = Produtu.objects.get(id = id)
#             instance.lingua = Lingua.objects.get(id=lingua)
#             # instance.id = hashed[0]
#             # instance.hashed = hashed[1]
#             Produtu.objects.filter(pk=id).update(data=request.POST['data_produsaun']) 
#             instance.save()
#             messages.success(request,"dados Rejistu  ho Susessu..!")
#             return redirect('informasaun:manezakonteuduprodutu' , id =  id)

#     konteuduprodutuform = KonteuduProdutuForm()
#     context = {
#         "asaun" : "input",
#         "pajina_perfil" : "active",
#         # "dokumentu" : dokumentu,
#         "pajina_titulu" : "Rejistu Perfil",
#         "button" : "Rejistu",
#         "forms" : konteuduprodutuform,
#     }
#     return render(request, 'informasaun/produtu/inputkonteuduprodutu.html',context)





# def editkonteuduprodutu(request,id,lingua):
#     konteuduprodutu = KonteuduProdutu.objects.get(id=id, lingua = lingua)
#     if request.method == 'POST':
#         hashed = getlastid(KonteuduProdutu)
#         forms = KonteuduProdutuForm(request.POST, instance = konteuduprodutu)
#         if forms.is_valid():
#             instance = forms.save(commit=False)
#             # instance.id = hashed[0]
#             # instance.hashed = hashed[1] 
#             instance.lingua = Lingua.objects.get(id=lingua)
#             instance.save()
#             Produtu.objects.filter(pk=konteuduprodutu.produtu.id).update(data=request.POST['data_produsaun']) 
#             messages.success(request,"dados Rejistu  ho Susessu..!")
#             return redirect('informasaun:manezakonteuduprodutu' , id =  konteuduprodutu.produtu.id)

#     konteuduprodutuform = KonteuduProdutuForm(instance = konteuduprodutu)
#     context = {
#         "asaun" : "input",
#         "pajina_produtu" : "active",
#         # "dokumentu" : dokumentu,
#         "pajina_titulu" : "Atualiza Konteudu",
#         "button" : "Atualiza",
#         "forms" : konteuduprodutuform,
#     }
#     return render(request, 'informasaun/informasaun/inputkonteuduinformasaun.html',context)



# def apagakonteuduprodutu(request,id):
#     konteuduprodutu = KonteuduProdutu.objects.get(id=id)
#     idinfo =  konteuduprodutu.produtu.id
#     konteudu = KonteuduProdutu.objects.get(id=id)
#     konteudu.delete()
#     messages.success(request,"Dados Apaga  Susessu..!")
#     return redirect('informasaun:manezakonteuduprodutu' , id =  idinfo)



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











# def setimagenprodutu(request,id):
#     imagen = ImagenProdutu.objects.get(id=id)
#     Produtu.objects.filter(pk=imagen.produtu.id).update(imagen_main=str(imagen.imagen))
#     idinfo = imagen.produtu.id
#     messages.success(request,"Imagen set  Susessu..!")
#     return redirect('informasaun:manezakonteuduprodutu', id = idinfo)









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


