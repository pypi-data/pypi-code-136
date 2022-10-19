from pydantic import BaseModel, Field, validator, root_validator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from enum import Enum, IntEnum
from typing import Dict, List, Optional, Union
from datetime import date
# Aqueon Models to parameters as json file

# Aqueon Model

class RunModeEnum(str, Enum):
    """
    Enum for the type of run.
    """
    fit = "fit"

class MultList(BaseModel):
    APIs: List[str] = Field([])
    mults: List[float] = Field([])
    
    @validator('APIs',each_item=True)
    def check_length(cls,v):
        assert len(v) == 14, 'API must be 14 characters long'
        return v
class ReservesData(BaseModel):
    Reservoir: List[str] = Field(..., description='Reservoirs name')
    SoInitMin: List[float] = Field(..., description='Initial Oil Sat')
    SoInitMax: List[float] = Field(..., description='Initial Oil Sat')
    SgInitMin: List[float] = Field(..., description='Initial Gas Sat')
    SgInitMax: List[float] = Field(..., description='Initial Gas Sat')
    NetPay: List[float] = Field(..., description='Net Pay')
    
    @validator('SoInitMax')
    def check_so_min(cls,v, values):
        if values['SoInitMin'] >= v:
            raise ValueError('SoInitMin must be less than SoInitMax')
        return v
    
    @validator('SgInitMax')
    def check_sg_min(cls,v, values):
        if values['SgInitMin'] >= v:
            raise ValueError('SgInitMin must be less than SgInitMax')
        return v
    
    @validator('NetPay', each_item=True)
    def check_netpay(cls,v):
        assert v >= 0, 'NetPay must be greater than 0'
    
    @root_validator
    def check_length_fields(cls,values):
        list_lengths = []
        for i in values:
            l = len(values[i])
            list_lengths.append(l)
        
        assert all(i == list_lengths[0] for i in list_lengths), 'All fields must have the same length'
        return values


    
class FlowUnits(BaseModel):
    wellGuid: List[str] = Field([])
    unitName: List[str] = Field([""])
    
class ResBounds(BaseModel):
    xMin: float
    xMax: float
    yMin: float
    yMax: float
    
    @validator('xMax')
    def check_xmax_min(cls,v, values):
        if values['xMin'] >= v:
            raise ValueError('xMax must be greater than xMin')
        return v
    @validator('yMax')
    def check_ymax_min(cls,v, values):
        if values['yMin'] >= v:
            raise ValueError('yMax must be greater than yMin')
        return v

class Enkf(BaseModel):
    fitType: int = Field(2, ge=0, le=3)
    qpFitMode: int = Field(0, ge=0, le=2)
    Nc: int = Field(20, ge=1, le=100000)
    Ne: int = Field(96, ge=32, le=192)
    NhPct: int = Field(95, ge=1, le=100)
    beta: float = Field(0.05, ge=0.01, le=0.1)
    dataType: int = Field(0, ge=0, le=1) #? Check if this is correct
    isIntInjW: bool = Field(True)
    isIntProd: bool = Field(True)
    prodBHPSource: int = Field(3, ge=0, le=3)
    isFilter: bool = Field(True)
    infFact : float = Field(0.05, ge=0.01, le=0.1)
    isPerturb: bool = Field(True)
    wSmooth: float = Field(0.05, ge=0.01)
    smoothType: int = Field(0, ge=0, le=3)
    minResponsivity: float = Field(0.001, gt=0)
    maxResponsivity: float = Field(5, gt=0)
    histControlMode: int = Field(0, ge=0, le=1)
    nBHPCont: int = Field(10, ge=10, le=10000000)
    nTCorr: int = Field(6, ge=1, le=60)
    nTCorrEnd: int = Field(2, ge=1, le=60)
    isPar: bool = Field(True)
    sd : List[List[float]] = Field([[0.15],[0.15],[0.3],[0.15],[0.4]])
    startDate: date = Field(None)
    endDate: date = Field(None)
    btEndDate: date = Field(None)
    isDB: int = Field(1, ge=0, le=2) #? Check if this is correct
    fitMode: int = Field(0, ge=0, le=1) #? Check if this is correct
    stepOutput: int = Field(0, ge=0, le=1) #? Check if this is correct
    maxExtrapolate: int = Field(0, ge=0)
    nMovingMeanBHP: int = Field(0, ge=0)
    allowConversions: bool = Field(False)

    
    @validator('sd', each_item=True)
    def check_sd(cls,v):
        assert len(v) == 1, 'sd must be a list of length 1'
        assert v[0] > 0, 'sd must be greater than 0'
        assert v[0] < 1, 'sd must be less than 1'
        
    class Config:
        json_encoders = {
            date: lambda d: d.strftime('%Y-%m-%d'),
            bool: lambda b: int(b)
        }

