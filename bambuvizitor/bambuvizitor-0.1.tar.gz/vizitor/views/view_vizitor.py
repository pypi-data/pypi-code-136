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

from informasaun.models import *
from informasaun.forms import *
from django.contrib.auth.models import User
from jeral.utils import getlastid
from geoalgo.algo_tree import calc
from mapa.models import *
from django.core.paginator import Paginator
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.utils import translation



def index(request):

    # user_language = 'tt'
    # translation.activate(user_language)
    # request.session[translation.LANGUAGE_SESSION_KEY] = user_language

    # from django.utils.translation import activate
    # lang_code = 'en'
    # response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
    # activate(lang_code)

    informasaun = KonteuduInformasaun.objects.filter(lingua = 1).order_by('-id')[0:2]
    informasaun2 = KonteuduInformasaun.objects.filter(lingua = 1).order_by('-id')[2:6]

    #kona ba ami foti deit bazeia ba ida husi konteudu bemvindu
    konabaami = KonteuduPajina.objects.filter(lingua = 1 , id = 1)


    #mapamento

    prefabrika = GrupuBambu.objects.all().count()
    viveirus = GrupuViveirus.objects.all().count()
    areabambu = AreaBambu.objects.all().count()



    
    #produtu 

    produtu = KonteuduProdutu.objects.filter(lingua = 1).order_by('-id')[0:4]

    parceiru = Parceiru.objects.all()


    context = {
        "informasaun2" :informasaun2,
        "informasaun" : informasaun,
        "prefabrika" : prefabrika,
        "viveirus" : viveirus,
        "areabambu" : areabambu,
        "parceiru" : parceiru,
        "produtu" : produtu,
        "pajina_index" : "active",
        "konabaami" : konabaami,
    }
    return render(request, 'index.html',context)

