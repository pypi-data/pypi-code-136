#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Copyright 2022 Changwu Huang, Hao Bai and Xin Yao

    Differential Evolution operators (matrix version)
'''
import numpy as np



#!------------------------------------------------------------------------------
#!                                 Pre-requirement
#!------------------------------------------------------------------------------
def _get_pbest(pop, fitness, p=0):
    ''' Get the 100p% individuals' indices
        pop : 2D-array
            population including all individuals
        fitness : 1D-array
            fitness corresponding to the population
        p : float (default=0)
            top 100p% idividuals within [0,1]. If p=0, it returns the index of
            the minimum

        Return
        ------
        1D-array : individuals indices
    '''
    if p == 0: # stands for minimum
        return np.nanargmin(fitness)  # if 2 minimums, it returns only the 1st
    else:
        top_p = int(np.ceil(pop.shape[0] * p))
        return np.argsort(fitness)[:top_p]


def _get_cov_pop(pop):
    ''' Calculate the Covariance Matrix of population
        pop : 2D-array
            population including all individuals at shape [NP, D]

        Return
        ------
        Q : 2D-array
            eigenvector basis, a square array of shape [D, D], whose i-th
            column is an eigenvector
        Qct : 2D-array
            conjugate transpose of the eigenvector basis
    '''
    # Each row is the xvalue of an individual, each col is a dimension
    COV = np.cov(pop, rowvar=False)
    # Eigen decomposition of COV:
    # COV is a symmetric matrix, so use eigh() method, which is more quickly
    # than eig().
    # A: eigenvalues; Q: matrix, each column is a eigenvector
    A, Q = np.linalg.eigh(COV)
    Qct = (np.matrix(Q)).H #! HB: the return is in <type np.matrix>
    return Q, np.asarray(Qct)



#!------------------------------------------------------------------------------
#!                                 Mutation Operators
#!------------------------------------------------------------------------------
# References:
# [1] Comparison of mutation strategies in Differential Evolution-A
# probabilistic perspective
# [2] Differential evolution algorithm with ensemble of parameters and
# mutation strategies


def rand_1(pop, F, RS, **kwargs):
    ''' DE/rand/1 mutation operator

        Reference
        ---------
        R. Storn et al., Differential Evolution – A Simple and Efficient
        Heuristic for Global Optimization over Continuous Spaces, 1997
    '''
    _ = np.arange(pop.shape[0])
    r = np.array([RS.choice(np.delete(_, i), 3, replace=False) for i in _])
    product = np.multiply((pop[r[:, 1]] - pop[r[:, 2]]).T, F)
    return pop[r[:, 0]] + product.T


def rand_2(pop, F, RS, **kwargs):
    ''' DE/rand/2 mutation operator

        Reference
        ---------
        A. K. Qin, V. L. Huang and P. N. Suganthan, "Differential Evolution
        Algorithm With Strategy Adaptation for Global Numerical Optimization,"
        in IEEE Transactions on Evolutionary Computation, vol. 13, no. 2,
        pp. 398-417, April 2009, doi: 10.1109/TEVC.2008.927706.
    '''
    _ = np.arange(pop.shape[0])
    r = np.array([RS.choice(np.delete(_, i), 5, replace=False) for i in _])
    product1 = np.multiply((pop[r[:, 1]] - pop[r[:, 2]]).T, F)
    product2 = np.multiply((pop[r[:, 3]] - pop[r[:, 4]]).T, F)
    return pop[r[:, 0]] + product1.T + product2.T


def best_1(pop, F, RS, **kwargs):
    ''' DE/best/1 mutation operator
        fitness : 1D-array
            fitness corresponding to the population

        Reference
        ---------
        R. Storn, "On the usage of differential evolution for function optimization,"
        Proceedings of North American Fuzzy Information Processing, Berkeley,
        CA, USA, 1996, pp. 519-523, doi: 10.1109/NAFIPS.1996.534789.
    '''
    _ = np.arange(pop.shape[0])
    r = np.array([RS.choice(np.delete(_, i), 2, replace=False) for i in _])
    min_idx = _get_pbest(pop, kwargs.get("fitness",np.nan), p=0)
    product = np.multiply((pop[r[:, 0]] - pop[r[:, 1]]).T, F)
    return pop[[min_idx,]*_.size] + product.T


def best_2(pop, F, RS, **kwargs):
    ''' DE/best/2 mutation operator
        fitness : 1D-array
            fitness corresponding to the population

        Reference
        ---------
        R. Storn, "On the usage of differential evolution for function optimization,"
        Proceedings of North American Fuzzy Information Processing, Berkeley,
        CA, USA, 1996, pp. 519-523, doi: 10.1109/NAFIPS.1996.534789.
    '''
    _ = np.arange(pop.shape[0])
    r = np.array([RS.choice(np.delete(_, i), 4, replace=False) for i in _])
    min_idx = _get_pbest(pop, kwargs.get("fitness",np.nan), p=0)
    product1 = np.multiply((pop[r[:, 0]] - pop[r[:, 1]]).T, F)
    product2 = np.multiply((pop[r[:, 2]] - pop[r[:, 3]]).T, F)
    return pop[[min_idx,]*_.size] + product1.T + product2.T


def rand_to_best_1(pop, F, RS, **kwargs):
    ''' DE/rand-to-best/1 mutation operator
        fitness : 1D-array
            fitness corresponding to the population

        Reference
        ---------
        R. Storn, "On the usage of differential evolution for function optimization,"
        Proceedings of North American Fuzzy Information Processing, Berkeley,
        CA, USA, 1996, pp. 519-523, doi: 10.1109/NAFIPS.1996.534789.
    '''
    _ = np.arange(pop.shape[0])
    r = np.array([RS.choice(np.delete(_, i), 3, replace=False) for i in _])
    min_idx = _get_pbest(pop, kwargs.get("fitness", np.nan), p=0)
    product1 = np.multiply((pop[[min_idx, ]*_.size] - pop[r[:, 0]]).T, F)
    product2 = np.multiply((pop[r[:, 1]] - pop[r[:, 2]]).T, F)
    return pop[r[:, 0]] + product1.T + product2.T


def rand_to_pbest_1(pop, F, RS, **kwargs):
    ''' DE/rand-to-pbest/1 mutation operator
        fitness : 1D-array
            fitness corresponding to the population
        p : float
            top 100p% idividuals within (0,1]

        Reference
        ---------
    '''
    _ = np.arange(pop.shape[0])
    r = np.array([RS.choice(np.delete(_, i), 3, replace=False) for i in _])
    p_idx = _get_pbest(pop, kwargs.get("fitness", np.nan),
                       p=kwargs.get("p", 0.2))
    idx = np.array([RS.choice(p_idx[p_idx != i], 1,) for i in _]).reshape(-1,)
    product1 = np.multiply((pop[idx] - pop[r[:, 0]]).T, F)
    product2 = np.multiply((pop[r[:, 1]] - pop[r[:, 2]]).T, F)
    return pop[r[:, 0]] + product1.T + product2.T


def current_1(pop, F, RS, **kwargs):
    ''' DE/current/1 mutation operator

        Reference
        ---------
    '''
    _ = np.arange(pop.shape[0])
    r = np.array([RS.choice(np.delete(_, i), 2, replace=False) for i in _])
    product = np.multiply((pop[r[:, 0]] - pop[r[:, 1]]).T, F)
    return pop + product.T


def current_to_rand_1(pop, F, RS, **kwargs):
    ''' DE/current-to-rand/1 mutation operator

        Reference
        ---------
        Opara, Karol, and Jarosław Arabas. "Comparison of mutation strategies
        in differential evolution–a probabilistic perspective."
        Swarm and Evolutionary Computation 39 (2018): 53-69.
    '''
    _ = np.arange(pop.shape[0])
    r = np.array([RS.choice(np.delete(_, i), 3, replace=False) for i in _])
    # K = RS.rand(_.size,) # use F instead
    product1 = np.multiply((pop[r[:, 0]] - pop).T, F)
    product2 = np.multiply((pop[r[:, 1]] - pop[r[:, 2]]).T, F)
    return pop + product1.T + product2.T


def current_to_best_1(pop, F, RS, **kwargs):
    ''' DE/current-to-best/1 mutation operator
        fitness : 1D-array
            fitness corresponding to the population

        Reference
        ---------
        R. Storn, "On the usage of differential evolution for function optimization,"
        Proceedings of North American Fuzzy Information Processing, Berkeley,
        CA, USA, 1996, pp. 519-523, doi: 10.1109/NAFIPS.1996.534789.
        J. Zhang et al., JADE: Adaptive Differential Evolution With Optional
        External Archive, Oct. 2009
    '''
    _ = np.arange(pop.shape[0])
    r = np.array([RS.choice(np.delete(_, i), 2, replace=False) for i in _])
    min_idx = _get_pbest(pop, kwargs.get("fitness", np.nan), p=0)
    product1 = np.multiply((pop[[min_idx, ]*_.size] - pop).T, F)
    product2 = np.multiply((pop[r[:, 0]] - pop[r[:, 1]]).T, F)
    return pop + product1.T + product2.T


def current_to_best_2(pop, F, RS, **kwargs):
    ''' DE/current-to-best/2 mutation operator
        fitness : 1D-array
            fitness corresponding to the population

        Reference
        ---------
    '''
    _ = np.arange(pop.shape[0])
    r = np.array([RS.choice(np.delete(_, i), 4, replace=False) for i in _])
    min_idx = _get_pbest(pop, kwargs.get("fitness", np.nan), p=0)
    # K = RS.rand(_.size,)
    product1 = np.multiply((pop[[min_idx, ]*_.size] - pop).T, F)
    product2 = np.multiply((pop[r[:, 0]] - pop[r[:, 1]]).T, F)
    product3 = np.multiply((pop[r[:, 2]] - pop[r[:, 3]]).T, F)
    return pop + product1.T + product2.T + product3.T


def current_to_pbest_1(pop, F, RS, **kwargs):
    ''' DE/current-to-pbest/1 mutation operator with optional external archive
        fitness : 1D-array
            fitness corresponding to the population
        p : float
            top 100p% idividuals within (0,1]

        Reference
        ---------
        J. Zhang et al., JADE: Adaptive Differential Evolution With Optional
        External Archive, Oct. 2009
    '''
    _ = np.arange(pop.shape[0])
    # get pbest
    p_idx = _get_pbest(pop, kwargs.get("fitness", np.nan),
                       p=kwargs.get("p", 0.2))
    idx = np.array([RS.choice(p_idx[p_idx != i], 1,) for i in _]).reshape(-1,)
    # get r1 and r2
    pop_archive = kwargs.get("pop_archive")
    if pop_archive is None or pop_archive == []:
        r = np.array([RS.choice(np.delete(_, i), 2, replace=False) for i in _])
        product1 = np.multiply((pop[idx] - pop).T, F)
        product2 = np.multiply((pop[r[:, 0]] - pop[r[:, 1]]).T, F)
        return pop + product1.T + product2.T
    else:
        r1 = np.array([RS.choice(np.delete(_, i), 1,) for i in _]).reshape(-1,)
        pop_union = np.concatenate([pop, pop_archive])
        __ = np.arange(pop_union.shape[0])
        r2 = np.array([RS.choice(np.delete(__, [i, r1[i]]), 1,)
                       for i in _]).reshape(-1,)
        r = np.transpose(np.array([r1, r2]))
        product1 = np.multiply((pop[idx] - pop).T, F)
        product2 = np.multiply((pop[r[:, 0]] - pop_union[r[:, 1]]).T, F)
        return pop + product1.T + product2.T



#!------------------------------------------------------------------------------
#!                                 Crossover Operators
#!------------------------------------------------------------------------------
def bin(pop, pop_mutant, CR, RS, **kwargs):
    ''' Binomial crossover operator

        Reference
        ---------
        R. Storn et al., Differential Evolution – A Simple and Efficient
        Heuristic for Global Optimization over Continuous Spaces, 1997
    '''
    NP, D = pop.shape
    CR = np.multiply(np.ones(NP,), CR)
    # ensure closed sides [0, 1]
    # Ref: https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html
    #? discuss: need to ensure uniform per vector ?
    cond1 = (0 + 1*RS.uniform(size=[NP, D])) <= CR[:, None]
    cond2 = (np.tile(np.arange(D), [NP, 1])) == (RS.randint(0, D, size=[NP, D]))
    return np.where(np.logical_or(cond1, cond2), pop_mutant, pop)


def exp(pop, pop_mutant, CR, RS, **kwargs):
    ''' Exponential crossover operator

        Reference
        ---------
        R. Storn, On the Usage of Differential Evolution for Function
        Optimization, 1996
    '''
    NP, D = pop.shape
    CR = np.multiply(np.ones(NP,), CR)
    cond = []
    for i in np.arange(NP):
        # determine L
        L = 1
        while (RS.uniform() < CR[i]) and (L < D):
            L += 1
        # generate n
        n = RS.randint(low=0, high=D)
        # calculate modulos
        idx = np.unique(np.arange(n, n+L) % D)
        _ = np.full(D, False)
        _[idx] = True
        cond.append(_)
    return np.where(cond, pop_mutant, pop)


def none(pop, pop_mutant, *args, **kwargs):
    ''' None crossover operator
        Return directly the mutant vector as the trial vector
    '''
    return pop_mutant


def eig(pop, pop_mutant, CR, RS, operator=bin):
    ''' Eigenvector-based crossover operator

        Reference
        ---------
        S. Guo et al., Enhancing Differential Evolution Utilizing
        Eigenvector-Based Crossover Operator, Feb. 2015
    '''
    NP, D = pop.shape
    # get eigenvector basis of the population
    Q, Qct = _get_cov_pop(pop)
    # transform to eigenvector basis spacce (through matrix product)
    eig_pop_target = np.matmul(Q, np.transpose(pop))
    eig_pop_mutant = np.matmul(Q, np.transpose(pop_mutant))
    # do bin crossover on eig_pop_target and eig_pop_mutant
    eig_pop_trial = operator(eig_pop_target.T, eig_pop_mutant.T, CR, RS)
    # transform to original space (through matrix product)
    return np.transpose(Qct @ eig_pop_trial.T)



#!------------------------------------------------------------------------------
#!                                 Selection Operators
#!------------------------------------------------------------------------------



#!------------------------------------------------------------------------------
#!                                     TESTING
#!------------------------------------------------------------------------------
def main():
    RS = np.random.RandomState(0)

    pop = np.array([[1,1,1,1],
                    [2,2,2,2],
                    [3,3,3,3],
                    [4,4,4,4],
                    [5,5,5,5]])
    popF = np.array([1,2,3,4,5])

    mut = rand_1(pop=pop, F=0.5, RS=RS)
    print("Mutant: \n", mut)

    trial = none(pop=pop, pop_mutant=mut, CR=0.5, RS=RS)
    print("Trial: \n", trial)

    COV = np.cov(pop, rowvar=False)

    A, Q = np.linalg.eigh(COV)
    print("A: ", A)
    print("Q: ", Q)
    Qct = (np.matrix(Q)).H

    print(Q@np.diag(A)@np.linalg.inv(Q))
    print(COV)

    return mut, trial


if __name__ == "__main__":
    mut = main()
