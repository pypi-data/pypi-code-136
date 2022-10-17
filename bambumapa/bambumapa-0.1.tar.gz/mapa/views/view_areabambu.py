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
from geoalgo.algo_tree import calc
from mapa.models import *
from mapa.forms import *
from django.contrib.auth.models import User
from main.decorators import login_ona, seidauk_login, allowed_users



@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def areabambu(request):

    buka = False;
    bukatitle = "mamuk"
    
    if request.GET.__contains__('page') :
        page_num = request.GET.get('page')
    else:
        page_num = 1
    if request.GET.__contains__('pesquiza'):
        buka = True
        paginator = Paginator(AreaBambu.objects.order_by('-id').filter(naran__icontains=request.GET['pesquiza']), 1)
    else:
        paginator = Paginator(AreaBambu.objects.order_by('-id'), 10)

    page_range = []
    for i in range(paginator.num_pages):
        page_range.append(i+1)
        data_AreaBambu = paginator.page(page_num)

        page_num_int = int(page_num)

    if buka :
        bukatitle = "Rezultadu Pesquiza husi <i>' (" + request.GET['pesquiza'] + ") '</i>"

    context = {
        "pajina_areabambu" : "active",
        "areabambu" : data_AreaBambu,
        'bukatitle' : bukatitle,
        'page_range' : page_range,
        'current_page' : page_num_int,
    }
    return render(request, 'mapa/areabambu/lista.html',context)




@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def inputareabambu(request):
    kordinate = "mamuk"
    # kordinate_centru = "mamuk"

    if request.method == 'POST':

        kordinatesarea = request.POST['kordinate_area']
        kordinatescentru = request.POST['kordinate_centru']

        data_cordinate_area = kordinatesarea.replace("LatLng(", "[")
        data_cordinate_area = data_cordinate_area.replace(")", "]")

        data_cordinate_centru = kordinatescentru.replace("LatLng(", "")
        data_cordinate_centru = data_cordinate_centru.replace(")", "")


        print(data_cordinate_centru)
        

        forms = AreaBambuForm(request.POST,request.FILES)
        if forms.is_valid():
            instance = forms.save(commit=False)

            instance.kordinate_area = data_cordinate_area
            instance.kordinate_centru = data_cordinate_centru
            instance.user_created = User.objects.get(id=request.user.id)
            instance.date_created = date.today()
            # instance.user_update = User.objects.get(id=request.user.id)
            instance.save()
            messages.success(request,"Dados Rejistu  ho Susessu..!")
            return redirect('mapa:areabambu')

    if request.GET.__contains__('kordinate') :
        kordinate = str(request.GET['kordinate'])
        # kordinate_centru = str(request.GET['kordinate_centru'])
        print("kordinate area : " + kordinate)
        # print("kordinate centru : " + kordinate_centru)
    else :
        kordinate = "mamuk"


    areabambuform = AreaBambuForm()


    context = {
        "asaun" : "input",
        "pajina_areabambu" : "active",
        # "kordinate_area" : kordinate_area,
        "kordinate" : kordinate,
        # "kordinate_centru" : kordinate_centru,

        # "kordinate_centru" : kordinate_centru,
        # "dokumentu" : dokumentu,
        # "pajina_titulu" : "Rejistu Dokumentu",
        # "button" : "Rejistu",
        "forms" : areabambuform,
    }
    return render(request, 'mapa/areabambu/input.html',context)



@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def editareabambu(request,id):

    areabambu = AreaBambu.objects.get(id=id)
    areabambu2 = AreaBambu.objects.filter(id=id)


    kordinatekoa = ""

    for dados in areabambu2.iterator():
        
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

        forms = AreaBambuForm(request.POST,request.FILES,instance=areabambu, )
        if forms.is_valid():

            instance = forms.save(commit=False)
            instance.user_created = User.objects.get(id=request.user.id)
            instance.date_created = date.today()


            if kordinatesarea == "":
                print("kordinate area la atualiza")

            else : 
                
                if kordinatescentru == "":
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
            return redirect('mapa:areabambu')


    if request.GET.__contains__('kordinate') :
        kordinate = str(request.GET['kordinate'])
        # kordinate_centru = str(request.GET['kordinate_centru'])
        print("kordinate area : " + kordinate)
        # print("kordinate centru : " + kordinate_centru)
    else :
        kordinate = "mamuk"


    areabambuform = AreaBambuForm(instance = areabambu)

    context = {
        "asaun" : "edit",
        "pajina_areabambu" : "active",
        "areabambu" : areabambu,
        "kordinate_area" : areabambu.kordinate_area,
        "kordinate" : kordinate,
        "naran_grupu"  : areabambu.naran,
        "kordinate_centru" :  areabambu.kordinate_centru, 
        # "pajina_titulu" : "Rejistu Dokumentu",
        # "button" : "Rejistu",
        "forms" : areabambuform,
    }
    return render(request, 'mapa/areabambu/update.html',context)