def mapa(request):

    html = ""

    if request.LANGUAGE_CODE == 'te' :
        html = "<br><br><center><font size='4'><img src='../../media/iconmaps/grupubambu.png' width='20px'> Grupu  Pre-Fabrika | <img src='../../media/iconmaps/grupuviveirus.png' width='20px'> Grupu Viveirus | <img src='../../media/iconmaps/areabambu.png' width='20px'> Area Plantasaun <center><div style='padding : 10px;'> <hr><h3> Localizasaun Grupu Pre-Fabrika no Grupu Viveirus iha timor-leste  <br> Total Grupu Pre-Fabrika {{totgrupubambu}} , Total Grupu Viveirus {{totgrupuviveirus}}<h4><br><form action '' method='get'>Hili Opsaun<br> <br><select class='form-control' name='mapa'><option value = 'grupuprefabrika'>Grupu Pre-Fabrika</option> <option value='grupuviveiros'>Grupu Viveirus</option> <option value='areabambu'>Grupu Area Bambu</option> </select> <br> <button class='btn btn-default' style='float:right;'type ='submit'>Hare Dados </button></form> <h4> </font> </div><br><br>"
    else :
        html = "<br><br><center><font size='4'><img src='../../media/iconmaps/grupubambu.png' width='20px'> Grupu  Pre-Fabrika | <img src='../../media/iconmaps/grupuviveirus.png' width='20px'> Grupu Viveirus | <img src='../../media/iconmaps/areabambu.png' width='20px'> Area Plantasaun <center><div style='padding : 10px;'> <hr><h3> Localizasaun Grupu Pre-Fabrika no Grupu Viveirus iha timor-leste  <br> Total Grupu Pre-Fabrika {{totgrupubambu}} , Total Grupu Viveirus {{totgrupuviveirus}}<h4><br><form action '' method='get'>Hili Opsaun<br> <br><select class='form-control' name='mapa'><option value = 'grupuprefabrika'>Grupu Pre-Fabrika</option> <option value='grupuviveiros'>Grupu Viveirus</option> <option value='areabambu'>Grupu Area Bambu</option> </select> <br> <button class='btn btn-default' style='float:right;'type ='submit'>Hare Dados </button></form> <h4> </font> </div><br><br>"
   

    
    template = ""
    context = {
        "pajina_mapa" : "active",
        "html" : html,
    }


    if request.GET.__contains__('mapa') :

        if request.GET['mapa'] == "grupuprefabrika" :
            grupubambu = GrupuBambu.objects.all()
            totgrupubambu = GrupuBambu.objects.all().count()
            template = "mapaprefabrika.html"
            total = " Localizasaun Grupu Pre-Fabrika iha timor-leste  <br> Total Grupu Pre-Fabrika : " + str(totgrupubambu)

            if request.LANGUAGE_CODE == 'te' :
                html = "<br><br><center><font size='4'><img src='../../media/iconmaps/grupubambu.png' width='20px'> Grupu  Pre-Fabrika | <img src='../../media/iconmaps/grupuviveirus.png' width='20px'> Grupu Viveirus | <img src='../../media/iconmaps/areabambu.png' width='20px'> Grupu Viveirus <center> <div style='padding : 10px;'> <hr><h3>"+total+"<h4><br><form action '' method='get'>Hili Opsaun<br> <br><select class='form-control' name='mapa'><option  selected value = 'grupuprefabrika'>Grupu  Pre-Fabrika</option> <option value='grupuviveiros'>Grupu Viveirus</option> <option value='areabambu'>Plantasaun Bambu</option> </select> <br> <button class='btn btn-default' style='float:right;'type ='submit'>Hare Dados </button></form></font> <h4></div><br><br>"
            else :
                html = "<br><br><center><font size='4'><img src='../../media/iconmaps/grupubambu.png' width='20px'> Grupu  Pre-Fabrika | <img src='../../media/iconmaps/grupuviveirus.png' width='20px'> Grupu Viveirus | <img src='../../media/iconmaps/areabambu.png' width='20px'> Grupu Viveirus <center> <div style='padding : 10px;'> <hr><h3>"+total+"<h4><br><form action '' method='get'>Hili Opsaun<br> <br><select class='form-control' name='mapa'><option  selected value = 'grupuprefabrika'>Grupu  Pre-Fabrika</option> <option value='grupuviveiros'>Grupu Viveirus</option> <option value='areabambu'>Plantasaun Bambu</option> </select> <br> <button class='btn btn-default' style='float:right;'type ='submit'>Hare Dados </button></form></font> <h4></div><br><br>"


            context = {
                "grupubambu" : grupubambu,
                "pajina_mapa" : "active",
                "html" : html,
            }

        elif request.GET['mapa'] == "grupuviveiros" :
            grupuviveirus = GrupuViveirus.objects.all()
            totgrupuviveirus = GrupuViveirus.objects.all().count()
            template = "mapaviveirus.html"
            total = " Localizasaun Grupu Viveirus iha timor-leste  <br> Total Grupu Viveirus : " + str(totgrupuviveirus)

            if request.LANGUAGE_CODE == 'te' :
                html = "<br><br><center><font size='4'><img src='../../media/iconmaps/grupubambu.png' width='20px'> Grupu Pre-Fabrika | <img src='../../media/iconmaps/grupuviveirus.png' width='20px'> Grupu Viveirus | <img src='../../media/iconmaps/areabambu.png' width='20px'> Area Plantasaun <center><div style='padding : 10px;'> <hr><h3>"+total+"<h4><br><form action '' method='get'>Hili Opsaun <br><br> <select class='form-control' name='mapa'><option value = 'grupuprefabrika'>Grupu Pre-Fabrika</option> <option selected value='grupuviveiros'>Grupu Viveirus</option> <option value='areabambu'>Plantasaun Bambu</option> </select> <br> <button class='btn btn-default' style='float:right;'type ='submit'>Hare Dados </button></form> </font>  <h4></div><br><br>"
            else :
                html = "<br><br><center><font size='4'><img src='../../media/iconmaps/grupubambu.png' width='20px'> Grupu Pre-Fabrika | <img src='../../media/iconmaps/grupuviveirus.png' width='20px'> Grupu Viveirus | <img src='../../media/iconmaps/areabambu.png' width='20px'> Area Plantasaun <center><div style='padding : 10px;'> <hr><h3>"+total+"<h4><br><form action '' method='get'>Hili Opsaun <br><br> <select class='form-control' name='mapa'><option value = 'grupuprefabrika'>Grupu Pre-Fabrika</option> <option selected value='grupuviveiros'>Grupu Viveirus</option> <option value='areabambu'>Plantasaun Bambu</option> </select> <br> <button class='btn btn-default' style='float:right;'type ='submit'>Hare Dados </button></form> </font>  <h4></div><br><br>"

            context = {
                "grupuviveirus" : grupuviveirus,
                "pajina_mapa" : "active",
                "html" : html,
            }

        elif request.GET['mapa'] == "areabambu" :
            areabambu = AreaBambu.objects.all()
            totareabambu = AreaBambu.objects.all().count()
            template = "mapaareabambu.html"
            total = " Localizasaun Area Plantasaun Bambu iha timor-leste  <br> Total  Area Plantasaun Bambu : " + str(totareabambu)





            if request.LANGUAGE_CODE == 'te' :
                html = "<br><br><center><font size='4'><img src='../../media/iconmaps/grupubambu.png' width='20px'> Grupu  Pre-Fabrika | <img src='../../media/iconmaps/grupuviveirus.png' width='20px'> Grupu Viveirus | <img src='../../media/iconmaps/areabambu.png' width='20px'> Area Plantasaun <center><div style='padding : 10px;'> <hr><h3>"+total+"<h4><br><form action '' method='get'>Hili Opsaun<br> <br><select class='form-control' name='mapa'><option value = 'grupuprefabrika'>Grupu Pre-Fabrika</option> <option value='grupuviveiros'>Grupu Viveirus</option> <option selected value='areabambu'>Plantasaun Bambu</option> </select> <br> <button class='btn btn-default' style='float:right;'type ='submit'>Hare Dados </button></form> </font>  <h4></div><br><br>"
            else :
                html = "<br><br><center><font size='4'><img src='../../media/iconmaps/grupubambu.png' width='20px'> Grupu  Pre-Fabrika | <img src='../../media/iconmaps/grupuviveirus.png' width='20px'> Grupu Viveirus | <img src='../../media/iconmaps/areabambu.png' width='20px'> Area Plantasaun <center><div style='padding : 10px;'> <hr><h3>"+total+"<h4><br><form action '' method='get'>Hili Opsaun<br> <br><select class='form-control' name='mapa'><option value = 'grupuprefabrika'>Grupu Pre-Fabrika</option> <option value='grupuviveiros'>Grupu Viveirus</option> <option selected value='areabambu'>Plantasaun Bambu</option> </select> <br> <button class='btn btn-default' style='float:right;'type ='submit'>Hare Dados </button></form> </font>  <h4></div><br><br>"


            context = {
                "areabambu" : areabambu,
                "pajina_mapa" : "active",
                "html" : html,
            }
        
    else :
        areabambu = AreaBambu.objects.all()
        totareabambu = AreaBambu.objects.all().count()
        
        grupubambu = GrupuBambu.objects.all()
        grupuviveirus = GrupuViveirus.objects.all()
        totgrupubambu = GrupuBambu.objects.all().count()
        totgrupuviveirus = GrupuViveirus.objects.all().count()
        template = "mapa.html"
        total = "Localizasaun Grupu Pre-Fabrika no Grupu Viveirus iha timor-leste  <br> Total Grupu Pre-Fabrika : " + str(totgrupubambu) +", Total Grupu Viveirus  : "+ str(totgrupuviveirus) +"<br> No Total Area Plantasaun  : "+ str(totareabambu)


        if request.LANGUAGE_CODE == 'te' :
            html = "<br><br><center><font size='4'><img src='../../media/iconmaps/grupubambu.png' width='20px'> Grupu Pre-Fabrika | <img src='../../media/iconmaps/grupuviveirus.png' width='20px'> Grupu Viveirus | <img src='../../media/iconmaps/areabambu.png' width='20px'> Area Plantasaun <center><div style='padding : 10px;'> <hr><h3>"+total+"<h4><br><form action '' method='get'>Hili Opsaun<br><br><select class='form-control' name='mapa'><option value = 'grupuprefabrika'>Grupu Pre-Fabrika</option> <option value='grupuviveiros'>Grupu Viveirus</option> <option value='areabambu'>Grupu Area Bambu</option> </select> <br> <button class='btn btn-default' style='float:right;'type ='submit'>Hare Dados </button></form> </font> <h4></div><br><br>"
        else :
            html = "<br><br><center><font size='4'><img src='../../media/iconmaps/grupubambu.png' width='20px'> Grupu Pre-Fabrika | <img src='../../media/iconmaps/grupuviveirus.png' width='20px'> Grupu Viveirus | <img src='../../media/iconmaps/areabambu.png' width='20px'> Area Plantasaun <center><div style='padding : 10px;'> <hr><h3>"+total+"<h4><br><form action '' method='get'>Hili Opsaun<br><br><select class='form-control' name='mapa'><option value = 'grupuprefabrika'>Grupu Pre-Fabrika</option> <option value='grupuviveiros'>Grupu Viveirus</option> <option value='areabambu'>Grupu Area Bambu</option> </select> <br> <button class='btn btn-default' style='float:right;'type ='submit'>Hare Dados </button></form> </font> <h4></div><br><br>"


        context = {
            "grupubambu" : grupubambu,
            "areabambu" : areabambu,
            "grupuviveirus" : grupuviveirus,
            "totgrupubambu" : totgrupubambu,
            "totgrupuviveirus" : totgrupuviveirus,
            "pajina_mapa" : "active",
            "html" : html,
        }





    return render(request,template,context)





