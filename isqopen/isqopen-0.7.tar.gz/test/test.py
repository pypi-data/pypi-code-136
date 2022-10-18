import sys
sys.path.append("../")

from isq import isq
import time

m = [[1,0,0,0],[0,1,0,0],[0,0,0,-1j],[0,0,1j,0]]
isq.quantumCor.addGate("CY", m)

theta = [0.0]*10

def passcir(s):
    data = s.split('\n')
    cnt = 0
    ans = []
    for qcis in data:
        tmp = qcis.split(' ')
        if len(tmp) == 3 and tmp[2] == '0.0':
            tmp[2] = '{a['+str(cnt)+']}'
            cnt += 1
        ans.append(' '.join(tmp))
    return '\n'.join(ans)


ans = []
for i in range(14):
    with open("vmcqc1.isq") as f:
        cisq = f.read()
        t =  time.time()
        ir = isq.quantumCor.compileFromStr(cisq,termo=i,thetao=theta)
        #print(time.time() - t)
        cir = passcir(ir)
        ans.append(cir)



c = ans[10].format(a = theta)
print(c)