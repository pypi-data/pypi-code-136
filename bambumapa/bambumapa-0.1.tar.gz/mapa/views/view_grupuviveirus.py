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
def grupuviveirus(request):

    buka = False;
    bukatitle = "mamuk"
    

    if request.GET.__contains__('page') :
        page_num = request.GET.get('page')
    else:
        page_num = 1
    if request.GET.__contains__('pesquiza'):
        buka = True
        paginator = Paginator(GrupuViveirus.objects.order_by('-id').filter(naran__icontains=request.GET['pesquiza']), 1)
    else:
        paginator = Paginator(GrupuViveirus.objects.order_by('-id'), 10)

    page_range = []
    for i in range(paginator.num_pages):
        page_range.append(i+1)
        data_GrupuViveirus = paginator.page(page_num)

        page_num_int = int(page_num)

    if buka :
        bukatitle = "Rezultadu Pesquiza husi <i>' (" + request.GET['pesquiza'] + ") '</i>"

    context = {
        "pajina_grupuviveirus" : "active",
        "grupuviveirus" : data_GrupuViveirus,
        'bukatitle' : bukatitle,
        'page_range' : page_range,
        'current_page' : page_num_int,
    }
    return render(request, 'mapa/grupuviveirus/lista.html',context)




@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def inputgrupuviveirus(request):



#     dokumentu =  Dokumentu.objects.all()
    # grupubambuform = GrupuBambuForm()


	# //prosses elemina sombolo no caracter nebe la inportante husi cordinate nebe foti husi lefleat draw

    # $data_cordinate = str_replace('LatLng(','[', substr($data_cordinate, 0, 10000));
    # $data_cordinate = str_replace(')',']', substr($data_cordinate, 0, 10000));	
    # $center_cordinate = str_replace('LatLng(','', substr($center_cordinate, 0, 100));
    # $center_cordinate = str_replace(')','', substr($center_cordinate, 0, 100));




    if request.method == 'POST':

        kordinatesarea = request.POST['kordinate_area']
        kordinatescentru = request.POST['kordinate_centru']

        data_cordinate_area = kordinatesarea.replace("LatLng(", "[")
        data_cordinate_area = data_cordinate_area.replace(")", "]")

        data_cordinate_centru = kordinatescentru.replace("LatLng(", "")
        data_cordinate_centru = data_cordinate_centru.replace(")", "")


        # print(data_cordinate_centru)
        

        forms = GrupuViveirusForm(request.POST,request.FILES)
        if forms.is_valid():
            instance = forms.save(commit=False)

            instance.kordinate_area = data_cordinate_area
            instance.kordinate_centru = data_cordinate_centru
            instance.user_created = User.objects.get(id=request.user.id)
            instance.date_created = date.today()
            # instance.user_update = User.objects.get(id=request.user.id)
            instance.save()
            messages.success(request,"Dados Rejistu  ho Susessu..!")
            return redirect('mapa:grupuviveirus')


    if request.GET.__contains__('kordinate') :
        kordinate = str(request.GET['kordinate'])
        print("kordinate : " + kordinate)
    else :
        kordinate = "mamuk"



    grupuviveirusform = GrupuViveirusForm()







    context = {
        "asaun" : "input",
        "pajina_grupuviveirus" : "active",
        "kordinate" : kordinate,
        # "dokumentu" : dokumentu,
        # "pajina_titulu" : "Rejistu Dokumentu",
        # "button" : "Rejistu",
        "forms" : grupuviveirusform,
    }
    return render(request, 'mapa/grupuviveirus/input.html',context)



@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def editgrupuviveirus(request,id):

    grupuviveirus = GrupuViveirus.objects.get(id=id)
    grupuviveirus2 = GrupuViveirus.objects.filter(id=id)


    kordinatekoa = ""



    if request.method == 'POST':

        kordinatesarea = request.POST['kordinate_area']
        kordinatescentru = request.POST['kordinate_centru']

        data_cordinate_area = kordinatesarea.replace("LatLng(", "[")
        data_cordinate_area = data_cordinate_area.replace(")", "]")

        data_cordinate_centru = kordinatescentru.replace("LatLng(", "")
        data_cordinate_centru = data_cordinate_centru.replace(")", "")

        forms = GrupuViveirusForm(request.POST,request.FILES,instance=grupuviveirus)
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
                    print(data_cordinate_area)
                    print("no")
                    print(data_cordinate_centru)


                    instance.kordinate_area = data_cordinate_area
                    instance.kordinate_centru = data_cordinate_centru

            # instance.user_update = User.objects.get(id=request.user.id)
            messages.success(request,"Dados Update  Susessu..!")
            instance.save()
            return redirect('mapa:grupuviveirus')
    grupuviveirusform = GrupuViveirusForm(instance = grupuviveirus)

    if request.GET.__contains__('kordinate') :
        kordinate = str(request.GET['kordinate'])
        print("kordinate : " + kordinate)
    else :
        kordinate = "mamuk"

    context = {
        "asaun" : "edit",
        "pajina_grupuviveirus" : "active",
        "grupuviveirus" : grupuviveirus,
        "kordinate" : kordinate,
        "kordinate_area" : grupuviveirus.kordinate_area,
        "naran_grupu" : grupuviveirus.naran,
        "kordinate_centru" :  grupuviveirus.kordinate_centru, 
        # "pajina_titulu" : "Rejistu Dokumentu",
        # "button" : "Rejistu",
        "forms" : grupuviveirusform,
    }
    return render(request, 'mapa/grupuviveirus/update.html',context)




@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def deletegrupuviveirus(request,id):
    grupubambu = GrupuViveirus.objects.get(id=id)
    grupubambu.delete()
    messages.success(request,"Dados Apaga  Susessu..!")
    return redirect('mapa:grupuviveirus')





@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def detallugrupuviveirus(request,id):

    dadosraix = GrupuViveirus.objects.filter(id=id)
  


    grupuviveirus = GrupuViveirus.objects.get(id=id)
    grupuviveirus2 = GrupuViveirus.objects.filter(id=id)

    context = {
        "pajina_grupuviveirus" : "active",
        "grupuviveirus" : grupuviveirus,
        "naran_grupu" : grupuviveirus.naran,
        "kordinate_area" : grupuviveirus.kordinate_area,
        "kordinate_centru" :  grupuviveirus.kordinate_centru, 
        "grupuviveirus2" : grupuviveirus2,

    }
    return render(request, 'mapa/grupuviveirus/detallu.html',context)