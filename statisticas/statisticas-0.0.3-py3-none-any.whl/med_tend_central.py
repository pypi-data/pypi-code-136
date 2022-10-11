import math

def moda(*args:float):
    # Casos especiais
    if len(args) == 0: raise Exception("Não foram passados valores para a função.")
    if len(args) == 1: return args[0]
    # Organiza todo mundo numa dict
    nums = {}
    for arg in args:
        if arg in nums: nums[arg] += 1
        else: nums[arg] = 1
    # Encontra a moda com base no dict
    moda = args[0]
    for key in nums.keys():
        if nums[moda] < nums[key]: 
            moda = key

    return moda

def moda(*args:str):
    # Casos especiais
    if len(args) == 0: raise Exception("Não foram passados valores para a função.")
    if len(args) == 1: return args[0]
    # Organiza todo mundo numa dict
    strs = {}
    for arg in args:
        if arg in strs: strs[arg] += 1
        else: strs[arg] = 1
    # Encontra a moda com base no dict
    moda = args[0]
    for key in strs.keys():
        if strs[moda] < strs[key]: 
            moda = key

    return moda

def mediana(args:list):
    args.sort()
    print(args)
    if len(args)%2 == 0:
        return (args[int(len(args)/2)] + args[int(len(args)/2)-1])/2
    else:
        return args[int(len(args)/2)]

def media(args:list):
    qtd = len(args)
    soma = sum([x for x in args])
    return soma/qtd