## Script: gem2mtx.ori.py
## Description: Convert GEM to 10x standard matrix directory output (try to accelerate)
## Author: Kevin Lee
## Date: 2021.12.07

import argparse
import sys
from utils import InputStream
from utils import PathType
import pandas as pd
import numpy as np
import os
import gzip

def warn(message):
    prog = os.path.basename(sys.argv[0])
    sys.stderr.write(prog + ": " + message + "\n")

def match(a,b):
    '''
    Depreacted as it's slow
    match = lambda a, b: [ b.index(x)+1 if x in b else None for x in a ]
    '''
    a = list(a)
    b = list(b)
    res = [ b.index(x)+1 if x in b else None for x in a ]
    return res

def binGem(gem_df,binSize):
    warn(' #** binGem(): Aggregate Spot by bin size:' + str(binSize))
    gem_df['xb'] = (np.floor((gem_df['x'] - 1)/binSize) + 1).astype(np.int32)
    gem_df['yb'] = (np.floor((gem_df['y'] - 1) / binSize) + 1).astype(np.int32)

    gem_df_g = gem_df.groupby(['xb','yb','geneID']).agg({'MIDCounts':'sum'})
    gem_df_g.reset_index(inplace=True)
    gem_df_g.columns = ['x','y','geneID','MIDCounts']

    warn('  #** binGem(): Sort gem by coordinate of spots')
    gem_df_g.sort_values(by = ['x','y'],inplace=True)

    warn('  #** binGem(): Add spotID to gem')
    gem_df_g['barcodeID'] =  gem_df_g['x'].astype(str).str.cat(gem_df_g['y'].astype(str), sep='|').apply(lambda x: "{}|{}".format('spot', x))

    return gem_df_g


def runFromArgs(args):
    ## 1. Processing GEM
    warn('##** Prepocessing gem file')
    gem_chunks = pd.read_csv(args.input,sep='\t',chunksize=100000,header=0)
    gem_lst = []
    for gem in gem_chunks:
        gem_lst.append(gem)
    warn(' #** Concatenate chunks of gem')
    gem_df = pd.concat(gem_lst,sort=False)

    warn(' #** Aggregate by binSize')
    gem_df = binGem(gem_df,binSize=args.binSize)

    ## 2. Features
    warn('##** Processing features')
    feature_df = pd.DataFrame({
            'gene_id': gem_df['geneID'].unique(),
            'gene_symbol': gem_df['geneID'].unique(),
            'type': list(np.repeat('Gene Expression', len(gem_df['geneID'].unique())))
    })
    feature_df_m = feature_df.copy()
    feature_df_m['geneIdx'] = feature_df_m.index + 1
    feature_df_m = feature_df_m.loc[:,['gene_id','geneIdx']]

    feature_df.to_csv(os.path.join(args.outDir,'features.tsv.gz'),header=False,index=False,sep='\t',compression='gzip')

    ## 3. Barcodes
    warn('##** Processing spots')
    spot_df = pd.DataFrame(gem_df['barcodeID'].unique(),columns=['barcodeID'])
    spot_df_m =  spot_df.copy()
    spot_df_m['barcodeIdx'] = spot_df_m.index + 1

    spot_df.to_csv(os.path.join(args.outDir,'barcodes.tsv.gz'),header=False,index=False,sep='\t',compression='gzip')

    ## 4. Matrix
    warn('##** Processing matrix')
    #gem_df['geneIdx'] = match(gem_df['geneID'],feature_df['gene_id'])
    #gem_df['spotIdx'] = match(gem_df['barcodeID'],spot_df['barcodeID'])
    #gem_df.head().to_csv(os.path.join(args.outDir,'matrix3.head.mtx'),header=True,index=False,sep='\t')
    #gem_df.to_csv(os.path.join(args.outDir,'matrix3.mtx'),header=True,index=False,sep='\t')

    warn(' #** Merge feature index and spot index with gem')
    gem_df = gem_df.merge(feature_df_m,left_on='geneID',right_on='gene_id',how='left').merge(spot_df_m,on='barcodeID',how='left')

    warn(' #** Sort sparse matrix by spot index and feature index')
    gem_df_s = gem_df.loc[:,['geneIdx','barcodeIdx','MIDCounts']].sort_values(by = ['barcodeIdx','geneIdx'])

    warn(' #** Wirte matrix to file')
    mtx = gzip.open(os.path.join(args.outDir, 'matrix.mtx.gz'), r'wb')
    mtx.write(b'%%MatrixMarket matrix coordinate integer general\n%metadata_json: {"software_version": "cellranger-6.1.1", "format_version": 2}\n')
    mtx.write(b'%s\t%s\t%s\n' % (str(feature_df.shape[0]).encode(),str(spot_df.shape[0]).encode(),str(gem_df_s.shape[0]).encode()))
    gem_df_s.to_csv(mtx,header=False,index=False,sep='\t')
    mtx.close()

if __name__ == "__main__":
    descrition='Convert GEM to 10X standard matrix output.'
    epilog='The input GEM file may be gzipped. If the input file is omitted then input is read from stdin. Output is written to stdout.'
    parser = argparse.ArgumentParser(description=descrition,epilog=epilog)
    parser.add_argument('-i','--input',metavar='<GEM>',default=None,help='BGI GEM file')
    parser.add_argument('-o','--outDir',metavar='<MTX>',default='.', type=PathType(exists=True, type='dir'), help='10X Matrix Directory')
    parser.add_argument('-b','--binSize',metavar='<INT>',default=1, type= np.int32,help='Bin Size to aggregate')

    parser.set_defaults(entry_point=runFromArgs)

    args = parser.parse_args()
    sys.exit(args.entry_point(args))


