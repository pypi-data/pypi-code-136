import math
import colebrook
import matplotlib.pyplot as plt
from sympy import *

DadosTubo = [20, 25, 32, 40, 50, 60, 75, 85, 110]
DadosPerda = [1.5, 1.7, 2.1, 2.4, 3, 3.3, 4.2, 4.7, 6.1]
DadosPerdaJoelho90 = [1.1, 1.2, 1.5, 2, 3.2, 3.4, 3.7, 3.9, 4.3]
DadosPerdaJoelho45 = [0.4, 0.5, 0.7, 1, 1.3, 1.5, 1.7, 1.8, 1.9]
DadosPerdaTC = [2.3, 2.4, 3.1, 4.6, 7.3, 7.6, 7.8, 8, 8.3]
DadosPerdaTD = [0.7, 0.8, 0.9, 1.5, 2.2, 2.3, 2.4, 2.5, 2.6]
DadosPerdaRegistro = [0.1, 0.2, 0.3, 0.4, 0.7, 0.8, 0.9, 0.9, 1]


def diametro(d):
    d = d * 1000
    j = 0
    diaexternofinal = None
    for i in DadosTubo:
        if i == d:
            i = i * 1e-3
            diaexternofinal = i - 2 * DadosPerda[j] * 1e-3
            break
        j = j + 1
    return diaexternofinal


def joelho90(d, n):
    j = 0
    d = d * 1000
    joelhofinal90 = None
    for i in DadosTubo:
        if i == d:
            joelhofinal90 = n * DadosPerdaJoelho90[j]
            break
        j = j + 1
    return joelhofinal90


def joelho45(d, n):
    j = 0
    d = d * 1000
    joelhofinal45 = None
    for i in DadosTubo:
        if i == d:
            joelhofinal45 = n * DadosPerdaJoelho45[j]
            break
        j = j + 1
    return joelhofinal45


def tc(d, n):
    j = 0
    d = d * 1000
    teecfinal = None
    for i in DadosTubo:
        if i == d:
            teecfinal = n * DadosPerdaTC[j]
            break
        j = j + 1
    return teecfinal


def td(d, n):
    j = 0
    d = d * 1000
    teedfinal = None
    for i in DadosTubo:
        if i == d:
            teedfinal = n * DadosPerdaTD[j]
            break
        j = j + 1
    return teedfinal


def re(d, n):
    j = 0
    d = d * 1000
    registrofinal = None
    for i in DadosTubo:
        if i == d:
            registrofinal = n * DadosPerdaRegistro[j]
            break
        j = j + 1
    return registrofinal


# Dados de entrada

k = 0.0000025  # rugosidade
g = 9.81  # gravidade
altcisterna = 1  # altura da cisterna
vapressure = 3200  # Pressao de vapor
rho = 981  # Densidade de agua
atmpressure = 1.01e+5  # Pressao atmosferica
visc = 0.000901  # Viscosidade da agua
DiaSuc = 32 * 1e-3
DiaRe = 32 * 1e-3

# Dados para reservatorio potavel para sucçao

ComprimentoSuc = 1.5
AlturaSuc = 0
QtdJoelho90 = 1
QtdJoelho45 = 0
PasDireta = 1
PasLado = 0
Registro = 3

# Dados para reservatorio potavel para recalque

ComprimentoRe = 27.57
AlturaRe = 19.65
QtdJoelho90Re = 10
QtdJoelho45Re = 0
PasDiretaRe = 1
PasLadoRe = 0
RegistroGavRe = 4