class gHKernelModel(IntEnum):
    each_resmap = 0
    continuous_resmap = 1

class BoundaryType(IntEnum):
    closed = 0
    edge = 1
    bottom = 2
    
class ReserveMode(IntEnum):
    constant_netpay = 0
    layer_netpay = 1
    well_netpay = 2
    
class FlowUnitType(IntEnum):
    no_separation = 0
    compartments = 1
    fault_blocks = 2
    custom = 3
    
class GsFacDeclineMode(IntEnum):
    linear = 1
    hyperbolic = 2

class GsFacType(IntEnum):
    dp_lift = 3
    pressure_gradient = 4

class ReservoirHorizonSource(IntEnum):
    constant_dip = 0
    horizon_from_db = 1
    
class DipEffectMode(IntEnum):
    no_gravity = 0
    gravity = 1

class ContProps(BaseModel):
    dt: int = Field(30, ge=30, le=150, multiple_of=30,)
    injWBHPCont: bool = Field(False)
    overrideInjWBHP: float = Field(0, ge=0)
    overrideProdBHP: float = Field(0, ge=0)
    overrideInjWMaxP: float = Field(0, ge=0)
    overrideInjWH: float = Field(0, ge=0)
    maximumProdBHP: float = Field(0, ge=0)
    minimumInjWBHP: float = Field(0, ge=0)
    minimumCompLProd: float = Field(0, ge=0)
    minimumCompLInjW: float = Field(0, ge=0)
    loadCompletions: bool = Field(False)
    multiplierMode: bool = Field(False)
    injWRateLoss: float = Field(0, ge=0, le=1)
    useCVSolver: bool = Field(True)
    useDomainsSolver: bool = Field(False)
    gHKernelMode: gHKernelModel = Field(gHKernelModel.each_resmap)
    boundaryType: BoundaryType = Field(BoundaryType.closed)
    reserveMode: ReserveMode = Field(ReserveMode.constant_netpay)
    completionMode: int = Field(2)
    dSol: float = Field(1500, ge=10, le=50000)
    lmda: float = Field(5, ge=0.1, le=100)
    minIter: int = Field(2, ge=2, le=10)
    maxIter: int = Field(10, ge=5, le=30)
    ATol: float = Field(1e-5, ge=1e-6, le=1e-3)
    convTolB: float = Field(1e-5, ge=1e-6, le=1e-2)
    convTolG: float = Field(1e-5, ge=1e-6, le=1e-2)
    convTolO: float = Field(1e-5, ge=1e-6, le=1e-2)
    convTolW: float = Field(1e-5, ge=1e-6, le=1e-2)
    timeOut: int = Field(3600, ge=120, le=6000)
    boundaryDistance: int = Field(3000, ge=10, le=10000)
    interiorPointClearanceDistance: int = Field(1, ge=1, le=1000)
    removeInactiveWells: bool = Field(False)
    minDist: int = Field(500, ge=10, le=10000)
    maxCondNum: int = Field(1e10, ge=1e3, le=1e15)
    cutEndTS: int = Field(0, ge=0)
    cutStartTS: int = Field(0, ge=0)
    dryRunSteps: int = Field(0, ge=0)
    flowUnitType: FlowUnitType = Field(FlowUnitType.no_separation)
    dSProd: float = Field(5, ge=2, le=10000)
    dSInjW: float = Field(5, ge=2, le=10000)
    debug: bool = Field(False)
    gsFacDeclineMode: GsFacDeclineMode = Field(GsFacDeclineMode.hyperbolic)
    decExponent: float = Field(0.0, ge=0.0, le=1.0)
    gsFacType: GsFacType = Field(GsFacType.dp_lift)
    krOBegDeclineMode: int = Field(2) #? Check if this is correct
    isSaveWksp: bool = Field(False)
    nIntPoints: int = Field(300, ge=50, le=500)
    writeState: int = Field(0) #? Check if this is correct
    reservoirHorizonSource: ReservoirHorizonSource = Field(ReservoirHorizonSource.constant_dip)
    dipEffectMode: DipEffectMode = Field(DipEffectMode.no_gravity) #? Check if this is boolean
    nAvgSteps: int = Field(1, ge=1, le=60)
    initMode: int = Field(0)
    explicitInjW: int = Field(0)
    saveMonthTable: int = Field(1)
    
    class Config:
        json_encoders = {
            bool: lambda b: int(b)
        }

    