def detallumapa(request,id):
    
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
                meter = 0

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
                meter = 0

                # print(c)


            # korlatlon = kordinatekoa[i].split(",")
    
            # phi_1=math.radians(lat1)
            # phi_2=math.radians(lat2)
            # delta_phi=math.radians(lat2-lat1)
            # delta_lambda=math.radians(lon2-lon1)
            # a=math.sin(delta_phi/2.0)**2+\
            # math.cos(phi_1)*math.cos(phi_2)*\
            # math.sin(delta_lambda/2.0)**2
            # c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))

            # phi_1=math.radians(korlatlon[0])
            # phi_2=math.radians(lat2)
            # delta_phi=math.radians(lat2-lat1)
            # delta_lambda=math.radians(lon2-lon1)
            # a=math.sin(delta_phi/2.0)**2+\
            # math.cos(phi_1)*math.cos(phi_2)*\
            # math.sin(delta_lambda/2.0)**2
            # c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))



    test = calc(kordinatekoa)


    areabambu = AreaBambu.objects.get(id=id)
    areabambu2 = AreaBambu.objects.filter(id=id)
    
    html = "<div style='padding:20px;'><h2><center><img src='"+areabambu.imagen.url+"' style ='width:100px; height:100px;'> <br> Area Plantasaun Bambu  <br> "+areabambu.naran+"</center></h2> <br> <font size='3'> Luan : "+str(test[0])+" m2 <br> Hectar : " +str(test[1])+ " <br> Localizasaun : " + str(areabambu.suku) + " / " + str(areabambu.suku.postu) + " / " + str(areabambu.suku.postu.munisipiu)  + "   </font></padding> <br> <br>"



    print(data_distance)

    context = {
        "pajina_dokumentu" : "active",
        "data_distance" : data_distance,
        "areabambu" : areabambu,
        "naran" : areabambu.naran,
        "kordinate_area" : areabambu.kordinate_area,
        "kordinate_centru" :  areabambu.kordinate_centru, 
        "km2" : km2,
        "hectar" : test[1],
        "html" : html,


    }
    return render(request, 'detallumapa.html',context)








