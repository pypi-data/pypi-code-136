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
from django.contrib.auth.models import User
from main.decorators import login_ona, seidauk_login, allowed_users



@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def grupubambu(request):

    buka = False;
    bukatitle = "mamuk"
    

    if request.GET.__contains__('page') :
        page_num = request.GET.get('page')
    else:
        page_num = 1
    if request.GET.__contains__('pesquiza'):
        buka = True
        paginator = Paginator(GrupuBambu.objects.order_by('-id').filter(naran__icontains=request.GET['pesquiza']), 1)
    else:
        paginator = Paginator(GrupuBambu.objects.order_by('-id'), 10)

    page_range = []
    for i in range(paginator.num_pages):
        page_range.append(i+1)
        data_GrupuBambu = paginator.page(page_num)

        page_num_int = int(page_num)

    if buka :
        bukatitle = "Rezultadu Pesquiza husi <i>' (" + request.GET['pesquiza'] + ") '</i>"

    context = {
        "pajina_grupubambu" : "active",
        "grupubambu" : data_GrupuBambu,
        'bukatitle' : bukatitle,
        'page_range' : page_range,
        'current_page' : page_num_int,
    }
    return render(request, 'mapa/grupubambu/lista.html',context)





@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def inputgrupubambu(request):
    kordinate = "mamuk"
    if request.method == 'POST':

        kordinatesarea = request.POST['kordinate_area']
        kordinatescentru = request.POST['kordinate_centru']

        data_cordinate_area = kordinatesarea.replace("LatLng(", "[")
        data_cordinate_area = data_cordinate_area.replace(")", "]")

        data_cordinate_centru = kordinatescentru.replace("LatLng(", "")
        data_cordinate_centru = data_cordinate_centru.replace(")", "")
        

        forms = GrupuBambuForm(request.POST, request.FILES)
        if forms.is_valid():
            instance = forms.save(commit=False)

            instance.kordinate_area = data_cordinate_area
            instance.kordinate_centru = data_cordinate_centru
            instance.user_created = User.objects.get(id=request.user.id)
            instance.date_created = date.today()
            # instance.user_update = User.objects.get(id=request.user.id)
            instance.save()
            messages.success(request,"Dados Rejistu  ho Susessu..!")
            return redirect('mapa:grupubambu')



    if request.GET.__contains__('kordinate') :
        kordinate = str(request.GET['kordinate'])
        print("kordinate : " + kordinate)
    else :
        kordinate = "mamuk"

    grupubambuform = GrupuBambuForm()
    context = {
        "asaun" : "edit",
        "pajina_grupubambu" : "active",
        "kordinate" : kordinate,
        # "dokumentu" : dokumentu,
        # "pajina_titulu" : "Rejistu Dokumentu",
        # "button" : "Rejistu",
        "forms" : grupubambuform,
    }




    return render(request, 'mapa/grupubambu/input.html',context)




@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def editgrupubambu(request,id):
    kordinate = "mamuk"
    grupubambu = GrupuBambu.objects.get(id=id)
    grupubambu2 = GrupuBambu.objects.filter(id=id)


    kordinatekoa = ""

    for dados in grupubambu2.iterator():
        
        kordinates = dados.kordinate_area
        kordinates = kordinates.replace("[", "")
        kordinates = kordinates.replace("]", "")
        kordinates = kordinates.replace(",-", "=-")
        kordinates = kordinates.replace(", -", "=-")
        kordinatekoa = kordinates.split("=")

    # print(kordinatekoa);

    if request.method == 'POST':

        kordinatesarea = request.POST['kordinate_area']
        kordinatescentru = request.POST['kordinate_centru']

        data_cordinate_area = kordinatesarea.replace("LatLng(", "[")
        data_cordinate_area = data_cordinate_area.replace(")", "]")

        data_cordinate_centru = kordinatescentru.replace("LatLng(", "")
        data_cordinate_centru = data_cordinate_centru.replace(")", "")

        forms = GrupuBambuForm(request.POST,request.FILES,instance=grupubambu)
        if forms.is_valid():

            instance = forms.save(commit=False)
            instance.user_created = User.objects.get(id=request.user.id)
            instance.date_created = date.today()



            if kordinatescentru == "":
                print("kordinate area la atualiza")
            else : 
                instance.kordinate_centru = data_cordinate_centru
                if kordinatesarea == "":
                    print("kordinate centeru la atualiza")
                else : 
                    instance.kordinate_area = data_cordinate_area
                    # instance.kordinate_centru = data_cordinate_centru

            # instance.user_update = User.objects.get(id=request.user.id)
            messages.success(request,"Dados Update  Susessu..!")
            instance.save()
            return redirect('mapa:grupubambu')
    

    grupubambuform = GrupuBambuForm(instance = grupubambu)


    if request.GET.__contains__('kordinate') :
        kordinate = str(request.GET['kordinate'])
        print("kordinate : " + kordinate)
    else :
        kordinate = "mamuk"


    print(kordinate)



    # print("kokokk : ")


    # print(grupubambu.kordinate_centru)

    context = {
        "asaun" : "edit",
        "pajina_grupubambu" : "active",
        "grupubambu" : grupubambu,
        "kordinate_area" : grupubambu.kordinate_area,
        "naran_grupu" : grupubambu.naran,
        "kordinate_centru" :  grupubambu.kordinate_centru, 
        # "pajina_titulu" : "Rejistu Dokumentu",
        # "button" : "Rejistu",
        "kordinate" : kordinate,
        "forms" : grupubambuform,
    }
    return render(request, 'mapa/grupubambu/update.html',context)





