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
from jeral.models import *
from mapa.models import *
from mapa.forms import *

from informasaun.models import *
from informasaun.forms import *


from django.contrib.auth.models import User

from jeral.utils import getlastid
from main.decorators import login_ona, seidauk_login, allowed_users



@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def perfil(request):

    buka = False;
    bukatitle = "mamuk"
    
    if request.GET.__contains__('page') :
        page_num = request.GET.get('page')
    else:
        page_num = 1
    if request.GET.__contains__('pesquiza'):
        buka = True
        paginator = Paginator(Pajina.objects.order_by('-id').filter(naran__icontains=request.GET['pesquiza']), 1)

    else:
        paginator = Paginator(Pajina.objects.order_by('-id'), 10)

    page_range = []
    for i in range(paginator.num_pages):
        page_range.append(i+1)
        data_Pajina = paginator.page(page_num)

        page_num_int = int(page_num)

    if buka :
        bukatitle = "Rezultadu Pesquiza husi <i>' (" + request.GET['pesquiza'] + ") '</i>"

    data = []
    lingua = Lingua.objects.all()
    titulu = ""
    for dadospajina in data_Pajina :
        statuslingua = ""
        for dadoslingua in lingua : 
            konteudu = KonteuduPajina.objects.filter(pajina = dadospajina.id , lingua = dadoslingua.id).count()
            if konteudu > 0 :
                konteudu = KonteuduPajina.objects.filter(pajina = dadospajina.id , lingua = dadoslingua.id).last()
                # konteudu2 = KonteuduInformasaun.objects.filter(informasaun = dadosinfo.id , lingua = 1).last()
                titulu = konteudu.titulu
                statuslingua = statuslingua +  " <i><b>   <img src=" +dadoslingua.icon.url + " width='20px'> &nbsp; </b> </i> " + konteudu.titulu + "<br>"
            else :
                statuslingua = statuslingua +  "<i><b>   <img src=" +dadoslingua.icon.url + " width='20px'> &nbsp; </b> </i>  <font color ='red'> Laiha</font> <br>"
        data.append({'lingua':dadoslingua.naran,'linguaicon' : dadoslingua.icon,'linguaid' : dadoslingua.id, 'statuslingua': statuslingua , 'data' : dadospajina.data ,'titulu' : titulu , "id" : dadospajina.id })




    context = {
        "pajina_perfil" : "active",
        "perfil" : data,
        'bukatitle' : bukatitle,
        'page_range' : page_range,
        'current_page' : page_num_int,
    }
    return render(request, 'informasaun/perfil/lista.html',context)





# def inputperfil(request):
#     if request.method == 'POST':
#         forms = KonteuduPajinaForm(request.POST)
#         if forms.is_valid():
#             instance = forms.save(commit=False)
#             instance.save()
#             messages.success(request,"Dados Rejistu  ho Susessu..!")
#             return redirect('informasaun:perfil')


#     perfilform = KonteuduPajinaForm()
#     context = {
#         "asaun" : "input",
#         "pajina_perfil" : "active",
#         # "dokumentu" : dokumentu,
#         "pajina_titulu" : "Rejistu Perfil",
#         "button" : "Rejistu",
#         "forms" : perfilform,
#     }
#     return render(request, 'informasaun/perfil/input.html',context)


@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def inputperfil(request):
    if request.method == 'POST':
        dataagora = timezone.now()
        hashed = getlastid(Pajina)
        forms = KonteuduPajinaForm(request.POST, request.FILES)
        
        if forms.is_valid():

            pajina = Pajina()
            pajina.id = hashed[0]
            pajina.data = request.POST['data']
            pajina.date_created = dataagora
            pajina.user_created = User.objects.get(id = request.user.id)
            pajina.save()

    
            instance = forms.save(commit=False)
            instance.pajina = Pajina.objects.get(id=hashed[0])
            instance.date = request.POST['data']
            instance.lingua = Lingua.objects.get(id = 1)
            instance.save()
            messages.success(request,"Dados Rejistu  ho Susessu..!")
            return redirect('informasaun:perfil')

    perfilform = KonteuduPajinaForm()
    context = {
        "asaun" : "input",
        "pajina_perfil" : "active",
        # "dokumentu" : dokumentu,
        "pajina_titulu" : "Rejistu Perfil",
        "button" : "Rejistu",
        "forms" : perfilform,
    }
    return render(request, 'informasaun/perfil/input.html',context)




@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def deleteperfil(request,id):
    perfil = Pajina.objects.get(id=id)
    perfil.delete()
    messages.success(request,"Dados Apaga  Susessu..!")
    return redirect('informasaun:perfil')