def konabaami(request):
    
    #kona ba ami foti deit bazeia ba ida husi konteudu bemvindu
    benvindu = KonteuduPajina.objects.filter(lingua = 1 , id = 1)

    print("kokoko  : " + str(benvindu))
    misaun = KonteuduPajina.objects.filter(lingua = 1 , id = 2)
    vizaun = KonteuduPajina.objects.filter(lingua = 1 , id = 3)
    ornograma = KonteuduPajina.objects.filter(lingua = 1 , id = 4)
    objetivu = KonteuduPajina.objects.filter(lingua = 1 , id = 5)
    context = {
        "benvindu" : benvindu,
        "pajina_konabaami" : "active",
        "misaun" : misaun,
        "vizaun" : vizaun,
        "ornograma" : ornograma,
        "objetivu" : objetivu,

    }
    return render(request, 'konabaami.html',context)





@xframe_options_deny
@xframe_options_exempt
def informasaungrupu(request , id):
    
    #kona ba ami foti deit bazeia ba ida husi konteudu bemvindu
    grupu = KonteuduPajina.objects.filter(lingua = 1 , id = id)

    print("------------------------")
    print(grupu)



    context = {
        "grupu" : grupu,
        "pajina_konabaami" : "active",

    }
    return render(request, 'informasaungrupu.html',context)



def produtu(request):
    
    #kona ba ami foti deit bazeia ba ida husi konteudu bemvindu
    produtu = KonteuduProdutu.objects.filter(lingua = 1).order_by('-id')
    produtufoun = KonteuduProdutu.objects.filter(lingua = 1, produtu__foun = True).order_by('-id')
    kategoriaprodutu = KategoriaProdutu.objects.all()

    context = {
        "pajina_produtu" : "active",
        "kategoriaprodutu" : kategoriaprodutu,
        "produtu" : produtu,
        "produtufoun" :produtufoun,
    }
    return render(request, 'produtu.html',context)