class StateBounds(BaseModel):
    PoMax: float = Field(7000, gt=0)
    PoMin: float = Field(100, gt=0)
    SwMax: float = Field(0.6, ge=0, lt=1)
    SwMin: float = Field(0.3, ge=0, lt=1)
    SgMax: float = Field(0.3, ge=0, lt=1)
    SgMin: float = Field(0.1, ge=0, lt=1)
    
    @validator('PoMin')
    def check_po_min(cls,v, values):
        if values['PoMax'] <= v:
            raise ValueError('PoMax must be greater than PoMin')
        return v
    
    @validator('SwMin')
    def check_sw_min(cls,v, values):
        if values['SwMax'] <= v:
            raise ValueError('SwMax must be greater than SwMin')
        return v
    
    @validator('SgMin')
    def check_sg_min(cls,v, values):
        if values['SgMax'] <= v:
            raise ValueError('SgMax must be greater than SgMin')
        return v
    
class Ranges(BaseModel):
    PoInit: List[float] = Field([2000,4000], min_items=2, max_items=2)
    SwInit: List[float] = Field([0.3,0.5], min_items=2, max_items=2)
    SgInit: List[float] = Field([0.1,0.2], min_items=2, max_items=2)
    phi: List[float] = Field([0.1,0.3], min_items=2, max_items=2)
    K: List[float] = Field([100,400], min_items=2, max_items=2)
    Cr: List[float] = Field([0.000001,0.00001], min_items=2, max_items=2)
    WIMultInjw: List[float] = Field([0.1,0.3], min_items=2, max_items=2)
    alphaSw: List[float] = Field([0.00002,0.00015], min_items=2, max_items=2)
    dPLift: List[float] = Field([0,4], min_items=2, max_items=2)
    alphaDP: List[float] = Field([0.00001,0.00005], min_items=2, max_items=2)
    muORef: List[float] = Field([5,40], min_items=2, max_items=2)
    muOMin: List[float] = Field([1,2], min_items=2, max_items=2)
    bO: List[float] = Field([-0.001,-0.0001], min_items=2, max_items=2)
    muGRef: List[float] = Field([1,5], min_items=2, max_items=2)
    muGMin: List[float] = Field([0.1,0.2], min_items=2, max_items=2)
    bG: List[float] = Field([-0.001,-0.0001], min_items=2, max_items=2)
    krOEnd: List[float] = Field([0.3,0.7], min_items=2, max_items=2)
    alphaKrO: List[float] = Field([0.000005,0.00001], min_items=2, max_items=2)
    krGEnd: List[float] = Field([0.5,1.0], min_items=2, max_items=2)
    krWEnd: List[float] = Field([0.4,0.7], min_items=2, max_items=2)
    DSg: List[float] = Field([0.001,0.005], min_items=2, max_items=2)
    DSw: List[float] = Field([0.001,0.005], min_items=2, max_items=2)
    kvAq: List[float] = Field([0,0], min_items=2, max_items=2)
    qh: List[float] = Field([-1e-7,1e7], min_items=2, max_items=2)
    
    
