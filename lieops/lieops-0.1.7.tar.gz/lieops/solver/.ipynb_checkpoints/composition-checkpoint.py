

class optimized:
    
    def __init__(self):
        '''
        Optimized composition method of order 8, see 
        https://www.unige.ch/~hairer/poly_geoint/week2.pdf
        
        References
        ----------
        [1] M. Suzuki & K. Umeno, Higher-order decomposition theory of exponential operators and its
        applications to QMC and nonlinear dynamics, Springer Proceedings in Physics 76 (1993) 74–86.
        [2] M. Suzuki, Quantum Monte Carlo methods and general decomposition theory of exponential
        operators and symplectic integrators, Physica A 205 (1994) 65–79.
        [3] R.I. McLachlan, On the numerical integration of ordinary differential equations by symmetric
        composition methods, SIAM J. Sci. Comput. 16 (1995) 151–168.
        '''
        
        gamma1 = 0.74167036435061295344822780
        gamma15 = gamma1
        gamma2 = -0.40910082580003159399730010
        gamma14 = gamma2
        gamma3 = 0.19075471029623837995387626
        gamma13 = gamma3
        gamma4 = -0.57386247111608226665638773
        gamma12 = gamma4
        gamma5 = 0.29906418130365592384446354
        gamma11 = gamma5
        gamma6 = 0.33462491824529818378495798
        gamma10 = gamma6
        gamma7 = 0.31529309239676659663205666
        gamma9 = gamma7
        gamma8 = -0.79688793935291635401978884
                
        self.scheme = [gamma1, gamma2, gamma3, gamma4, gamma5, gamma6, gamma7, gamma8, gamma9, gamma10,
                       gamma11, gamma12, gamma13, gamma14, gamma15]