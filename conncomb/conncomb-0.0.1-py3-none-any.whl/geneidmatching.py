import mygene
import pandas as pd

def geneIDmatching(geneList,
                   scope, #input
                   field = "ensembl.gene"): #output
    
    if field == "ensembl.gene":
        colName = "ensembl"
    elif field == "entrezgene":
        colName = "entrezgene"
        
        
    #geneID to Emsembl ID
    mg = mygene.MyGeneInfo()
    
    mygeneOutput = mg.querymany(set(geneList), scopes=scope,
                 fields=[field],
                 species="human", returnall=True)
     
        
    out_df=pd.DataFrame.from_dict(mygeneOutput["out"])
    out_df=out_df[out_df[colName].notnull()]
    
    out_df["notfound"]=""

    for i in range(len(out_df)):
        out_df.notfound.iloc[i]=str(type(out_df[colName].iloc[i]))
    #out_df

    for i in range(len(out_df)):
        if "'dict'" in out_df.notfound.iloc[i]:
            out_df.notfound.iloc[i]="dict"
        else:
            out_df.notfound.iloc[i]="list"

    out_df_single = out_df[out_df.notfound == "dict"].reset_index(drop=True)
    #len(out_df_single)

    out_df_mult = out_df[out_df.notfound == "list"].reset_index(drop=True)
    #len(out_df_mult)

    for i in range(len(out_df_single)):
        out_df_single[colName].iloc[i]=out_df_single[colName].iloc[i]["gene"]
    out_df_single=out_df_single.reset_index()

    exp_df=pd.DataFrame(out_df_mult[colName].explode())

    exp_df_all=exp_df.join(out_df_mult[['query', '_id', '_score', 'notfound']])

    exp_df_all=exp_df_all.reset_index()

    for i in range(len(exp_df_all)):
        exp_df_all[colName].iloc[i]=exp_df_all.ensembl.iloc[i]["gene"]
    #exp_df_all

    biggEnsembl = exp_df_all[['query', '_id', '_score', colName]].append(out_df_single[[
        'query', '_id', '_score', colName]]).reset_index(drop=True)
    
    return biggEnsembl