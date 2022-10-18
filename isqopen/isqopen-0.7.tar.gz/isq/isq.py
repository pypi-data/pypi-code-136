import sys
import numpy as np
from .errors import *
import inspect
from .parser import IR, compile
from .config import debug_mode
from .tools import decompose
from .simulator import simulate
from collections import defaultdict
from .mapping import *
from ezQpy import *
import random

def getRandom():
    s = ""
    for i in range(10):
        s += chr(random.randint(97, 122))
    return s     

def shape_satisfy(n):
    if n < 2:
        return False
    while n > 1:
        if n % 2 == 1:
            return False
        n //= 2
    return True


class quantumCor:

    __gate = {}
    __ir = ""

    # add user-define unitary gate
    @staticmethod
    def addGate(name, val):
        if not isinstance(val, (np.ndarray, list)):
            raise CoreError("gate type error: need list or np.array value")
        
        rowS = 0
        if isinstance(val, np.ndarray):
            a,b = val.shape
            if a != b:
                raise CoreError("gate size error: different size of weight and height")
            for i in range(n):
                for j in range(n):
                    if not isinstance(val[i][j], (int, float, complex, np.complex128)):
                        raise CoreError("val error: {} need int/float/complex".format(val[i][j]))
            rowS = a
        else:
            rowS = len(val)
            for i in range(rowS):
                if not isinstance(val[i], list) or len(val[i]) != rowS:
                    raise CoreError("gate size error: different size of weight and height")
                for num in val[i]:
                    if not isinstance(num, (int, float, complex, np.complex128)):
                        raise CoreError("val error: {} need int/float/complex".format(num))
            
        if not shape_satisfy(rowS):
            raise CoreError("gate size error: gate size need power of 2, {} is not satisfied".format(rowS))
        
        flag, res = decompose(val, rowS, name)
        if not flag:
            raise CoreError(res)

        quantumCor.__gate[name] = res
    
    @staticmethod
    def getIR():
        return quantumCor.__ir
    
    @staticmethod
    def getMapping(qubit_num, topo, qcis):
        init_map = get_init_map_by_reverse(qubit_num, topo, qcis)
        mp = Map(qubit_num, topo, qcis, init_map)
        return mp.mapping()
    
    @staticmethod
    def compileFromStr(isq_str, target='qcis', **kwargs):
        ir = IR()
        res = compile(ir, isq_str, target, quantumCor.__gate, kwargs)
        if res == -1:
            raise CoreError(ir.error)
        quantumCor.__ir = ir.out
        return ir.out
    
    @staticmethod
    def simulate(qcis, backend='simulate-fast', shots = 100):
        if backend == 'simulate':
            return dict(simulate(qcis, shots, fast = False))
        elif backend == 'simulate-fast':
            return dict(simulate(qcis, shots, fast = True))
        else:
            raise CoreError('"{}" backend is not support, only "simulate" or "simulate-fast"'.format(backend))

        
    def __init__(self, f, *args, **kwargs):

        self.func = f
        
        self.name = f.__name__
        # get backend, only support 'simulate'/'qcis'
        self.backend = 'simulate'
        if 'backend' in kwargs:
            self.backend = kwargs['backend']
        
        if self.backend not in ['simulate', 'simulate-fast', 'qcis-12bit']:
            raise CoreError('"{}" backend is not support, only "simulate" or "simulate-fast" or "qcis-12bit"'.format(self.backend))

        #get run time
        self.shots = 100
        if self.backend in ['qcis-12bit']:
            self.shots = 12000
        if 'shots' in kwargs:
            self.shots = kwargs['shots']
        
        self.account = None
        if 'account' in kwargs:
            self.account = kwargs['account']
        
        if self.account == None:
            if self.backend in ['qcis-12bit']:
                raise CoreError('need provide cloudplatform account for use "{}" backend'.format(self.backend))
    
        self.max_wait_time = 60
        if 'wait_time' in kwargs:
            self.max_wait_time = kwargs['wait_time']
    

    def __call__(self, *args, **kwargs):

        quantumCor.__ir = ""

        par = self.get_par(*args, **kwargs)
        
        self.check_par(par)
        
        # get isq code
        code = inspect.getdoc(self.func)
        
        # parser isq code, get ir
        ir = IR()
        res = compile(ir, code, 'qcis', quantumCor.__gate, par)
        if res == -1:
            raise CoreError(ir.error)
        
        quantumCor.__ir = ir.out
        #if debug_mode == True:
        #    print(ir.out)
        # run ir in backend
        if self.backend == 'simulate':
            return dict(simulate(ir.out, self.shots, fast = False))
        elif self.backend == 'simulate-fast':
            return dict(simulate(ir.out, self.shots, fast = True))
        elif self.backend == 'qcis-12bit':
            circuit = quantumCor.getMapping(12, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12]], ir.out)
            exp_name = "{}_{}".format(self.name, getRandom())
            query_id = self.account.submit_job(circuit=circuit, exp_name=exp_name, version="1.0", num_shots=self.shots)
            if query_id:
                print('提交任务成功，等待执行')
                result = self.account.query_experiment(query_id, max_wait_time=self.max_wait_time)
                if not result:
                    result = {}
                return result
        else:
            return {}
    
    def get_par(self, *args, **kwargs):
        # parser parameter
        
        partype = inspect.getfullargspec(self.func).annotations
        par = inspect.getfullargspec(self.func).args
        
        if debug_mode == True:
            print("args: ", args)
            print("kwargs: ", kwargs)
            print("par: ", par)
            print("partype: ", partype)

        newpar = {}
        m = len(args)
        n = len(kwargs)
        if (m + n) != len(par):
            raise CoreError("par error: need {} but {}".format(len(par), (m+n)))
        else:
            for i in range(m):
                if par[i] in partype and type(args[i]) != partype[par[i]]:
                    raise CoreError('"{}" type error, need {} but {}'.format(par[i], partype[par[i]], type(args[i])))
                else:
                    newpar[par[i]] = args[i]
            
            for i in range(m, m+n):
                if par[i] not in kwargs:
                    raise CoreError('"{}" not provide'.format(par[i]))
                elif par[i] in partype and type(kwargs[par[i]]) != partype[par[i]]:
                    raise CoreError('"{}" type error, need {} but {}'.format(par[i], partype[par[i]], type(kwargs[par[i]])))
                else:
                    newpar[par[i]] = kwargs[par[i]]
        
        return newpar
    
    def check_par(self, par):

        # check parameter type, only support int/float/list
        for k, v in par.items():
            if isinstance(v, list):
                for idx, val in enumerate(v):
                    if not isinstance(val, (int, float)):
                        raise CoreError('"{}[{}]" type error, isq core only support int/float/list par, but {}'.format(k, idx, type(val)))
            elif not isinstance(v, (int, float, list)):
                raise CoreError('"{}" type error, isq core only support int/float/list par, but {}'.format(k, type(v)))         


class qpu():
    
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
    
    def __call__(self, f):
        cor = quantumCor(f, *self.args, **self.kwargs)
        return cor