def calculograficopot(pessoas):
    nump = pessoas  # numero de pessoas
    vazao = 50 * nump / (1000 * 86400)
    aguapot = 100  # % de agua potavel

    # Calculo de parametros

    VazaoPot = (aguapot / 100) * vazao
    DiaExternoCanoSuc = diametro(DiaSuc)
    DiaExternoCanoRe = DiaExternoCanoSuc  # Diametro de ambos os canos iguais
    AreaSuc = (DiaExternoCanoSuc ** 2) * math.pi / 4.0
    AreaRe = (DiaExternoCanoRe ** 2) * math.pi / 4.0
    VazaoSuc = VazaoPot / AreaSuc
    VazaoRe = VazaoPot / AreaRe
    ReynoldsSucPot = rho * VazaoSuc * DiaExternoCanoSuc / visc
    ReynoldsRePot = rho * VazaoRe * DiaExternoCanoRe / visc
    Ksuc = k / DiaExternoCanoSuc
    Kre = k / DiaExternoCanoRe
    fSucPot = colebrook.sjFriction(ReynoldsSucPot, Ksuc)
    fRePot = colebrook.sjFriction(ReynoldsRePot, Kre)
    pc = rho * g * altcisterna

    # Ponto 1 sucçao

    TEEDiretoSuc = td(DiaSuc, PasDireta)  # 0.9 retirado dos dados do tigre de perda
    TEESaidaSuc = tc(DiaSuc, PasLado)  # 3.1 retirado dos dados do tigre de perda
    RegistroSuc = re(DiaSuc, Registro)  # 0.3 retirado dos dados do tigre de perda
    Joelho90Suc = joelho90(DiaSuc, QtdJoelho90)  # 1.5 retirado dos dados do tigre de perda
    Joelho45Suc = joelho45(DiaSuc, QtdJoelho45)  # 0.7 retirado dos dados do tigre de perda

    Lpsr1 = TEEDiretoSuc + TEESaidaSuc + RegistroSuc + Joelho90Suc + Joelho45Suc + ComprimentoSuc
    Hpot1 = (fSucPot * Lpsr1 * VazaoSuc ** 2) / (2 * g * DiaExternoCanoSuc)

    # Ponto 2 Recalque

    TEEDiretoRe = td(DiaRe, PasDiretaRe)  # 0.9 retirado dos dados do tigre de perda
    TEESaidaRe = tc(DiaRe, PasLadoRe)  # 3.1 retirado dos dados do tigre de perda
    RegistroRe = re(DiaRe, RegistroGavRe)  # 0.3 retirado dos dados do tigre de perda
    Joelho90Re = joelho90(DiaRe, QtdJoelho90Re)  # 1.5 retirado dos dados do tigre de perda
    Joelho45Re = joelho45(DiaRe, QtdJoelho45Re)  # 0.7 retirado dos dados do tigre de perda

    Lp2 = TEEDiretoRe + TEESaidaRe + RegistroRe + Joelho90Re + Joelho45Re + ComprimentoRe
    Hpot2 = (fRePot * Lp2 * VazaoRe ** 2) / (2 * g * DiaExternoCanoRe)

    # Calculo da altura manometrica

    psb, peb, Hb = symbols('psb,peb,Hb')

    eq1 = Eq(Hpot1 + AlturaSuc, (pc - peb) / (rho * g))
    eq2 = Eq(Hb, (psb - peb) / (rho * g))
    eq3 = Eq(Hpot2 + AlturaRe, (psb - atmpressure) / (rho * g))

    x, = linsolve([eq1, eq2, eq3], (psb, peb, Hb))
    AlturaManometrica = x[2]

    # NPSH dado de cavitaçao

    NPSH = atmpressure / (rho * g) - AlturaSuc - Hpot1 - vapressure / (rho * g)

    # NPSHr (NBR 12214)

    NPSHr1 = NPSH - 0.2 * NPSH
    NPSHr2 = NPSH - 0.5
    if NPSHr1 < NPSHr2:
        NPSHr = NPSHr1
    else:
        NPSHr = NPSHr2

    # Calculo Potencia

    Potencia = rho * g * VazaoPot * AlturaManometrica / 746

    # Calculo da Vazao

    VazaoFinal = VazaoPot * 3600

    return VazaoFinal, Potencia, NPSHr, NPSH, AlturaManometrica


#  --------------------------------------------------------------------------------
# Reserva pluvial
# Dados de entrada

DiaSucPlu = 32 * 1e-3
aguapot1 = 0

# Dados para reservatorio pluvial para sucçao

ComprimentoPlu = 4.52
AlturaSucPlu = 0
QtdJoelho90Plu = 2
QtdJoelho45Plu = 0
PasDiretaPlu = 1
PasLadoPlu = 0
RegistroPlu = 3

# Dados primeira ramificaçao do recalque

ComprimentoPlu1 = 32.02
AlturaPlu1 = 17
QtdJoelho90Plu1 = 6
QtdJoelho45Plu1 = 0
PasDiretaPlu1 = 1
PasLadoPlu1 = 0
RegistroPlu1 = 2

