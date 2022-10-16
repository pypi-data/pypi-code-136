## Script: utils.py
## Description: Some utilities
## Author: Kevin Lee
## Date: 2021.12.05

import sys
from argparse import ArgumentTypeError as err
import os
import numpy as np
import math
import scanpy as sc
import seaborn as sns


class InputStream(object):
    '''This class handles opening either stdin or a gzipped or non-gzipped file'''

    def __init__(self, string=None):
        '''Create a new wrapper around a stream'''
        if string in (None, '-', 'stdin') and self.valid(string):
            self.handle = sys.stdin
            return
        if string.endswith('.gz'):
            import gzip
            self.handle = gzip.open(string, 'rb')
        else:
            self.handle = open(string, 'r')

    def __enter__(self):
        '''Support use of with by passing back the originating handle'''
        return self.handle

    def __exit__(self, *kwargs):
        '''Support use of with by closing on exit of the context'''
        self.handle.close()

    def __iter__(self):
        '''Support use in loops like a normal file object'''
        return self.handle.__iter__()

    def close(self):
        '''Close the underlying handle'''
        return self.handle.close()


class PathType(object):
    '''
    Refer to answer of @Dan Lenski in https://stackoverflow.com/questions/11415570/directory-path-types-with-argparse
    '''

    def __init__(self, exists=True, type='file', dash_ok=True):
        '''exists:
                True: a path that does exist
                False: a path that does not exist, in a valid parent directory
                None: don't care
           type: file, dir, symlink, None, or a function returning True for valid paths
                None: don't care
           dash_ok: whether to allow "-" as stdin/stdout'''

        assert exists in (True, False, None)
        assert type in ('file', 'dir', 'symlink', None) or hasattr(type, '__call__')

        self._exists = exists
        self._type = type
        self._dash_ok = dash_ok

    def __call__(self, string):
        if string == '-':
            # the special argument "-" means sys.std{in,out}
            if self._type == 'dir':
                raise err('standard input/output (-) not allowed as directory path')
            elif self._type == 'symlink':
                raise err('standard input/output (-) not allowed as symlink path')
            elif not self._dash_ok:
                raise err('standard input/output (-) not allowed')
        else:
            e = os.path.exists(string)
            if self._exists == True:
                if not e:
                    raise err("path does not exist: '%s'" % string)

                if self._type is None:
                    pass
                elif self._type == 'file':
                    if not os.path.isfile(string):
                        raise err("path is not a file: '%s'" % string)
                elif self._type == 'symlink':
                    if not os.path.symlink(string):
                        raise err("path is not a symlink: '%s'" % string)
                elif self._type == 'dir':
                    if not os.path.isdir(string):
                        raise err("path is not a directory: '%s'" % string)
                elif not self._type(string):
                    raise err("path not valid: '%s'" % string)
            else:
                if self._exists == False and e:
                    raise err("path exists: '%s'" % string)

                p = os.path.dirname(os.path.normpath(string)) or '.'
                if not os.path.isdir(p):
                    raise err("parent path is not a directory: '%s'" % p)
                elif not os.path.exists(p):
                    raise err("parent directory does not exist: '%s'" % p)

        return string


'''
Calculate centroid of scatters
'''


def calCentroid(array):
    res = np.average(array,axis=0)
    res = np.reshape(res,(-1,2))
    return res


'''
Move origin to centroid
'''


def origin2centroid(coordArray,centroid):
    res = coordArray - centroid
    return res


'''
Rotate based on centroid
'''


def rotate(angle,coordArray,centroid):
    theta=math.radians(angle)
    rotateMat = np.array([[math.cos(theta),-math.sin(theta)],[math.sin(theta),math.cos(theta)]])
    res = np.dot(rotateMat,coordArray.T-centroid.T)+centroid.T
    return res.T

'''
seq() in python
'''


def seq(start, end, by = None, length_out = None):
    len_provided = True if (length_out is not None) else False
    by_provided = True if (by is not None) else False
    if (not by_provided) & (not len_provided):
        raise ValueError('At least by or n_points must be provided')
    width = end - start
    eps = pow(10.0, -14)
    if by_provided:
        if (abs(by) < eps):
            raise ValueError('by must be non-zero.')
    #Switch direction in case in start and end seems to have been switched (use sign of by to decide this behaviour)
        if start > end and by > 0:
            e = start
            start = end
            end = e
        elif start < end and by < 0:
            e = end
            end = start
            start = e
        absby = abs(by)
        if absby - width < eps:
            length_out = int(width / absby)
        else:
            #by is too great, we assume by is actually length_out
            length_out = int(by)
            by = width / (by - 1)
    else:
        length_out = int(length_out)
        by = width / (length_out - 1)
    out = [float(start)]*length_out
    for i in range(1, length_out):
        out[i] += by * i
    if abs(start + by * length_out - end) < eps:
        out.append(end)
    return out

'''
grep in python
'''


def grep(l, s):
    return [i for i in l if s in i]

'''
Blend plot
'''


def sigmoid(x):
    return  1 / (1 + math.exp(-x))

def hex2rgb(x):
    h = x.lstrip('#')
    return np.asarray(tuple(int(h[i:i+2], 16) for i in (0, 2, 4)))

def rgb2hex(x):
    def clamp(x):
        return max(0, min(x, 255))
    return "#{0:02x}{1:02x}{2:02x}".format(int(clamp(x[0])), int(clamp(x[1])), int(clamp(x[2])))

