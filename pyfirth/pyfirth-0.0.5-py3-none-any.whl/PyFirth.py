import pandas as pd
import statsmodels.api as sm
import numpy as np
import copy
from scipy import stats
from scipy import special

__version__ = "0.0.5"

def logsig(x):
    """Compute the log-sigmoid function component-wise."""
    out = np.zeros_like(x)
    idx0 = x < -33
    out[idx0] = x[idx0]
    idx1 = (x >= -33) & (x < -18)
    out[idx1] = x[idx1] - np.exp(x[idx1])
    idx2 = (x >= -18) & (x < 37)
    out[idx2] = -np.log1p(np.exp(-x[idx2]))
    idx3 = x >= 37
    out[idx3] = -np.exp(-x[idx3])
    return out



class PyFirth():

    def firth_likelihood(self,beta):
        """
        Note: likelihood based on methods in http://fa.bianp.net/blog/2019/evaluate_logistic/
        This avoids numerical precision issues.
        """
        Z=np.dot(self.model.exog,beta)
        return (-1.0*np.sum((1 - self.model.endog) * Z - logsig(Z)))+0.5*np.linalg.slogdet(-1.0*self.model.hessian(beta))[1]

    def __init__(self,data_table,x_variables,y_variable,hasconst=False):
        """

        Basic implementation of Firth-penalized logistic regression. There are likely better/more efficient Python versions available.
        Based on the implementation from John Lees: https://gist.github.com/johnlees/3e06380965f367e4894ea20fbae2b90d, and the methods described in PMID: 12758140. 
        Note, this implementation is not optimized for speed. Many improvements could be made.

        Parameters
        ----------
        data_table : pd.DataFrame
            Pandas data frame containing endogenous and exogenous variables.
        x_variables : list
            Exogenous variables to use in the regression. Expects list of strings corresponding to columns in dataframe.
        y_variable : string
            Engogenous variable in data_table
        hasconst : bool
            Indicates whether x_variables contains intercept/constant. Default is False. If False, constant is added to the dataframe.

        Returns
        -------
        FirthRegression class

        """

        self.hasconst=hasconst
        self.x_variables=x_variables

        self.X=data_table[x_variables].values
        if self.hasconst==False:
            self.X=np.hstack((np.ones((self.X.shape[0],1)),self.X))
            self.x_variables=['Intercept']+self.x_variables
            self.const_column=0
        else:
            self.const_column=None
            for i in range(self.X.shape[1]):
                if len(np.setdiff1d(self.X[:,i],np.array([1])))==0:
                    self.const_column=i
            if self.const_column is None:
                raise ValueError("Must include constant in data table if hasconst=True")

        self.Y=data_table[y_variable].values.reshape(-1,1)
        self.model=sm.Logit(self.Y, self.X)
        self.firth_model=None

    def fit(self,variables, num_iters=1000,step_limit=100, convergence_limit=1e-6):
        """
        Performs Logistic regerssion infernece using penalized likelihood ratio test for variables (H_0: Beta=0). 
        Note, can be called repeatedly for different variables, including sets of multiple variables. The full model will only be fit once.

        Parameters
        ----------
        variables : list of strings or a single string
            Variables for inference. Can include only single string, which will be transformed into a list.
        num_iters: int
            Number of Newton-Rapheson iterations
        step_limit : int
            Number of steps to allow for step-halving. Default is 100.
        convergence_limit : float
            Threshold for convergence. Based on the norm of the difference between the new and old paramater vector.

        Returns
        -------
        Dict
            Model Log-likelihood
            Table of parameters and their associated effect coefficiencts and standard errors
            P-value for model with free vs restricted (BETA=0) parameters

        """
        if self.firth_model is None:
            self.firth_model = self._newton_rapheson(step_limit,num_iters, convergence_limit)

        if isinstance(variables,list)==False:
            variables=[variables]

        test_variable_indices=[self.x_variables.index(variable) for variable in variables]
        null_blocking_vec=np.ones(self.X.shape[1],dtype=bool)

        for test_variable in test_variable_indices:
            null_blocking_vec[test_variable]=False
        null_model=self._newton_rapheson(step_limit,num_iters,convergence_limit,blocking_vec=null_blocking_vec)
        p_val =stats.chi2.sf(2.0*(self.firth_model['LogLike'] - null_model['LogLike']), len(variables))

        return_model=copy.deepcopy(self.firth_model)
        return_model['PVal']=p_val
        return_model['Flag']=null_model['Flag']|self.firth_model['Flag']
        return return_model

    def _newton_rapheson(self, step_limit,num_iters, convergence_limit,blocking_vec=None):
        # initialize with zeros with intercept set to log-odds of incidence
        start_vec = np.zeros(self.X.shape[1])
        start_vec[self.const_column]=np.log(np.mean(self.Y)/(1.0-np.mean(self.Y)))

        #if blocking_vec is None, then assume unblocked
        if blocking_vec is None:
            blocking_vec=np.ones(start_vec.shape[0],dtype=bool)
        else:
            assert blocking_vec.shape[0]==self.X.shape[1],"Shape of parameter blocking vector does not match the number of covariates. Don't forget to include the intercept."
            start_vec[blocking_vec==False]*=0.0

        beta_iterations = []
        beta_iterations.append(start_vec)

        warn_flag=0
        for i in range(0, int(num_iters)):
            #based on implementation in PMID: 12758140
            pi = self.model.predict(beta_iterations[i])
            W_diag = pi*(1-pi)
            if blocking_vec.sum()==blocking_vec.shape[0]:
                # full inference
                var_covar_mat = np.linalg.pinv(-self.model.hessian(beta_iterations[i]))

                root_W_diag=np.sqrt(W_diag)
                H=np.transpose(self.X*root_W_diag.reshape(-1,1))
                H=np.matmul(var_covar_mat, H)
                H_diag = np.sum(self.X*root_W_diag.reshape(-1,1)*H.T,axis=1)

                U = np.matmul(np.transpose(self.X), self.Y - pi.reshape(-1,1) + (H_diag*(0.5 - pi)).reshape(-1,1))
                new_beta = np.copy(beta_iterations[i])
                new_beta+=np.matmul(var_covar_mat, U).T.ravel()
            else:
                #inference of only the non-blocked parameters, since the others are fixed to zero for LRT 
                blocked_model=sm.Logit(self.Y, self.X[:,blocking_vec])
                var_covar_mat = np.linalg.pinv(-blocked_model.hessian(beta_iterations[i][blocking_vec]))
                root_W_diag=np.sqrt(W_diag)

                H=np.transpose(self.X[:,blocking_vec]*root_W_diag.reshape(-1,1))
                H=np.matmul(var_covar_mat, H)
                H_diag = np.sum(self.X[:,blocking_vec]*root_W_diag.reshape(-1,1)*H.T,axis=1)

                U = np.matmul(np.transpose(self.X[:,blocking_vec]), self.Y - pi.reshape(-1,1) + (H_diag*(0.5 - pi)).reshape(-1,1))                
                new_beta = np.copy(beta_iterations[i])
                new_beta[blocking_vec]+=np.matmul(var_covar_mat, U).T.ravel()
            # step halving
            j = 0

            while self.firth_likelihood(new_beta) < self.firth_likelihood(beta_iterations[i]):

                new_beta = beta_iterations[i] + 0.5*(new_beta - beta_iterations[i])
                j = j + 1
                if (j > step_limit):
                    if (i > 0):
                        print('Warning: Unable to find parameter vector to further optimize likelihood at iteration {0:d}. Convergence Uncertain.\n'.format(i))
                        warn_flag=1
                        new_beta=beta_iterations[i]
                    else:
                        raise ValueError("Unable to find parameter vector to optimize likelihood on first iteration. Try increasing step_limit.")
            beta_iterations.append(new_beta)
            if (np.linalg.norm(beta_iterations[-1][blocking_vec] - beta_iterations[-2][blocking_vec]) < convergence_limit):
                break
        if np.linalg.norm(beta_iterations[-1][blocking_vec] - beta_iterations[-2][blocking_vec]) >= convergence_limit:
            raise ValueError('Firth regression failed failed to converge in {0:d} iterations. Consider increasing iteration number.\n'.format(i+1))
        else:
            fitll = self.firth_likelihood(beta_iterations[-1])
            bse = np.sqrt(np.diagonal(np.linalg.pinv(-self.model.hessian(beta_iterations[-1]))))
            output={'VAR':[],'BETA':[],'SE':[]}
            for i,var in enumerate(self.x_variables):
                output['VAR']+=[var]
                output['BETA']+=[beta_iterations[-1][i]]
                output['SE']+=[bse[i]]

            output=pd.DataFrame(output)
            output.set_index('VAR',inplace=True)
            return {'LogLike':fitll,'ParamTable':output,'Flag':warn_flag}