# Dados para primeira caixa de agua

ComprimentoPlu2 = 5.01
AlturaPlu2 = 1.21
QtdJoelho90Plu2 = 3
QtdJoelho45Plu2 = 1
PasDiretaPlu2 = 1
PasLadoPlu2 = 0
RegistroPlu2 = 1

# Dados para a segunda caixa

ComprimentoPlu3 = 11.31
AlturaPlu3 = 1.21
QtdJoelho90Plu3 = 3
QtdJoelho45Plu3 = 0
PasDiretaPlu3 = 0
PasLadoPlu3 = 0
RegistroPlu3 = 1


def calculograficoplu(pessoas):
    nump = pessoas
    vazao = 50 * nump / (1000 * 86400)
    aguapot = 0

    # Calculo parametros

    VazaoPlu = ((100 - aguapot) / 100) * vazao
    DiaSucPluExterno = diametro(DiaSucPlu)
    DiaRePluExterno = diametro(DiaSucPlu)
    DiaRePluExterno1 = diametro(DiaSucPlu)
    DiaRePluExterno2 = diametro(DiaSucPlu)
    AreaSucPlu = DiaSucPluExterno ** 2 * math.pi / 4
    AreaRePlu = DiaRePluExterno ** 2 * math.pi / 4
    VazaoSucPlu = VazaoPlu / AreaSucPlu
    VazaoRePlu = VazaoPlu / AreaRePlu
    ReynoldsSucPlu = rho * VazaoSucPlu / visc
    ReynoldsRePlu = rho * VazaoRePlu / visc
    kSucPlu = k / DiaSucPluExterno
    kRePlu = k / DiaRePluExterno
    fSucPlu = colebrook.sjFriction(ReynoldsSucPlu, kSucPlu)
    fRePlu = colebrook.sjFriction(ReynoldsRePlu, kRePlu)
    pc = rho * g * altcisterna

    # Ponto 1 sucçao

    TEEDiretoSucPlu = td(DiaSucPlu, PasDiretaPlu)
    TEESaidaSucPlu = tc(DiaSucPlu, PasLadoPlu)
    RegistroSucPlu = re(DiaSucPlu, RegistroPlu)
    Joelho45SucPlu = joelho45(DiaSucPlu, QtdJoelho45Plu)
    Joelho90SucPlu = joelho90(DiaSucPlu, QtdJoelho90Plu)

    Lpsr = TEEDiretoSucPlu + TEESaidaSucPlu + RegistroSucPlu + Joelho45SucPlu + Joelho90SucPlu
    Hplu = (fSucPlu * Lpsr * (VazaoSucPlu ** 2)) / (DiaSucPlu * 2 * g)

    # Ponto 2 recalque

    TEEDiretoSucPlu1 = td(DiaSucPlu, PasDiretaPlu1)
    TEESaidaSucPlu1 = tc(DiaSucPlu, PasLadoPlu1)
    RegistroSucPlu1 = re(DiaSucPlu, RegistroPlu1)
    Joelho45SucPlu1 = joelho45(DiaSucPlu, QtdJoelho45Plu1)
    Joelho90SucPlu1 = joelho90(DiaSucPlu, QtdJoelho90Plu1)

    Lpsr1 = TEEDiretoSucPlu1 + TEESaidaSucPlu1 + RegistroSucPlu1 + Joelho45SucPlu1 + Joelho90SucPlu1
    Hplu1 = fRePlu * Lpsr1 * (VazaoRePlu ** 2) / (DiaSucPlu * 2 * g)

    # Ponto 3

    TEEDiretoSucPlu2 = td(DiaSucPlu, PasDiretaPlu2)
    TEESaidaSucPlu2 = tc(DiaSucPlu, PasLadoPlu2)
    RegistroSucPlu2 = re(DiaSucPlu, RegistroPlu2)
    Joelho45SucPlu2 = joelho45(DiaSucPlu, QtdJoelho45Plu2)
    Joelho90SucPlu2 = joelho90(DiaSucPlu, QtdJoelho90Plu2)

    Lpsr3 = TEEDiretoSucPlu2 + TEESaidaSucPlu2 + RegistroSucPlu2 + Joelho45SucPlu2 + Joelho90SucPlu2

    # Ponnto 4

    TEEDiretoSucPlu3 = td(DiaSucPlu, PasDiretaPlu3)
    TEESaidaSucPlu3 = tc(DiaSucPlu, PasLadoPlu3)
    RegistroSucPlu3 = re(DiaSucPlu, RegistroPlu3)
    Joelho45SucPlu3 = joelho45(DiaSucPlu, QtdJoelho45Plu3)
    Joelho90SucPlu3 = joelho90(DiaSucPlu, QtdJoelho90Plu3)

    Lpsr4 = TEEDiretoSucPlu3 + TEESaidaSucPlu3 + RegistroSucPlu3 + Joelho45SucPlu3 + Joelho90SucPlu3

    # Relaçao de hazen willians C igual para os tubos

    ex = 4.87 / 1.85
    ex2 = 1 / 1.85
    lec = (((DiaRePluExterno ** ex)/(DiaRePluExterno1 ** ex/Lpsr3 ** ex2))+(DiaRePluExterno2**ex/Lpsr4**ex2))
    lec2 = lec**1.85
    Hplu2 = (fRePlu * lec2 * (VazaoRePlu ** 2)) / (DiaRePluExterno * 2 * g)

    # Calculo altura manometrica

    psb1, peb1, Hb1 = symbols('psb1,peb1,Hb1')

    eqplu = Eq(Hplu + AlturaSucPlu, (pc - peb1) / (rho * g))
    eqplu2 = Eq(Hb1, (psb1 - peb1) / (rho * g))
    eqplu3 = Eq(Hplu1 + Hplu2 + AlturaPlu1 + AlturaPlu2, (psb1 - atmpressure) / (rho * g))

    x, = linsolve([eqplu, eqplu2, eqplu3], (psb1, peb1, Hb1))
    AlturaManometrica1 = x[2]

    # Calculo NPSH

    NPSH1 = (atmpressure / (rho * g)) - AlturaSucPlu - Hplu - (vapressure / (rho * g))
    NPSHr11 = NPSH1 - 0.2 * NPSH1
    NPSHr12 = NPSH1 - 0.5

    if NPSHr11 < NPSHr12:
        NPSHrFinal = NPSHr11
    else:
        NPSHrFinal = NPSHr12

    # Calculo potencia

    Potencia1 = rho * g * VazaoPlu * AlturaManometrica1 / 746

    # Calculo Vazao

    VazaoFinal1 = VazaoPlu * 3600

    return VazaoFinal1, Potencia1, NPSHrFinal, NPSH1, AlturaManometrica1


