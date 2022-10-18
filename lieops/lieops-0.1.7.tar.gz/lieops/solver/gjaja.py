
'''
Implementation of exact solutions in case of monomials.

References
----------
[1] I. Gjaja: "Monomial factorization of symplectic maps", 
    Part. Accel. 1994, Vol. 43(3), pp. 133 -- 144.
'''

def flow(hamiltonian):
    
    assert len(hamiltonian.keys()) == 1, 'No monomial provided.'
    
    rb = hamiltonian.realBasis()