@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def deletegrupubambu(request,id):
    grupubambu = GrupuBambu.objects.get(id=id)
    grupubambu.delete()
    messages.success(request,"Dados Apaga  Susessu..!")
    return redirect('mapa:grupubambu')





@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def deleteimportasaungrupubambu(request,id):
    importasaunbambu = ImportasaunBambu.objects.get(id=id)
    idimp = importasaunbambu.grupubambu.id
    importasaunbambu.delete()
    messages.success(request,"Dados Apaga  Susessu..!")
    return redirect('mapa:rejistuimportasaunbambu' , id = idimp)







@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def detallugrupubambu(request,id):

    grupubambu = GrupuBambu.objects.get(id=id)
    grupubambu2 = GrupuBambu.objects.filter(id=id)



    context = {
        "pajina_dokumentu" : "active",
        "grupubambu" : grupubambu,
        "grupubambu2" : grupubambu2,
        "naran_grupu" : grupubambu.naran,
        "kordinate_area" : grupubambu.kordinate_area,
        "kordinate_centru" :  grupubambu.kordinate_centru, 
        "pajina_grupubambu" : "active",
    }
    return render(request, 'mapa/grupubambu/detallu.html',context)




@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def rejistuimportasaunbambu(request,id):



    grupubambuimportasaun =   ImportasaunBambu.objects.filter(grupubambu__id=id)
    grupubambuimportasaun2 =  GrupuBambu.objects.get(id=id)

    context = {
        "grupubambuimportasaun" : grupubambuimportasaun,
        "pajina_grupubambu" : "active",
        "idgrupubambu" : id,
        "naran_grupu" : grupubambuimportasaun2.naran
  
    }
    return render(request, 'mapa/grupubambu/rejistuimportasaunbambu.html',context)



@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def inputimportasaunbambu(request,id):
    grupubambu = GrupuBambu.objects.get(id=id)
    if request.method == 'POST':
        print("Tamaaaaaaa")
        forms = ImportasaunBambuForm(request.POST)
        if forms.is_valid():
            instance = forms.save(commit=False)
            instance.grupubambu = GrupuBambu.objects.get(id=id)
            instance.user_created = User.objects.get(id=request.user.id)
            instance.date_created = date.today()
            instance.save()
            messages.success(request,"Dados Rejistu  ho Susessu..!")
            return redirect('mapa:rejistuimportasaunbambu' , id = grupubambu.id)


    importasaunbambuform = ImportasaunBambuForm()
    context = {
        "forms" : importasaunbambuform,
        "pajina_grupubambu" : "active",
        "grupubambu" : grupubambu,
        "idgrupubambu" : grupubambu.id,
        "naran_grupu" : grupubambu.naran,
        "kordinate_area" : grupubambu.kordinate_area,
        "kordinate_centru" :  grupubambu.kordinate_centru,
        "asaun" : "input", 
    }
    return render(request, 'mapa/grupubambu/inputimportasaunbambu.html',context)





@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def editimportasaungrupubambu(request,id):
    importasaunbambu = ImportasaunBambu.objects.get(id=id)
    if request.method == 'POST':
        print("Tamaaaaaaa")
        forms = ImportasaunBambuForm(request.POST, instance = importasaunbambu)
        if forms.is_valid():
            instance = forms.save(commit=False)
            instance.save()
            messages.success(request,"Dados Rejistu  ho Susessu..!")
            return redirect('mapa:rejistuimportasaunbambu' , id =importasaunbambu.grupubambu.id)


    importasaunbambuform = ImportasaunBambuForm(instance = importasaunbambu)
    context = {
        "forms" : importasaunbambuform,
        "pajina_dokumentu" : "active",
        "asaun" : "edit",
        "idgrupubambu" : importasaunbambu.grupubambu.id,
        "naran_grupu" : importasaunbambu.grupubambu.naran,
    }
    return render(request, 'mapa/grupubambu/inputimportasaunbambu.html',context)