t = calculograficopot(965)
q = calculograficoplu(965)


# print("\nResultados referentes à 100% de água pótavel\n")
# print("--------------------------------------------------------")
# print(f"A altura manométrica é {t[4]} m.c.a")
# print(f"A Potência é {t[1]} HP")
# print(f"A Vazão é {t[0]} m³/h")
# print(f"NPSH é {t[3]} m")
# print(f"NPSHr é {t[2]} m")
# print("--------------------------------------------------------")
# print("\nResultados referentes à 0% de água pótavel\n")
# print("--------------------------------------------------------")
# print(f"A altura manométrica é {q[4]} m.c.a")
# print(f"A Potência é {q[1]} HP")
# print(f"A Vazão é {q[0]} m³/h")
# print(f"NPSH é {q[3]} m")
# print(f"NPSHr é {q[2]} m")
# print("--------------------------------------------------------")

npmin = 300
npmax = 1100

b = list()
y = list()

for u in range(npmin, npmax, 50):
    z = calculograficopot(u)
    b.append(z[0])
    y.append(z[4])

w = list()
r = list()

for h in range(npmin, npmax, 50):
    s = calculograficoplu(h)
    w.append(s[0])
    r.append(s[4])
print(w)
print(r)

plt.figure()
plt.title('Gráfico referente a uso de 100% água pótavel')
plt.plot(b, y)
plt.xlabel('Vazão [m³/h]')
plt.ylabel('NPSH [m]')
plt.grid(True)

plt.figure()
plt.title('Gráfico referente a uso de 0% água pótavel')
plt.plot(w, r)
plt.xlabel('Vazão [m³/h]')
plt.ylabel('NPSH [m]')
plt.grid(True)
plt.show()
