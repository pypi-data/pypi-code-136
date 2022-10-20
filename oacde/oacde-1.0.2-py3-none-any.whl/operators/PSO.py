#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Copyright 2022 Changwu Huang, Hao Bai and Xin Yao

    Particle Swarm Optimization operators (matrix version)
'''
import numpy as np



#!------------------------------------------------------------------------------
#!                                 Pre-requirement
#!------------------------------------------------------------------------------



#!------------------------------------------------------------------------------
#!                                 Moving Operators
#!------------------------------------------------------------------------------
# References:
# [1] A.P. Engelbrecht, Computational intelligence: an introduction, 2007


def update_velocity(v, pos, pos_cbest, pos_sbest, c1, c2, RS, w=1, **kwargs):
    ''' Velocity of particles in star social structure (equivalent to gbestPSO)

        v : 2D-array
            (previous) velocities of particles
        pos : 2D-array
            (previous) positions of particles
        pos_cbest : 2D-array
            cognitive best position found by each particle during its lifetime
        pos_sbest : float | 2D-array
            social best position found by the global swarm (all neighbors) or
            local swarm (several neighbors)
        c1 : float | 1D-array
            positive acceleration constant used to scale the cognitive component
            (i.e., `pos_cbest`)
        c2 : float | 1D-array
            positive acceleration constant used to scale the social component
            (i.e., `pos_sbest`)
        RS : np.random.RandomState
            NumPy's random number generator
        w : float | 1D-array (optional, default=1)
            inertia weight [2] used to scale the previous velocity (i.e., `v`)

        Reference
        ---------
        [1]
        [2] Shi and Eberhart [780]
    '''
    NP, D = pos.shape
    w, c1, c2 = np.ones(NP,)*w, np.ones(NP,)*c1, np.ones(NP,)*c2
    r1 = 0 + 1*RS.uniform(size=[NP, D]) # ensure both sides of [0, 1] are closed
    r2 = 0 + 1*RS.uniform(size=[NP, D])
    product1 = np.multiply(w, v.T).T # inertia velocity
    product2 = np.multiply(c1, r1.T).T * (pos_cbest - pos) # cognitive velocity
    product3 = np.multiply(c2, r2.T).T * (pos_sbest - pos) # social velocity
    return product1 + product2 + product3



#!------------------------------------------------------------------------------
#!                             Social Structure Operators
#!------------------------------------------------------------------------------
def star(pos, fitness, *args, **kwargs):
    ''' Find the best position in the global swarm (all neighbors)

        pos : 2D-array
            positions of particles
        fitness : 1D-array
            fitness corresponding to the particles

        Return
        ------

    '''
    return pos[np.nanargmin(fitness),]


gbest = star # alias for <function star>


#* HB: if fitness has same values, only the 1st one will be returned
def ring(pos, fitness, N_neighbor=2, **kwargs):
    ''' Find the best position in the local swarm (several neighbors)

        pos : 2D-array
            positions of particles
        fitness : 1D-array
            fitness corresponding to the particles
        N_neighbor : int
            number of neighbors
    '''
    _ = [np.roll(fitness, i+1) for i in range(N)]
    _.append(fitness)
    min_fitness = np.roll(np.min(np.vstack(_), axis=0), -int(N/2))
    min_idx = [np.asarray(fitness == f).nonzero()[0][0] for f in min_fitness]
    return pos[min_idx,]


lbest = ring  # alias for <function ring>


def von_neumann(parameter_list):
    ''' Ref: https://www.codewars.com/kata/5b2e5a02a454c82fb9000048
    '''
    pass



#!------------------------------------------------------------------------------
#!                                 Cognitive Operators
#!------------------------------------------------------------------------------
# same as DE's <function select>



#!------------------------------------------------------------------------------
#!                                     TESTING
#!------------------------------------------------------------------------------
def main():
    pass


if __name__ == "__main__":
    main()
