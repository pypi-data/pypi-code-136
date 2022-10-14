import numpy as np
import skfuzzy
# ------------------------------------------------------------------------------------------------------------------
# GOBC-PA: A new unconstrained global optimization method based on clustering and parabolic approximation
# (GOBC-PA) is proposed. Although the proposed method is basically similar to other
# evolutionary and stochastic methods, it represents a significant advancement of global optimization
# technology for four important reasons. First, it is orders of magnitude faster than existing optimization
# methods for global optimization of unconstrained problems. Second, it has significantly better repeatability,
# numerical stability, and robustness than current methods in dealing with high dimensionally
# and many local minima functions. Third, it can easily and faster find the local minimums using the
# parabolic approximation instead of gradient descent or crossover operations. Fourth, it can easily
# adapted to any theoretical or industrial systems which are using the heuristic methods as an intelligent
# system. In this study, we assume that the best cluster center gives the
# position of the possible global optimum. The usage of clustering and curve fitting techniques brings
# multi-start and local search properties to the proposed method. The experimental studies show that
# the proposed methodology is simple, faster and, it demonstrates a superior performance
# when compared with some state of the art methods.

# Arguments: (input)
# func         - objective function as text
# rang         - range of search space
# target       - target function value. That value used for measuring error.
# N            - dimension number of objective function
# ite          - Maximum iteration
# pop_size     - population size

# Arguments: (output)
# Best_point   - Global minimum points
# Best_result  - Global minimum value on global minimum points
# perf         - errors list
# broken_epoch - epoch number of code break
# performance  - best points and their objective value on each epoch

# Example usage:
# import numpy as np
# from GOBC_PA import GOBC_PA
# def func(x):  # Rastrigin function
#     y= x[0]**2+x[1]**2-np.cos(18*x[0])-np.cos(18*x[1])
#     return y
# # min range values for each dimension are in the first row, max range values for each dimension are in the second row
# rang = np.array([[-1,-1],[1, 1]])
# target = -2
# N,ite,pop_size = 2,1000,60
# Best_point, Best_result, perf, broken_epoch, performance = GOBC_PA(func,rang,target,N,ite,pop_size)