if __name__=='__main__':
    dta = sm.datasets.fair.load_pandas().data

    #create a rare count dataset by binning affair time into extreme not extreme
    dta["extreme_affairs"] = (dta["affairs"] > 10.0).astype(float)
    dta = sm.add_constant(dta)
    logit_mod = sm.Logit(dta["extreme_affairs"], dta[['const','occupation', 'educ', 'occupation_husb','rate_marriage','age','yrs_married','children','religious']])
    fitted_mod=logit_mod.fit()
    print('Logistic Regression Marriage Rating (Beta, SE, P): {0:.2f}, {1:.2f}, {2:.2e}'.format(fitted_mod.params['rate_marriage'],fitted_mod.bse['rate_marriage'],fitted_mod.pvalues['rate_marriage']))
    
    firth_test=PyFirth(dta,['const','occupation', 'educ', 'occupation_husb','rate_marriage','age','yrs_married','children','religious'],'extreme_affairs',hasconst=True)
    firth_output=firth_test.fit('rate_marriage')
    print('Firth Logistic Regression Marriage Rating (Beta, SE, P): {0:.2f}, {1:.2f}, {2:.2e}'.format(firth_output['ParamTable'].loc['rate_marriage']['BETA'],firth_output['ParamTable'].loc['rate_marriage']['SE'],firth_output['PVal']))

    #run standard logistic regression