def blend_color(i, j, col_threshold, n, C0, C1, C2):
    c_min = sigmoid(5 * (1 / n - col_threshold))
    c_max = sigmoid(5 * (1 - col_threshold))
    c1_weight = sigmoid(5 * (i / n - col_threshold))
    c2_weight = sigmoid(5 * (j / n - col_threshold))
    c0_weight = sigmoid(5 * ((i + j) / (n * 2) - col_threshold))
    c1_weight = (c1_weight - c_min) / (c_max - c_min)
    c2_weight = (c2_weight - c_min) / (c_max - c_min)
    c0_weight = (c0_weight - c_min) / (c_max - c_min)
    C1_length = math.sqrt(sum((C1 - C0) ** 2))
    C2_length = math.sqrt(sum((C2 - C0) ** 2))
    C1_unit = (C1 - C0) / C1_length
    C2_unit = (C2 - C0) / C2_length
    C1_weight = C1_unit * c1_weight
    C2_weight = C2_unit * c2_weight
    C_blend = C1_weight * (i - 1) * C1_length / (n - 1) + C2_weight * (j - 1) * C2_length / (n - 1) + (i - 1) * (
                j - 1) * c0_weight * C0 / (n - 1) ** 2 + C0
    C_blend[C_blend > 255] = 255
    C_blend[C_blend < 0] = 0

    return rgb2hex(C_blend)

def blendMatrix(n=10, col_threshold=0.5, two_colors=("#ff0000", "#00ff00"), negative_color="#000000"):
    C0 = hex2rgb(negative_color)
    C1 = hex2rgb(two_colors[0])
    C2 = hex2rgb(two_colors[1])

    blend_matrix = np.empty((n, n), dtype='<U7')
    for i in range(n):
        for j in range(n):
            blend_matrix[i, j] = blend_color(i=i + 1, j=j + 1, col_threshold=col_threshold, n=n, C0=C0, C1=C1, C2=C2)
    return blend_matrix

def blendExpression(gene1,gene2):
    gene1 = np.array([round(i) for i in 9 * (gene1 - min(gene1))/(max(gene1)-min(gene1))])
    gene2 = np.array([round(i) for i in 9 * (gene2 - min(gene2))/(max(gene2)-min(gene2))])
    blend = gene1 + gene2 * 10
    return blend

'''
Scanpy analysis function
'''


def filter_data(adata, min_counts=1000, max_counts=4500, mito_frac=20, min_cells=1):
    '''
    Get boolean array of kept cells and genes
    '''

    bool_min_cell = sc.pp.filter_cells(adata, min_counts=min_counts, inplace=False)
    bool_max_cell = sc.pp.filter_cells(adata, max_counts=max_counts, inplace=False)
    bool_mito_cell = np.asarray(adata.obs['pct_counts_mt'] < mito_frac)
    res_bool_cell = np.logical_and(np.logical_and(bool_min_cell[0], bool_max_cell[0]), bool_mito_cell)

    bool_min_gene = sc.pp.filter_genes(adata, min_cells=min_cells, inplace=False)
    res_bool_gene = bool_min_gene[0]

    '''
    Filter out cells
    '''

    adata_fil = adata[res_bool_cell, res_bool_gene]
    print(f'Number of cells after filtration: {adata_fil.n_obs}')
    print(f'Number of genes after filtration: {adata_fil.n_vars}')

    '''
    Return adata, index of kept cell, index of kept gene
    '''

    return adata_fil, res_bool_cell, res_bool_gene

def normalize_data(adata):
    res = sc.pp.normalize_total(adata,copy=True)
    sc.pp.log1p(res,copy=False)
    return res

def sc_pca(adata,label,hvg):
    adata.var['highly_variable'] = adata.var[hvg]
    temp = sc.pp.pca(adata,copy=True)
    adata.obsm['X_pca_{}'.format(label)] = temp.obsm['X_pca']
    adata.varm['PCs_{}'.format(label)] = temp.varm['PCs']
    adata.uns['pca_{}'.format(label)] = temp.uns['pca']

'''
Plotly graph_objects functions
'''


def snsCol2rgbStr(col_pal):
    res = ['rgb{}'.format(i) for i in col_pal]
    res = np.asarray(res)
    return res

def clusters2rgb(clusters,col_pal):
    clusters = np.asarray(clusters,dtype='int32')
    cluster_num = len(np.unique(clusters))
    col = sns.color_palette(col_pal,cluster_num)
    col_rgb = snsCol2rgbStr(col_pal=col)
    res = col_rgb[clusters]
    return res

'''
Basic analysis functions
 Created: 20220601
 Last edited: 20220601
'''

def checkIfDuplicates_1(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True
    
def intersection(lst1, lst2):
    ''' Intersection of two list'''
    lst3 = [value for value in lst1 if value in lst2]
    return len(lst1), len(lst2), len(lst3), lst3

def getDupItem(listOfElems):
    ''' Get duplicated items in a list'''
    import collections
    dup = [item for item, count in collections.Counter(listOfElems).items() if count > 1]
    try:
        dup[0]
        return dup
    except IndexError:
        print('There are no duplicates! returning None!')
        return None

def getDupIndex(listOfElems):
    ''' Get duplicated index in a list '''
    import collections
    dup = [item for item, count in collections.Counter(listOfElems).items() if count > 1]
    try:
        dup[0]
        dupIdx = []

        for dupElem in dup:
            dupIdx.extend([idx for idx,elem in enumerate(listOfElems) if elem == dupElem ])

        dupIdx.sort()
        return dupIdx
    except IndexError:
        print('There are no duplicates! returning None!')
        return None

def getDupBool(listOfElems):
    ''' Get duplicated items in a list'''
    import collections
    dup = [item for item, count in collections.Counter(listOfElems).items() if count > 1]
    bool = [ elem in dup for elem in listOfElems ]
    return bool

