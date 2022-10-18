import os
from sqlite3 import apilevel
import sys
import numpy as np
import time
import random
from .errors import *
from collections import defaultdict

gate_list = ['H', 'X', 'Y', 'Z', 'S', 'T', 'RZ', 'RX', 'RY', 'SD', 'TD', 'X2M', 'X2P', 'Y2M', 'Y2P', 'CZ', 'CNOT', 'M']

def gateApply(gateName, qubit, alpha, qnum, theta = 0):
    nn = len(alpha)
    a = np.array([[1,0],[0,1]])
    #print(gateName)
    if (gateName in ['H','X','Y','Z','T','S', 'X2M', 'X2P', 'Y2M', 'Y2P', 'SD', 'TD', 'RZ', 'RX', 'RY']):
        if gateName == 'H':
            b = np.sqrt(2)/2
            a = np.array([[b,b],[b,-b]])
        if gateName == 'X':
            a = np.array([[0,1],[1,0]])
        if gateName == 'Y':
            a = np.array([[0,-1j],[1j,0]])
        if gateName == 'Z':
            a = np.array([[1,0],[0,-1]])
        if gateName == 'T':
            a = np.array([[np.exp(-1j*np.pi / 8), 0], [0, np.exp(1j*np.pi / 8)]])
        if gateName == 'S':
            a = np.array([[1,0],[0,1j]])
        if gateName[0:2] == 'RZ':
            a = np.array([[1,0],[0,np.cos(theta)+np.sin(theta)*1j]], dtype=complex)
        if gateName[0:2] == 'RX':
            theta /= 2
            a = np.array([[np.cos(theta),-1j*np.sin(theta)],[-1j*np.sin(theta),np.cos(theta)]], dtype=complex)
        if gateName[0:2] == 'RY':
            theta /= 2
            a = np.array([[np.cos(theta),-1*np.sin(theta)],[np.sin(theta),np.cos(theta)]], dtype=complex)
        if gateName == 'SD':
            a = np.array([[1, 0], [0, -1j]], dtype=complex)
        if gateName == 'TD':
            a = np.array([[np.exp(1j*np.pi / 8), 0], [0, np.exp(-1j*np.pi / 8)]])
        if gateName == 'X2P':
            b = np.sqrt(2)/2
            a = b*np.array([[1, -1j], [-1j, 1]])
        if gateName == 'X2M':
            b = np.sqrt(2)/2
            a = b*np.array([[1, 1j], [1j, 1]])
        if gateName == 'Y2P':
            b = np.sqrt(2)/2
            a = b*np.array([[1, -1], [1, 1]])
        if gateName == 'Y2M':
            b = np.sqrt(2)/2
            a = b*np.array([[1, 1], [-1, 1]])

        
        alpha = reshape_single(alpha, qnum, qubit)
        #alpha = np.tensordot(a, alpha, axes=(1,1))
        alpha[:, 0, :], alpha[:, 1, :] = a[0][0]*alpha[:, 0, :]+a[0][1]*alpha[:, 1, :], a[1][0]*alpha[:, 0, :]+a[1][1]*alpha[:, 1, :]
        alpha = np.ravel(alpha)
        '''
        half_stride = 2**qubit
        stride = 2**(qubit+1)
        beta = np.zeros(half_stride, dtype=complex)
        for i in range(nn//stride):
            offset = i*stride
            beta[:] = a[0,0]*alpha[offset:offset+half_stride] + a[0,1]*alpha[offset+half_stride:offset+stride]
            alpha[offset+half_stride:offset+stride] = a[1,0]*alpha[offset:offset+half_stride] + a[1,1]*alpha[offset+half_stride:offset+stride]
            alpha[offset:offset+half_stride] = beta[:]
        '''
        
    elif gateName in ['CNOT','CX','CZ']:
        
        c,t = qubit
        
        if gateName in ['CX', 'CNOT']:
            if c < t:
                alpha = reshape_double(alpha, qnum, c, t)
                alpha[:,1,:,0,:], alpha[:,1,:,1,:] = alpha[:,1,:,1,:], alpha[:,1,:,0,:]
            else:
                alpha = reshape_double(alpha, qnum, t, c)
                alpha[:,0,:,1,:], alpha[:,1,:,1,:] = alpha[:,1,:,1,:], alpha[:,0,:,1,:]
            alpha = np.ravel(alpha)
        else:
            alpha = reshape_double(alpha, qnum, min(c,t), max(c, t))
            alpha[:,1,:,1,:] *= -1
            alpha = np.ravel(alpha)
        #print(c,t)
        '''
        t_stride = 2**(t+1)
        t_halfstride = 2**t
        c_stride = 2**(c+1)
        c_halfstride = 2**c

        if gateName in ['CX','CNOT']:
            if c > t:
                belta = np.zeros(t_halfstride, dtype=complex)
                for i in range(nn//c_stride):
                    offset = i*c_stride
                    for j in range(c_halfstride//t_stride):
                        offset2 = offset + c_halfstride + j*t_stride
                        belta[:] = alpha[offset2:offset2+t_halfstride]
                        alpha[offset2:offset2+t_halfstride] = alpha[offset2+t_halfstride:offset2+t_stride]
                        alpha[offset2+t_halfstride:offset2+t_stride] = belta[:]
            else: # t > c
                belta = np.zeros(c_halfstride, dtype=complex)
                for i in range(nn//t_stride):
                    offset = i*t_stride
                    for j in range(t_halfstride//c_stride):
                        offset2 = offset + j*c_stride + c_halfstride
                        belta[:] = alpha[offset2:offset2+c_halfstride]
                        alpha[offset2:offset2+c_halfstride] = alpha[offset2+t_halfstride:offset2+c_halfstride+t_halfstride]
                        alpha[offset2+t_halfstride:offset2+c_halfstride+t_halfstride] = belta[:]
        else:
            if c < t:
                t1,t2 = c_stride,c_halfstride
                c_stride,c_halfstride = t_stride,t_halfstride
                t_stride,t_halfstride = t1, t2
            for i in range(nn//c_stride):
                offset = i*c_stride
                for j in range(c_halfstride//t_stride):
                    offset2 = offset + c_halfstride + j*t_stride + t_halfstride
                    alpha[offset2:offset2+t_halfstride] = -alpha[offset2:offset2+t_halfstride]
        '''
    return alpha

