from typing import *
from .qtypes import *
import time
from .config import debug_mode
# symbol table
varDic: Dict[VarKey, VarType] = {}
current_type: Literal["Paras", "Local"] = "Local"
var_type: VarType = "int"
#proc_id: ProcedureKey = ''

qDic: Dict[VarKey, RegisterId] = {}
cDic: Dict[VarKey, RegisterId] = {}
qlocalDic: Dict[ProcedureKey, Dict[VarKey, RegisterId]] = {}
clocalDic: Dict[ProcedureKey, Dict[VarKey, RegisterId]] = {}
slocalDic: Dict[ProcedureKey, Dict[VarKey, RegisterId]] = {}
#qParas = {};
#cParas = {};
#qlocalTemp = {};
#clocalTemp = {};

q_cnt: RegisterId = 0
c_cnt: RegisterId = 0


callDic: Dict[ProcedureKey,int] = {}

localVarDic: Dict[ProcedureKey,Dict[VarKey, VarType]] = {}
parasList: Dict[ProcedureKey, List[VarKey]] = {}

# Current procedure.
proc_key: ProcedureKey = ''
local_q_cnt: Dict[ProcedureKey, RegisterId] = {}
local_c_cnt: Dict[ProcedureKey, RegisterId] = {}
local_s_cnt: Dict[ProcedureKey, RegisterId] = {}

# current procedure stack start idx
CSTART = 'SPEC1'
QSTART = 'SPEC2'

'''
gateDic[gateName]: (numberOfQubits, gateSequence)
'''

gateDic: Dict[GateKey, Tuple[int, List[DecomposedGate]]] = {}

# Syntax Tree Node Type:

'''
    topNode
        gateDef : the block of custom quantum gates
		gateDefclause : single  custom quantum gate
			

        defBlock
            qbitDef
            intDef
                varDic[ID] = 'int' | 'qbit' | ['int',n] | ['qbit',n] | 'proc'
                
        progBody
            procBlock()
                localVarDef
                    localDefBlock
                progBlock
                    initStat
                    unitStat
                        Node('unitStat',None,listU)
                        listU = [gateName, numberQubit, qubitList]
                    cintAssign
                        p[0] = Node('cintAssign', [intExpr], term)
                        intExpr
                            expr1
                                ID
                                NUMBER
                            expr2
                            exprM
                    ifStat
                        Node('ifStat',[intExpr1, intExpr2, programBlock], Association)
                        Node('ifStat',[intExpr1, intExpr2, programBlock1, programBlock2], Association)
                    whileStat
                        Node('whileStat',[intExpr1, intExpr2, programBlock], Association)
                    callStat

'''

# varType in Dic
'''
    qbit
    int
    proc
'''

#translation phase
if_cnt: int = 0;
loop_cnt: int = 0;
proc_cnt: int = 0;

#output IR
output: str = "";


msgDic = {
    1000: "词法错误",
    1001: "语法错误",
    1002: "语义错误",
    2000: "输入语言错误",
    3000: "编译成功",
    4000: "参数错误",
    9999: "编译器内部错误",
    5000: "模拟成功",
    6000: "模拟失败",
    7000: "isq核错误"
}


print_ast = False; # Only print AST.


def http_error(msgcode, errmsg, id):
    return {
        "code": 1, 
        "msg": msgDic[msgcode],
        "data": {
            "id": id,
            "error": errmsg
        }
    }

def http_res(msgcode, ir, id):
    return {
        "code": 0,
        "msg": msgDic[msgcode],
        "data":{
            "id": id,
            "qcis": ir.out
        }
    }

def sim_res(msgcode, res, id):
    return {
        "code": 0,
        "msg": msgDic[msgcode],
        "data":{
            "id": id,
            "sim_res": res
        }
    }