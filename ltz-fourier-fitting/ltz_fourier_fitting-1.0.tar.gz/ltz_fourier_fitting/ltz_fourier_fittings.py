import matplotlib.pyplot as plt
import numpy as np
def fourier_fitting(function,l,r,step=0,draw_picture=True,precision=1000,precision_per_len=False,best_step=True):
    t=r-l
    mid=(l+r)/2
    f=1/t
    w=2*np.pi/t
    if precision_per_len==True:
        len_dx=1/precision
        if best_step==True:
            step=precision*t/2
    else:
        len_dx=t/precision
        if best_step==True:
            step=precision/2
    step=(int)(step)
    line_x=np.arange(l-mid,r-mid,len_dx)
    ans=function((line_x+mid))
    a0=2*f*np.sum(ans)*len_dx
    y=0*line_x+a0/2
    for i in range(1,step):
        cos_wnx=np.cos(w*i*line_x)
        sin_wnx=np.sin(w*i*line_x)
        ai=2*f*np.dot(cos_wnx,ans)*len_dx
        bi=2*f*np.dot(sin_wnx,ans)*len_dx
        y+=ai*cos_wnx+bi*sin_wnx
    if draw_picture==True:
        line_x+=mid
        plt.rcParams['font.family']='SimHei'
        plt.rcParams['axes.unicode_minus']=False
        line1=plt.plot(line_x,ans,color='red',linewidth=1.5)[0]
        line2=plt.plot(line_x,y,color='blue',linewidth=1.5)[0]
        plt.legend(handles=[line1,line2],labels=['原函数','拟合函数'],loc='best')
        plt.show()
    return y    

def func(x):
    return -1.23*x**3-3.5*x**2+10*x+2.13
#划分微元时不按照单位长度进行，傅里叶级数设置为精度的一半较好;若按照单位长度进行，傅里叶级数设置为len*精度的一般较好