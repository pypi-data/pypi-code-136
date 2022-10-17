from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# from population.models import Population,DetailFamily,Family,Religion,Profession,Citizen,Aldeia,Village,User,Migration,Death,Migrationout,Temporary,ChangeFamily
# from population.utils import getnewidp,getnewidf
# from population.forms import Family_form,Family_form,FamilyPosition,Population_form,DetailFamily_form,CustumDetailFamily_form,Death_form,Migration_form,Migrationout_form,Changefamily_form
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone
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

from django.conf import settings
from django.http import HttpResponse
from django.utils import translation
from django.utils.translation import *
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from main.decorators import login_ona, seidauk_login, allowed_users
from mapa.models import *

from jeral.models import *



@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def set_language_from_url(request, user_language):
    translation.activate(user_language)
    request.session[settings.LANGUAGE_CODE] = user_language
    # I use HTTP_REFERER to direct them back to previous path 
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))





def index(request):
    if request.user.is_authenticated:
        return redirect('main:painel')
    else:
        context = {}
        if request.method == 'POST':
            user_input = request.POST['dmsusername']
            password_input = request.POST['dmspassword']
            user = authenticate(request, username = user_input, password = password_input)
            if user is not None:
                try:
                    group = user.groups.all()[0].name
                    print(group)
                    if group == "adminbambu" : 
                        login(request, user)
                        return redirect('main:painel')
                    else :
                        context['message'] = 'Username ho Password lalos' 
                except : 
                    context['message'] = 'Username ho Password lalos'
            else:
                context['message'] = 'Username ho Password lalos'
        return render(request, 'main/login.html',context)



@allowed_users(allowed_roles=['adminbambu'])
def userperfil(request):


    context = {
        "asaun" : "input",
        "pajina_painel" : "active",
    }



    if request.method == 'POST':
        user = authenticate(request, username = request.user.username, password = request.POST['passwordtuan'])




        if user is not None:


            d_user = User.objects.get(pk=request.user.id)
            d_user.set_password(request.POST['passwordfoun'])
            d_user.save()

            user = authenticate(request, username = request.user.username, password = request.POST['passwordfoun'])
            login(request, user)

            messages.success(request,"Password Foun Atualiza Ho susesu..!")
            context = {
                "pajina_painel" : "active",
            }


        else:

            
            messages.error(request,"Password Tuan Sala , Password Troka Falla..!")

            context = {
                "pajina_painel" : "active",
            }

            
        
    return render(request, 'main/userperfil.html',context)



def logoutuser(request):
    # d_group = request.user.groups.all()[0].name
    logout(request)
    return redirect('main:login')


@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def dashboard(request):
    return render(request, 'main/dashboard.html')

@login_ona
@allowed_users(allowed_roles=['adminbambu'])
def painel(request):



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

        "kontaprefabrika" : kontaprefabrika,
        "kontagrupuviveirus" : kontagrupuviveirus,
        "kontaareabambu" : kontaareabambu,
        "pajina_painel" : "active",

    }



    return render(request, 'main/painel.html',context)