class ConstProps(BaseModel):
    Co: float = Field(1e-5, ge=0.0)
    muWRef: float = Field(1, gt=0.0)
    muWMin: float = Field(0.1, gt=0.0)
    bW: float = Field(-0.00001)
    Cw: float = Field(1e-5, ge=0.0)
    rhoO: float = Field(60, ge=0.0)
    rhoW: float = Field(62.4, ge=0.0)
    molG: float = Field(16)
    nG: float = Field(2,gt=0)
    nW: float = Field(2,gt=0)
    krOBeg: float = Field(0.2)
    Pb: float = Field(500, gt=0.0)
    RsoPb: float = Field(0.5, gt=0.0)
    BoPb: float = Field(1.0, gt=0.0)
    Sgc: float = Field(0.0, ge=0.0, lt=1.0)
    Sor: float = Field(0.2, ge=0.0, lt=1.0)
    SwInjW: float = Field(0.8, ge=0.0, lt=1.0)
    Swc: float = Field(0.25, ge=0.0, lt=1.0)
    TRef: float = Field(100)
    pRef: float = Field(14.7, ge=14.7)
    omega: float = Field(1)
    zeta: float = Field(1)
    gasMult: float = Field(1)
    NetPay: float = Field(100, gt=0.0)
    WOC: float = Field(0.0)
    GOC: float = Field(0.0)
    zRef: float = Field(0.0)
    poAq: float = Field(0.0)
    topDip: float = Field(0.0)
    topAzimuth: float = Field(0.0)
    topXRef: float = Field(0.0)
    topYRef: float = Field(0.0)
    topZRef: float = Field(0.0)

    
class AqueonModel(BaseModel):
    caseName: str = Field(..., description="Case Name")
    runMode: RunModeEnum = Field(RunModeEnum.fit, description="Run Mode")
    companyName: str = Field(" ", description="Company Name")
    #? Model level integers meaning
    modelLevel: int = Field(1, description="Model Level")
    #? BadWellIndx Dict Schema
    badWellIndx: Dict = Field({}, description="Bad Well Indx")
    wellGuidList: List[List[str]] = Field(..., description="Well Guid List")
    multList: MultList = Field(MultList(), description="Multipliers")
    reservesData: Union[Dict, ReservesData] = Field({}, description="Reserves Data")
    flowUnit: FlowUnits = Field(FlowUnits(), description="Flow Units")
    isMultiReservoir: bool = Field(False, description="Is Multi Reservoir")
    resBnds: ResBounds = Field(ResBounds, description="Reservoir Bounds")
    enkf: Enkf = Field(Enkf(), description="EnKF")
    contProps: ContProps = Field(ContProps(), description="Continuous Properties")
    stateBnds: StateBounds = Field(StateBounds(), description="State Bounds")
    Rng: Ranges = Field(Ranges(), description="Random Number Generator")
    constProps: ConstProps = Field(ConstProps(), description="Constants Properties")
    
    @validator('wellGuidList', always=True, each_item=True)
    def check_wellis_list(cls,v):
        assert isinstance(v, list), "wellGuidList must be a list"
        assert len(v) == 3, "wellGuidList must be a list of 3 elements"
        assert all(isinstance(i,str) for i in v), "wellGuidList must be a list of 3 strings"
        lenght_chars = [10,2,2]
        
        for i,s in enumerate(v):
            assert len(s) == lenght_chars[i], f"wellGuidList[{i}] must be {lenght_chars[i]} characters long"
        return v
    
    class Config:
        json_encoders = {
            date: lambda d: d.strftime('%Y-%m-%d'),
            bool: lambda b: int(b)
        }