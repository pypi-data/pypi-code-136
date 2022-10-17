# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 22:40:26 2022

@author: eda_c
"""
import networkx as nx
from cobra.io import read_sbml_model
import cobra
import numpy as np
import pandas as pd
from scipy import sparse

from geneIDmatching import geneIDmatching


def buildRecon(pathtosave = "networks/", reconlist = ["recon2", "recon3D"], currencyMethRange = range(0,9)):
    
    for i in reconlist:
        for j in currencyMethRange:
            
           
            geneCentricDF = geneCentricMetabolicNetworkDF(i, currencyPercentage=j)
    
            G = metabolicNetwork(geneCentricMetabolicNetwork = geneCentricDF,
                                 scope="entrezgene",
                                 field = "ensembl.gene")
            
            name = pathtosave+i+"_CurrMet"+str(j)+".gexf"
            
            nx.write_gexf(G, name)




def geneCentricMetabolicNetworkDF(reconModel, currencyPercentage):
    
    """
    Given the recon2/recon3D model and the percentage of currency metabolites to be eliminated,
    this function builds the gene centric metabolic network dataframe.
    
    reconModel = "recon2" / "recon3D"
    currencyPercentage = 2
    
    """
    if reconModel == "recon2":
        model = read_sbml_model("../../recon2/updated_recon2.v03.xml")
    elif reconModel == "recon3D":
        model = read_sbml_model("../../recon3D/Recon3D.xml")
    
    print(model)
    print("Number of metabolites : {}".format(len(model.metabolites)))
    print("Number of reactions : {}".format(len(model.reactions)))
    print("Number of genes : {}".format(len(model.genes)))
    
    #stoichiometric matrix
    N=cobra.util.array.create_stoichiometric_matrix(model)
    Nbin = np.where(N == 0, 0, 1)
    
    #metabolite-reaction dataframe
    df_N=pd.DataFrame(Nbin, columns=model.reactions, index=model.metabolites)
    
    #eliminate currency metabolites
    df_N["count"]=df_N.sum(axis=1)
    df_N=df_N.sort_values(by="count", ascending=False)
    
    topMetabolites=int(np.round(len(df_N)*currencyPercentage/100))
    
    #metabolite-reaction dataframe without currency metabolites
    df_N_woCur = df_N.iloc[topMetabolites:len(df_N)]
    print("\ncurrency metabolites: {} metabolites are eliminated".format(topMetabolites))
    
    #stoichiometric matrix & transpose
    N_woCur = sparse.csr_matrix(df_N_woCur.iloc[:,:-1].to_numpy())
    N_woCur_T = sparse.csr_matrix(N_woCur.T)
    
    #reaction-reaction matrix
    adj_reaction=N_woCur_T.dot(N_woCur)
    
    #gene list
    geneList0=[]
    for gene in model.genes:
        geneList0.append(gene.id.split(".", 1)[0])

    geneList=[]
    for gene in geneList0:
        geneList.append(gene.split("_", 1)[0])
    
    #reaction gene matrix
    rxnGeneDF = rxnGeneMat(model).to_numpy()
        
    #gene-centric GT.ST.S.G
    rxnGeneDF = sparse.csr_matrix(np.where(rxnGeneDF == 0, 0, 1))
    rxnGeneDF_T=sparse.csr_matrix(rxnGeneDF.T)

    geneCentric1 = rxnGeneDF_T.dot(adj_reaction)
    geneCentric = geneCentric1.dot(rxnGeneDF)
    
    geneCentric = geneCentric.toarray()
    geneCentricBin = np.where(geneCentric == 0, 0, 1)

    geneCentricDF=pd.DataFrame(geneCentricBin, columns=geneList, index=geneList)
    
    #eliminate duplicate genes
    geneCentricDFnoDUP = geneCentricDF.loc[~geneCentricDF.index.duplicated(keep='first'),
                                           ~geneCentricDF.columns.duplicated()]
    
    print("\nGene centric metabolic network: {}".format(geneCentricDFnoDUP.shape))
    
    return geneCentricDFnoDUP





def rxnGeneMat(model):
    # make a matrix for rxnGeneMat
    # reactions are rows, genes are columns
    rxn_gene = sparse.dok_matrix((len(model.reactions), len(model.genes)))
    if min(rxn_gene.shape) > 0:
        for i, reaction in enumerate(model.reactions):
            for gene in reaction.genes:
                rxn_gene[i, model.genes.index(gene)] = 1

    rxn_gene_df=pd.DataFrame.sparse.from_spmatrix(rxn_gene)
    
    return rxn_gene_df



def metabolicNetwork(geneCentricMetabolicNetwork, scope="entrezgene", field="ensembl.gene"):
    
    """
    Given the dataframe of gene centric metabolic network,
    this function builds the graph with ensembl IDs.
    """
    
    #adjacency matrix to edge list
    edgeList = geneCentricMetabolicNetwork.stack().reset_index()

    #filter edges (value should be 1)
    edgeList = edgeList[edgeList.iloc[:, 2]==1].reset_index(drop=True)
    edgeList=edgeList.rename(columns={"level_0": "node1", "level_1":"node2"})
    edgeList = edgeList[edgeList.node1 != edgeList.node2]
    
    #ID matching
    geneListFinal=set(edgeList.node1).union(set(edgeList.node2))
    
    print("\nID mapping")
    biggEnsembl = geneIDmatching(geneListFinal, scope=scope, field = field)
    
    
    if field == "ensembl.gene":
        colName = "ensembl"
    elif field == "entrezgene":
        colName = "entrezgene"
    
    
    #dataframe    
    edgeList1=pd.merge(left=edgeList[["node1", "node2"]], right=biggEnsembl[["query", colName]],
                   left_on="node1", right_on="query", how="left")

    edgeList2=pd.merge(left=edgeList1, right=biggEnsembl[["query", colName]],
                       left_on="node2", right_on="query", how="left")
    
    EdgeList = edgeList2[[str(colName+"_x"), str(colName+"_y")]].dropna().reset_index(drop=True)

    EdgeList = EdgeList.drop_duplicates(ignore_index=True)
    
    #graph
    G = nx.Graph(name="Gene Centric Metabolic Network")

    for i, edges_row in EdgeList.iterrows():
        G.add_edge(edges_row[0], edges_row[1])

    G.remove_edges_from(nx.selfloop_edges(G))
    
    print("\n")
    print(nx.info(G))
    
    return G