# Cite:
# Pence, I., Cesmeli, M. S., Senel, F. A., & Cetisli, B. (2016).
# A new unconstrained global optimization method based on clustering and parabolic approximation. Expert Systems with Applications, 55, 493-507.
# ------------------------------------------------------------------------------------------------------------------

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#                         OBJECTIVE FUNCTION
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def Calc_func_values(popu,func):
    output=np.empty(shape=[popu.shape[0], 1])
    for i in range(popu.shape[0]):
        output[i,0]=func(popu[i,:])
    return output
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def GOBC_PA(func,rang,target,N,ite,pop_size):
    import warnings
    warnings.filterwarnings("ignore")

    param_n=N                      # dimension number of objective function
    epoch=ite                     # Epoch size 1000
    p_size=pop_size                   # Population size 60
    limit=1e-32                       # Parameter for breaking code
    kume=int(np.ceil(p_size/3))       # Number of cluster size
    size_kum=int(np.ceil(kume/3))   # Number of best clusters size
    size_pop=2                        # Number of best population size for creating new populations around them
    ma=rang[[1],:]                    # max range
    mi=rang[[0],:]                     # min range

    mi_temp=mi
    ma_temp=ma
    mi=np.empty(shape=[0, param_n])
    ma=np.empty(shape=[0, param_n])
    for im in range(p_size):
        mi = np.append(mi, mi_temp, axis=0)
        ma = np.append(ma, ma_temp, axis=0)

    performance = np.empty(shape=[0, param_n+1])
    perf = np.empty(shape=[0, 1])

    popu=mi+(ma-mi)*np.random.rand(p_size,param_n)   # First population created randomly

    evali=Calc_func_values(popu,func)    # Estimate populations objective values
    vv=evali.argsort(axis=0)
    broken_epoch=epoch

    for i in range(epoch):
        c, t, u0, d2, jm, p2, fpc = skfuzzy.cluster.cmeans(np.concatenate((popu,evali), axis=1), kume, 2, error=1e-5, maxiter=2)
        # cluster_membership = np.argmax(t, axis=0)
        t[:,[-1]] = Calc_func_values(t[:,0:-1], func) # Estimate populations objective values

        kk = t[:,[-1]].argsort(axis=0)
        mm=np.argmax(c, axis=0)
        n=size_kum

        cc,brk = 0,0
        while cc<n:
            rr = np.argwhere(mm == kk[cc])
            if rr.size == 0:
                kk=np.append(kk, [kk[cc]], axis=0)
                kk=np.delete(kk, cc, 0)
            else:
                cc+=1

            brk += 1
            if brk>=kume:
                break

        tr_temp = mm
        pop_new = np.empty(shape=[0, param_n])

        for j in range(size_kum):
            # Parabolic approximation starts
            x_yer = np.array([tr_temp == kk[j]]).T
            x_yer=x_yer[:,0]
            if np.sum(x_yer) > 2:
                A = np.concatenate((popu[x_yer,:]**2 , popu[x_yer,:] , np.ones((np.sum(x_yer), 1))), axis=1)
                param = np.dot(np.dot(np.linalg.pinv(np.dot(A.T,A)),A.T),evali[x_yer])
                tepe = (-param[param_n:-1] / (2 * param[0:param_n]))

                ind = param[param_n:-1] == 0
                tepe[ind] = 0
                ind = np.sign(param[0:param_n]) < 0
                tepe[ind] = t[kk[j], np.append(ind,False)]

                if sum(np.isnan(tepe)) == 0 and sum(np.isinf(tepe)) == 0:
                    t[kk[j], 0:-1]=tepe.T
            # Parabolic approximation ends

            kume_eleman_std = np.std(popu[x_yer,:],axis=0)   # Estimate the standart derivation of populations which are members of clusters
            kume_eleman_std=kume_eleman_std[np.newaxis,:]
            if kume_eleman_std.shape[1] == 1:         # If the cluster has one member fix the standart derivation
                kume_eleman_std = np.ones((1, param_n))

            pop_new = np.concatenate((pop_new, ((1/(i+1)) * np.concatenate((kume_eleman_std,kume_eleman_std,kume_eleman_std), axis=0) * (np.random.rand(3,param_n)*2 -1)) + np.concatenate((t[kk[j], 0:-1], t[kk[j], 0:-1], t[kk[j], 0:-1]), axis=0)), axis=0)


        pop_best = np.empty(shape=[0, param_n])
        pp_temp = ((np.max(popu, axis=0) - np.min(popu, axis=0)) / (2 * kume))
        pp_temp = pp_temp[np.newaxis,:]
        pp_best_temp = np.concatenate((pp_temp, pp_temp, pp_temp), axis=0)

        for j in range(size_pop):
            pop_best = np.concatenate((pop_best,(pp_best_temp*(np.random.rand(3,param_n)*2 -1))+np.concatenate((popu[vv[j],:],popu[vv[j],:],popu[vv[j],:]), axis=0)), axis=0)


        popu = np.concatenate((popu[vv[0],:],popu[vv[1],:],t[kk[0:size_kum,0], 0:param_n],pop_new,pop_best), axis=0)

        mi_temp = rang[[0], :]
        ma_temp = rang[[1], :]
        mi = np.empty(shape=[0, param_n])
        ma = np.empty(shape=[0, param_n])
        for im in range(p_size-popu.shape[0]):
            mi = np.append(mi, mi_temp, axis=0)
            ma = np.append(ma, ma_temp, axis=0)

        # ------------------------------------------------------------------------
        popu = np.concatenate((popu,mi + (ma - mi) * np.random.rand(p_size-popu.shape[0], param_n)), axis=0)
        popu[-1]=np.round(popu[vv[0],:])

        # constrained the population in search space
        for im in range(param_n):
            ind = popu[:, im] > ma[0, im]
            popu[ind, im] = ma[0, im]
            ind = popu[:, im] < mi[0, im]
            popu[ind, im] = mi[0, im]
        # ------------------------------------------------------------------------

        ind = np.sum(np.isnan(popu),axis=1) > 0

        if sum(ind) > 0:
            nan_temp = rang[[0],:] + (rang[[1],:]-rang[[0],:]) * np.random.rand(sum(ind), param_n)
            popu[ind]=nan_temp


        evali = Calc_func_values(popu, func)  # Estimate populations objective values
        vv = evali.argsort(axis=0)

        performance=np.append(performance,np.concatenate((popu[vv[0],:], evali[vv[0]]), axis=1), axis=0)
        perf = np.append(perf, np.absolute(target - evali[vv[0]]), axis=0)
        if perf[i] < limit:   # Breaking code
            broken_epoch = i+1
            break


    Best_point = popu[vv[0],:]
    Best_result = evali[vv[0],0]

    print('Best points: ',Best_point)
    print('Best result for best points: ',Best_result)
    print('target: ',target)
    print('error: ',perf[-1])
    print('broken_epoch: ',broken_epoch)

    return Best_point, Best_result, perf, broken_epoch, performance