import pandas as pd
import multiprocessing as mp
from padelpy import from_smiles

cpu= 20
com = len(pd.read_csv('/data/jianping/bokey/OCAICM/dataset/chembl31/error.txt'))
num = int(com/cpu) +1
df = pd.read_csv('/data/jianping/bokey/OCAICM/dataset/chembl31/error.txt')
def convert(data,num,count):

    start ,end= count*num,(count+1)*num-1
    end  = end if end<len(data) else len(data)
    data = data.iloc[start:end,:]

    for smiles in data['Smiles'].tolist():
        try:
            info = from_smiles(smiles,descriptors=True,timeout=100)
            f = open('/data/jianping/bokey/OCAICM/dataset/chembl31/target.txt','a')
            info =list(info.items())
            info = [value[1] for value in info]
            f.write('{},{}\n'.format(smiles,''.join(info)))
            f.close()
        except:
            e = open('/data/jianping/bokey/OCAICM/dataset/chembl31/error.txt', 'a')
            e.write('{}\n'.format(smiles))
            e.close()
p = mp.Pool(processes = cpu)
for i in range(cpu):
    result = p.apply_async(convert, args=(df, num,i))
p.close()
p.join()