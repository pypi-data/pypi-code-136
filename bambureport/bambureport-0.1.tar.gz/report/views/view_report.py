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

from jeral.models import *
from django.db.models import Sum








def report(request):


    munisipiu = Munisipiu.objects.all()

    kontaprefabrika = []
    kontagrupuviveirus = []
    kontaareabambu = []

    for dados in munisipiu.iterator() :
        total = 0
        total = GrupuBambu.objects.filter(suku__postu__munisipiu__id = dados.id).count()
        kontaprefabrika.append({"munisipiu" : dados.naran ,"id" : dados.id, "total" : total} )


    for dados in munisipiu.iterator() :
        total = 0
        total = GrupuViveirus.objects.filter(suku__postu__munisipiu__id = dados.id).count()
        kontagrupuviveirus.append({"munisipiu" : dados.naran ,"id" : dados.id, "total" : total} )


    for dados in munisipiu.iterator() :
        total = 0
        total = AreaBambu.objects.filter(suku__postu__munisipiu__id = dados.id).count()
        kontaareabambu.append({"munisipiu" : dados.naran ,"id" : dados.id,  "total" : total} )




    

    context = {
        "pajina_report" : "active",
        "kontaprefabrika" : kontaprefabrika,
        "kontagrupuviveirus" : kontagrupuviveirus,
        "kontaareabambu" : kontaareabambu,

    }
    return render(request, 'report/report/index.html',context)



def printviveirus(request, id) :
    printviveirus = GrupuViveirus.objects.filter(suku__postu__munisipiu__id = id)
    munisipiu = Munisipiu.objects.get(id = id)
    context = {
        "pajina_report" : "activat",
        "printviveirus" : printviveirus,
        "munisipiu" : munisipiu.naran , 
    }
    return render(request, 'report/report/printviveirus.html',context)




def printviveirus(request, id) :
    printviveirus = GrupuViveirus.objects.filter(suku__postu__munisipiu__id = id)
    munisipiu = Munisipiu.objects.get(id = id)
    context = {
        "pajina_report" : "activat",
        "printviveirus" : printviveirus,
        "munisipiu" : munisipiu.naran , 
    }
    return render(request, 'report/report/printviveirus.html',context)




def printareabambu(request, id) :

    totalhectar = AreaBambu.objects.aggregate(Sum('hectar'))
    print(totalhectar)

    printareabambu = AreaBambu.objects.filter(suku__postu__munisipiu__id = id)
    munisipiu = Munisipiu.objects.get(id = id)
    context = {
        "pajina_report" : "activat",
        "printareabambu" : printareabambu,
        "totalhectar" : totalhectar['hectar__sum'],
        "munisipiu" : munisipiu.naran , 
    }
    return render(request, 'report/report/printareabambu.html',context)



def printprefabrika(request, id) :
    printprefabrika = GrupuBambu.objects.filter(suku__postu__munisipiu__id = id)
    munisipiu = Munisipiu.objects.get(id = id)
    context = {
        "pajina_report" : "activat",
        "printprefabrika" : printprefabrika,

        "munisipiu" : munisipiu.naran , 
    }
    return render(request, 'report/report/printprefabrika.html',context)