def informasaun(request):


    buka = False
    bukatitle = "mamuk"
    if request.GET.__contains__('page') :
        page_num = request.GET.get('page')
    else:
        page_num = 1
    if request.GET.__contains__('pesquiza'):
        buka = True
        paginator = Paginator(Informasaun.objects.order_by('-id').filter(titulu__icontains=request.GET['pesquiza']), 1)
    else:
        paginator = Paginator(Informasaun.objects.order_by('-id'), 10)

    page_range = []
    for i in range(paginator.num_pages):
        page_range.append(i+1)
        data_Informasaun = paginator.page(page_num)
        page_num_int = int(page_num)

    if buka :
        bukatitle = "Rezultadu Pesquiza husi <i>' (" + request.GET['pesquiza'] + ") '</i>"


    data = []
    lingua = Lingua.objects.all()
    titulu = ""
    for dadosinfo in data_Informasaun :
        statuslingua = ""
        for dadoslingua in lingua : 
            konteudu = KonteuduInformasaun.objects.filter(informasaun = dadosinfo.id , lingua = dadoslingua.id).count()
            if konteudu > 0 :
                konteudu = KonteuduInformasaun.objects.filter(informasaun = dadosinfo.id , lingua = dadoslingua.id).last()
                # konteudu2 = KonteuduInformasaun.objects.filter(informasaun = dadosinfo.id , lingua = 1).last()
                titulu = konteudu.titulu
                statuslingua = statuslingua +  " <i><b>Versaun   <img src=" +dadoslingua.icon.url + " width='20px'> &nbsp; " + str(dadoslingua.naran) + " :</b> </i> " + konteudu.titulu + "<br>"
            else :
                statuslingua = statuslingua +  "<i><b>Versaun   <img src=" +dadoslingua.icon.url + " width='20px'> &nbsp;  " + str(dadoslingua.naran) + ":</b> </i>  <font color ='red'> Laiha</font> <br>"
        data.append({'imagen' : dadosinfo.imagen_main ,'lingua':dadoslingua.naran,'linguaicon' : dadoslingua.icon,'linguaid' : dadoslingua.id, 'statuslingua': statuslingua , 'data' : dadosinfo.data ,'titulu' : titulu , "id" : dadosinfo.id })

    context = {
        "pajina_informasaun" : "active",
        "informasaun" : data,
        'bukatitle' : bukatitle,
        'page_range' : page_range,
        'current_page' : page_num_int,
    }
    return render(request, 'informasaun.html',context)







def detalluprodutu(request , id):


    informasaunseluk = KonteuduInformasaun.objects.filter(lingua = 1).order_by('-id')[0:3]

    info = KonteuduInformasaun.objects.filter(informasaun__id = id, lingua = 1)


    context = {
        "pajina_informasaun" : "active",
        "info" : info,
        "informasaunseluk" : informasaunseluk,

    }
    return render(request, 'detalluinformasaun.html',context)





def detalluinformasaun(request,id):
    informasaunseluk = KonteuduInformasaun.objects.filter(lingua = 1).exclude(informasaun__id=id).order_by('-id')[0:4]
    info = KonteuduInformasaun.objects.filter(informasaun__id = id, lingua = 1)
    imagen = ImagenInformasaun.objects.filter(informasaun__id = id)
    print("info")
    context = {
        "pajina_informasaun" : "active",
        "info" : info,
        "imagen" : imagen,
        "informasaunseluk" : informasaunseluk,

    }
    return render(request, 'detalluinformasaun.html',context)


def detalluprodutu(request,id):
    konteuduprodutu = KonteuduProdutu.objects.filter(produtu__id = id, lingua = 1)
    imagenprodutu = ImagenProdutu.objects.filter(produtu__id = id)


    context = {
        "pajina_produtu" : "active",
        "konteuduprodutu" : konteuduprodutu,
        "imagenprodutu" : imagenprodutu,
    }
    return render(request, 'detalluprodutu.html',context)



def detalluprodutu2(request):
    id = request.GET['id']
    print(id)
    konteuduprodutu = KonteuduProdutu.objects.filter(produtu__id = id , lingua = 1)
    imagenprodutu = ImagenProdutu.objects.filter(produtu__id = id)


    context = {
        "pajina_produtu" : "active",
        "konteuduprodutu" : konteuduprodutu,
        "imagenprodutu" : imagenprodutu,

    }
    return render(request, 'detalluprodutu2.html',context)

