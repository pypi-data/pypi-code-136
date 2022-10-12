class LinearRegression:
  import numpy as np
  import scipy.stats as st
  def __init__(self, x,y):
    import numpy as np
    import scipy.stats as st
    self.b_est = None
    self.ee = None
    self.t = None
    self.p_valor = None
    self.int_confianza = None
    self.x = x
    self.y = y
    self.y_est = None
    self.columns = self.x.columns
    self.jarque_bera = None
    self.LM =None
    self.pval = None
  def __repr__(self): 
    import numpy as np
    import scipy.stats as st
    self.x = np.c_[np.ones(len(self.x)),self.x]
    self.b_est =np.dot(np.linalg.inv(np.dot(self.x.T,self.x)), np.dot(self.x.T,self.y))
    np.random.seed(12345)
    e_est = self.y- np.dot(self.x, self.b_est)
    n, k = self.x.shape
    sigma = np.dot(e_est.T, e_est)/(n-k)
    self.ee = np.sqrt(np.diag(sigma* np.linalg.inv(np.dot(self.x.T,self.x))))
    self.t = self.b_est / (self.ee)
    self.y_est = self.x @ self.b_est
    T = st.t(df = n-k)
    self.p_valor = (2)*(1-T.cdf(self.t))
    self.int_confianza= self.b_est + (self.ee)*(T.ppf(0.975)), self.b_est - (self.ee)*(T.ppf(0.975))
    SRC = np.sum((self.y -self.y_est)**2)
    STC = np.sum((self.y - np.mean(self.y))**2)
    R2 = 1-(SRC/STC)
    errores=self.y - (self.x @ self.b_est)
    asi = st.skew(errores)
    kur = st.kurtosis(errores)
    jb = st.jarque_bera(errores)
    self.jarque_bera = self.x.shape[0]*((((asi)**2)/6) + (((kur)**2)/24))
    chi2= st.chi2(df = self.x.shape[1])
    erros=(self.y - self.x @(np.linalg.inv(self.x.T @self.x) @ (self.x.T @ self.y)))**2
    erros_est = np.linalg.lstsq(self.x, erros, rcond = None) [0]
    erros_predic = self.x @ erros_est
    SS_res =np.sum((erros - erros_predic)**2)
    SS_tot = np.sum((erros - np.mean(erros))**2)
    R2_u = 1-(SS_res/SS_tot)
    self.LM = self.x.shape[0]*R2_u
    self.pval = st.chi2.sf(self.LM,self.x.shape[1])
    chi2 = st.chi2(df = self.x.shape[1]-1)
    variables = ['B_0']
    for j in self.columns:
      variables.append(j)
    lista = [['-------------------------------------------------------------------------------------------------------------------------------------------------'],
             ['|','Number of obs = ', self.x.shape[0], '--Regression ----', '---Results--' ,'R2 =', round(R2,4),'', '|'],
             ['-------------------------------------------------------------------------------------------------------------------------------------------------'],
             ['|','Variable', 'β^','ee', 't', 'p_valor', 'inter inferior', 'inter superior','|']]
    if self.x.shape[1] -1> 1:
      co = self.x.shape[1]
      #self.columns.insert('Constante', 0)
      for i in range(1, co):
        lista.append(['|',variables[i],round(self.b_est[i],7),round(self.ee[i],7),round(self.t[i],7),round(self.p_valor[i],7), round(self.int_confianza[1][i],7),round(self.int_confianza[0][i],7),'|'])
    lista.append(['|','Constante', round(self.b_est[0],7),round(self.ee[0],7),round(self.t[0],7),round(self.p_valor[0],7), round(self.int_confianza[1][0],7), round(self.int_confianza[0][0],7), '|'])
    lista.append(['-------------------------------------------------------------------------------------------------------------------------------------------------'])
    lista.append(['Breush-Pagan =', round(self.LM, 5), 'prueba(bp) =', round(self.pval, 5), 'Jarque -Bera = ', self.jarque_bera, 'prueba(jb) =', 1-chi2.cdf(self.jarque_bera)])
    lista.append(['-------------------------------------------------------------------------------------------------------------------------------------------------'])
    for fila in lista:
      for elem in fila:
        print(f'{elem:<18}', end='')
      print()
    return f'tamaño_tabla: {len(lista)-1, len(lista[0])}'
  def ajuste(self):
    import numpy as np
    import scipy.stats as st
    SRC = np.sum((self.y -self.y_est)**2)
    STC = np.sum((self.y - np.mean(self.y))**2)
    R2 = 1-(SRC/STC)
    return R2
  def fit(self):
    return self.b_est
  def predict(self, datos):
    import numpy as np
    import scipy.stats as st
    '''Ingresar las varibales a predecir'''
    return self.b_est[0] + datos@self.b_est[1::]  
  def Jarque_Bera(self):
    import numpy as np
    import scipy.stats as st
    chi2= st.chi2(df = self.x.shape[1])
    return f'Estadistico: {self.jarque_bera}, p_valor: {1-chi2.cdf(self.jarque_bera)}'

  def Breusch_Pagan(self):
    return f'Estadistico: {self.LM}, p_valor:{self.pval}'