@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def editperfil(request,id):
    pajina = Pajina.objects.get(id=id)


    if request.method == 'POST':
        forms = PerfilForm(request.POST, instance=pajina)
        if forms.is_valid():
            instance = forms.save(commit=False)
            instance.save()
            messages.success(request,"Dados Rejistu  ho Susessu..!")
            return redirect('informasaun:perfil')

    perfilform = PerfilForm(instance = pajina)
    context = {
        "asaun" : "input",
        "pajina_perfil" : "active",
        # "dokumentu" : dokumentu,
        "pajina_titulu" : "Rejistu Perfil",
        "button" : "Rejistu",
        "forms" : perfilform,
        "naran_perfil" : pajina.titulu,
    }
    return render(request, 'informasaun/perfil/input.html',context)







@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def manezakonteuduperfil(request,id):

    #konteudu lingua 
    pajinakontedu =  KonteuduPajina.objects.filter(pajina = id)
    pajinakontedu2 =  KonteuduPajina.objects.get(pajina = id)

    
    lingua = Lingua.objects.all()
    data = []

    for dados in lingua.iterator() :
        konteudu = KonteuduPajina.objects.filter(lingua=dados.id,pajina = id).count()

        if konteudu > 0 :

            konteudu = KonteuduPajina.objects.filter(lingua=dados.id,pajina = id).last()
            data.append({'lingua':dados.naran,'linguaicon' : dados.icon,'linguaid' : dados.id,  'status': 'iha' , 'data' : konteudu.data,'linkvideo' : konteudu.linkvideo,'pdf' : konteudu.file_pdf, 'imagen' : konteudu.imagen ,'titulu' : konteudu.titulu , "id" : konteudu.id })
        else :
            data.append({'lingua':dados.naran,'linguaicon' : dados.icon,'linguaid' : dados.id, 'status': 'laiha' , 'linkvideo' : 'Liaha','pdf' : 'Laiha', 'imagen' : 'Laiha',  'data' : "Mamuk" ,'titulu' : "Mamuk" , "id" : int(id) })

    context = {

        "asaun" : "input",
        "pajina_perfil" : "active",
        "pajinakontedu" : data,
        "pajina_titulu" : "Rejistu Perfil",
        "button" : "Rejistu",
        "pajinakontedu2" : pajinakontedu2.titulu,

        "id" : id,

    }
    return render(request, 'informasaun/perfil/manezakonteudu.html',context)


@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def inputkonteuduperfil(request,id,lingua):

    pajina = Pajina.objects.get(id=id)
    

    if request.method == 'POST':
        forms = KonteuduPajinaForm(request.POST,request.FILES)
        if forms.is_valid():
            instance = forms.save(commit=False)
            instance.pajina = pajina
            instance.lingua = Lingua.objects.get(id=lingua)
            instance.save()
            messages.success(request,"Dados Rejistu  ho Susessu..!")
            return redirect('informasaun:manezakonteuduperfil', id = id)

    konteudupajinaform = KonteuduPajinaForm()
    context = {
        "asaun" : "input",
        "pajina_perfil" : "active",
        # "dokumentu" : dokumentu,
        "pajina_titulu" : "Rejistu Perfil",
        "button" : "Rejistu",
        "forms" : konteudupajinaform,
    }
    return render(request,'informasaun/perfil/inputkonteuduperfil.html',context)




@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def editkonteuduperfil(request, id, lingua):


    kontedudpajina = KonteuduPajina.objects.get(id=id , lingua = lingua)
    pajina = Pajina.objects.get(id=kontedudpajina.pajina.id)
    

    if request.method == 'POST':
        forms = KonteuduPajinaForm(request.POST,request.FILES, instance = kontedudpajina )
        if forms.is_valid():
            instance = forms.save(commit=False)
            instance.save()
            messages.success(request,"Dados Rejistu  ho Susessu..!")
            return redirect('informasaun:manezakonteuduperfil', id = pajina.id)


    konteudupajinaform = KonteuduPajinaForm(instance = kontedudpajina)
    context = {
        "asaun" : "edit",
        "pajina_perfil" : "active",
        "kontedudpajina" : kontedudpajina.titulu,

        # "dokumentu" : dokumentu,
        "pajina_titulu" : "Rejistu Perfil",
        "button" : "Rejistu",
        "forms" : konteudupajinaform,
    }
    return render(request,'informasaun/perfil/inputkonteuduperfil.html',context)


@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def apagakonteuduperfil(request,id):
    perfil = KonteuduPajina.objects.get(id=id)
    idp = perfil.pajina.id
    perfil.delete()
    messages.success(request,"Dados Apaga  Susessu..!")
    return redirect('informasaun:manezakonteuduperfil', id = idp)

    