def measureApply(qubit, alpha, qnum):
    
    alpha = reshape_single(alpha, qnum, qubit)
    p0 = np.real(np.sum(alpha[:, 0, :] * np.conj(alpha[:, 0, :])))
    res = 0
    if np.random.uniform() < p0:
        alpha[:,1,:] = 0
        alpha /= p0
    else:
        p1 = 1 - p0
        alpha[:,0,:] = 0
        alpha /= p1
        res = 1
    alpha = np.ravel(alpha)
    return res, alpha
    '''
    nn = len(alpha)
    stride = 2**(qubit+1)
    half_stride = 2**qubit
    p0 = 0
    for i in range(nn//stride):
        offset = i*stride
        for j in range(half_stride):
            p0 = p0 + np.abs(alpha[offset+j])**2
    pr = random.random()
    if pr < p0:
        for i in range(nn//stride):
            offset = i*stride
            for j in range(half_stride):
                alpha[offset+j] = alpha[offset+j] / np.sqrt(p0)
                alpha[offset+half_stride+j] = 0
        return 0
    else:
        for i in range(nn//stride):
            offset = i*stride
            for j in range(half_stride):
                alpha[offset+j] = 0
                alpha[offset+half_stride+j] = alpha[offset+half_stride+j] / np.sqrt(1-p0)
        return 1
    '''

def reshape_single(state, qnum, target):
    shape = [1 << target, 2, 1 << (qnum - 1 - target)]
    return np.reshape(state, shape)

def reshape_double(state, qnum, t1, t2):
    shape = [1 << t1, 2, 1 << (t2 - t1-1), 2, 1 << (qnum - t2 - 1)]
    return np.reshape(state, shape)

def simulate(data, run_time = 100, fast = False):

    line_data = data.split('\n')
    qdic = {}
    qnum = 0
    for idx, line in enumerate(line_data):
        if not line:
            continue
        strArr = line.split(' ')
        if strArr[0] not in gate_list:
            raise CoreError('simulate error: in line {}, gate error'.format(idx))
        if len(strArr) < 2 or len(strArr) > 3:
            raise CoreError('simulate error: in line {}, qbit number error'.format(idx))
        if strArr[1][0] != 'Q' or not strArr[1][1:].isdigit():
            raise CoreError('simulate error: in line {}, qbit syntax error'.format(idx))

        if strArr[1] not in qdic:
            qdic[strArr[1]] = qnum
            qnum += 1
        
        if strArr[0] == 'CNOT' or strArr[0] == 'CZ':
            if len(strArr) != 3:
                raise CoreError('simulate error: in line {}, qbit number error'.format(idx))
            
            if strArr[2][0] != 'Q' or not strArr[2][1:].isdigit():
                raise CoreError('simulate error: in line {}, qbit syntax error'.format(idx))

            if strArr[2] not in qdic:
                qdic[strArr[2]] = qnum
                qnum += 1
        if strArr[0] in ['RX', 'RY', 'RZ']:
            if len(strArr) != 3:
                raise CoreError('simulate error: in line {}, qbit number error'.format(idx))
    
    if qnum > 16:
        raise CoreError('simulate error: qbit number out of 16, can not simulate')
    
    alpha = np.zeros(pow(2, qnum), dtype = complex)
    ans = defaultdict(int)
    Mq = []
    for iter_round in range(run_time):
        alpha[:] = 0
        alpha[0] = 1
        res = ''
        for idx, line in enumerate(line_data):
            if not line:
                continue
            strArr = line.split(' ')
            qid1 = qdic[strArr[1]]
            if strArr[0] == 'M':
                if fast:
                    Mq.append(qid1)
                    continue
                mres, alpha = measureApply(qid1, alpha, qnum)
                res += str(mres)
            else:
                qbit = qid1
                theta = 0
                if strArr[0] == 'CNOT' or strArr[0] == 'CZ':
                    qid2 = qdic[strArr[2]]
                    qbit = (qid1, qid2)
                if strArr[0] in ['RX', 'RY', 'RZ']:
                    theta = float(strArr[2])

                alpha = gateApply(strArr[0], qbit, alpha, qnum, theta)
        if fast: break
        ans[res] += 1
    
    if fast:
        for iter_round in range(run_time):
            qvec = alpha.copy()
            res = ''
            for qidx in Mq:
                mres, qvec = measureApply(qidx, qvec, qnum)
                res += str(mres)
            ans[res] += 1
    return ans


if __name__ == '__main__':
    # file_name = sys.argv[1];
    data = ''

    filename = 'output.txt'
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    testing_mode = True
    if testing_mode:
        file_in = open(filename,'r')
        data = file_in.read()
        file_in.close()
    else:
        try:
            while True:
                ssttrr = input()
                data = data + ssttrr + '\n'
        except EOFError:
            pass

    start_time = time.time()
    
    res = simulate(data, "test")
    if res['code'] == 0:
        print(res['data']['sim_res'])
    else:
        print(res)
    end_time = time.time()