@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def deleteareabambu(request,id):
    areabambu = AreaBambu.objects.get(id=id)
    areabambu.delete()
    messages.success(request,"Dados Apaga  Susessu..!")
    return redirect('mapa:areabambu')





@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def detalluareabambu(request,id):
    test = ""
    import math
    dadosraix = AreaBambu.objects.filter(id=id)
  
    km2 = ""
    R=6371000  
    data_distance = []
    for dados in dadosraix.iterator():

        kordinates = dados.kordinate_area
        kordinates = kordinates.replace("[", "")
        kordinates = kordinates.replace("]", "")
        kordinates = kordinates.replace(",-", "=-")
        kordinates = kordinates.replace(", -", "=-")
        kordinatekoa = kordinates.split("=") 


        # kalkula kordinate husi poin ida ba ida
        meter = 0
        totalkor = len(kordinatekoa)
        kor1 = 0
        for i in   range(totalkor) :
            lat2 = i + 1

            if lat2 < totalkor :
                ko1 = kordinatekoa[i].split(",") 
                ko2 =  kordinatekoa[lat2].split(",") 

                # lat1 = ko1[0]
                # lat2 = ko2[0]


                # lon1 = ko1[1]
                # lon2 = ko2[1]
                phi_1=math.radians(float(ko1[0]))
                phi_2=math.radians(float(ko2[0]))
                delta_phi=math.radians(float(ko2[0])-float(ko1[0]))
                delta_lambda=math.radians(float(ko2[1])-float(ko1[1]))
                a=math.sin(delta_phi/2.0)**2+\
                math.cos(phi_1)*math.cos(phi_2)*\
                math.sin(delta_lambda/2.0)**2
                c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))
                meters=R*c
                meter = meter+meters
                meter = round(meter)
                data_distance.append({"kor1": kordinatekoa[i], "kor2": kordinatekoa[lat2], "distancia" : meter, "husi": i+1 ,"ba": lat2+1})

                # print(kordinatekoa[i] + "ho" + kordinatekoa[lat2]) 
            else :
                # print(kordinatekoa[i]+" ho "+ kordinatekoa[0])
                ko1 = kordinatekoa[i].split(",") 
                ko2 =  kordinatekoa[0].split(",") 

                phi_1=math.radians(float(ko1[0]))
                phi_2=math.radians(float(ko2[0]))
                delta_phi=math.radians(float(ko2[0])-float(ko1[0]))
                delta_lambda=math.radians(float(ko2[1])-float(ko1[1]))
                a=math.sin(delta_phi/2.0)**2+\
                math.cos(phi_1)*math.cos(phi_2)*\
                math.sin(delta_lambda/2.0)**2
                c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))
                meters=R*c
                meter = meter+meters
                meter = round(meter)
                data_distance.append({"kor1": kordinatekoa[i], "kor2": kordinatekoa[0], "distancia" : meter, "husi": i+1 ,"ba": "zero"})


        test = calc(kordinatekoa)


        AreaBambu.objects.filter(pk=id).update(hectar=test)


    areabambu = AreaBambu.objects.get(id=id)
    areabambu2 = AreaBambu.objects.filter(id=id)




    print(data_distance)
    areabambuform = AreaBambuForm(instance = areabambu)

    context = {
        "pajina_dokumentu" : "active",
        "data_distance" : data_distance,
        "areabambu2" : areabambu2,
        "areabambu" : areabambu,
        "kordinate_area" : areabambu.kordinate_area,
        "kordinate_centru" :  areabambu.kordinate_centru, 
        "km2" : test[0],
        "hectar" : test[1],
        "pajina_areabambu" : "active",
        # "pajina_titulu" : "Rejistu Dokumentu",
        # "button" : "Rejistu",
        "forms" : areabambuform,
    }
    return render(request, 'mapa/areabambu/detallu.html',context)