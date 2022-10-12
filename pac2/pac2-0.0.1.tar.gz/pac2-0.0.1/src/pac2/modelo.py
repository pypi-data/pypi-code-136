class LinearRegresion:
  def __init__(self,x:list,y:list):
    import numpy as np
    import scipy.stats as st
    self.X=x
    self.y=y
    self.x=np.c_[np.ones(len(self.X)),self.X]
  def tabla(self):
    self.betas=np.dot((np.linalg.inv(np.dot(self.x.T,self.x))),(np.dot(self.x.T,self.y)))
    self.y_=np.dot(self.x,self.betas)
    self.ee= sum((self.y-self.y_)**2)
    sigma=self.ee/(self.X.shape[0]-self.X.shape[1])
    self.error =np.sqrt(np.diag(np.linalg.inv(np.dot(self.x.T,self.x))*sigma))
    self.t=self.betas/self.error
    T=st.t(df=self.x.shape[0]-self.x.shape[1])
    self.Pvalor=((1-T.cdf(self.t))*2)
    self.Int_inf=self.betas- self.error*T.ppf(0.975)
    self.Int_sup=self.betas+ self.error*T.ppf(0.975)
    lista=[[" ","Coef","Stde err","T","P>|t|","[0.25","0.975]"]]
    for i in range(0,self.x.shape[1]):
        lista.append([f"B_{i}",self.betas[i], self.error[i], self.t[i] , self.Pvalor[i],self.Int_inf[i], self.Int_sup[i]])
    for fila in lista:
      for elem in fila:
        print(f"{elem:<20}",end=" ")
      print()
    return " "  
  def bp(self):
    X=np.c_[x, np.ones(len(x))]
    err=(self.y - np.dot(self.x,np.dot((np.linalg.inv(np.dot(self.x.T,self.x))),(np.dot(self.x.T,self.y)))))**2
    _err=np.linalg.lstsq(X,err, rcond=None) [0]
    pred_err=np.dot(X,_err)
    ss_tot = sum((err - np.mean(err))**2)
    ss_res = sum((err - pred_err)**2)
    r2 = 1 - (ss_res / ss_tot)
    LM = self.y.shape[0] * r2
    pval =  st.chi2.sf(LM,X.shape[1])
    if pval<0.05:
      en="Se presenta heterocedasticidad"
    else:
      en="No se presenta heterocedasticidad"
    return [LM,pval,en], r2
  def Jb(self):
    err=self.y - np.dot(self.x,np.dot((np.linalg.inv(np.dot(self.x.T,self.x))),(np.dot(self.x.T,self.y))))
    kur=st.kurtosis(err)
    asi=st.skew(err)
    stadistic=self.x.shape[0]*(((asi**2)/6)+(kur**2)/24)
    pval =  st.chi2.sf(stadistic,self.x.shape[1])
    if pval<0.05:
      en="Los errores siguen una distribución normal"
    else:
      en="No hay suficiente evidencia estadistica para considerar que los errores siguen una distribución normal "
    return [stadistic,pval,en]
  def predition(self,a):
    betas = np.dot((np.linalg.inv(np.dot(self.x.T,self.x))),(np.dot(self.x.T,self.y)))
    return betas[0]+np.dot(a,betas[1:])