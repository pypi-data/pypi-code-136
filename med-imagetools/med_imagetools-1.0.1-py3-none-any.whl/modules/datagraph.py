import os, time, pathlib
from typing import List
from functools import reduce
import numpy as np
import pandas as pd
from tqdm import tqdm


class DataGraph:
    '''
    This class given the crawled dataset in the form of CSV file, deals with forming a graph on the full dataset, taking advantage of connections between different modalities. Based
    on these connections, an edge table is made. This class also supports querying and for a given query, returns the file locations of the user-specified sub-dataset from the full dataset.
    The graph is made based on the references made by different DICOMS. Different connections are given different edge type values, to make parsing easier. The edge types are as follows:-
    1) edge_type:0 RTDOSE(key:ref_rt) -> RTSTRUCT(pair: series/instance)
    2) edge_type:1 RTDOSE(key:ref_ct) -> CT(pair: series) 
    3) edge_type:2 RTSTRUCT(key:ref_ct) -> CT(pair: series) 
    4) edge_type:3 RTSTRUCT(key:ref_ct) -> PT(pair: series) 
    5) edge_type:4 CT(key:study) -> PT(pair: study) 
    6) edge_type:5 RTDOSE(key: ref_pl) -> RTPLAN(pair: instance)
    7) edge_type:6 RTPLAN(key: ref_rs) -> RTSTRUCT(pair: series/instance)

    Once the edge table is formed, one can query on the graph to get the desired results. For uniformity, the supported query is list of modalities to consider
    For ex:
    query = ["CT","RTDOSE","RTSTRUCT","PT], will return interconnected studies containing the listed DICOM modalities. The interconnected studies for example may look like 
    (RTDOSE->RTSTRUCT->CT<-PT<-RTSTRUCT)
    '''
    def __init__(self,
                 path_crawl: str,
                 edge_path: str = "./patient_id_full_edges.csv",
                 visualize: bool = False) -> None:
        '''
        Parameters
        ----------
        path_crawl
            The csv returned by the crawler

        edge_path
            This path denotes where the graph in the form of edge table is stored or to be stored
        '''
        self.df = pd.read_csv(path_crawl, index_col=0)
        self.edge_path = edge_path
        self.df_new = None
        if os.path.exists(self.edge_path):
            print("Edge table is already present. Loading the data...")
            self.df_edges = pd.read_csv(self.edge_path)
        else:
            print("Edge table not present. Forming the edge table based on the crawl data...")
            self.form_graph()
        if visualize:
            self.visualize_graph()
    
    def form_graph(self):
        '''
        Forms edge table based on the crawled data
        '''
        #Get reference_rs information from RTDOSE-RTPLAN connections
        df_filter = pd.merge(self.df, self.df[["instance_uid","reference_rs"]], 
                             left_on="reference_pl", 
                             right_on="instance_uid", 
                             how="left")
        
        df_filter.loc[(df_filter.reference_rs_x.isna()) & (~df_filter.reference_rs_y.isna()),"reference_rs_x"] = df_filter.loc[(df_filter.reference_rs_x.isna()) & (~df_filter.reference_rs_y.isna()),"reference_rs_y"].values
        df_filter.drop(columns=["reference_rs_y", "instance_uid_y"], inplace=True)
        df_filter.rename(columns={"reference_rs_x":"reference_rs", "instance_uid_x":"instance_uid"}, inplace=True)
        
        #Remove entries with no RTDOSE reference, for extra check, such cases are mostprobably removed in the earlier step
        df_filter = df_filter.loc[~((df_filter["modality"] == "RTDOSE") & (df_filter["reference_ct"].isna()) & (df_filter["reference_rs"].isna()))]

        #Get all study ids
        # all_study = df_filter.study.unique()
        start = time.time()

        #Defining Master df to store all the Edge dataframes
        # self.df_master = []

        # for i in tqdm(range(len(all_study))):
            # self._form_edge_study(df_filter, all_study, i)

        # df_edge_patient = form_edge_study(df,all_study,i)
        
        self.df_edges = self._form_edges(self.df) #pd.concat(self.df_master, axis=0, ignore_index=True)
        end = time.time()
        print(f"\nTotal time taken: {end - start}")


        self.df_edges.loc[self.df_edges.study_x.isna(),"study_x"] = self.df_edges.loc[self.df_edges.study_x.isna(), "study"]
        #dropping some columns
        self.df_edges.drop(columns=["study_y", "patient_ID_y", "series_description_y", "study_description_y", "study"],inplace=True)
        self.df_edges.sort_values(by="patient_ID_x", ascending=True)
        print(f"Saving edge table in {self.edge_path}")
        self.df_edges.to_csv(self.edge_path, index=False)

    def visualize_graph(self):
        """
        Generates visualization using Pyviz, a wrapper around visJS. The visualization can be found at datanet.html
        """
        from pyvis.network import Network # type: ignore (PyLance)
        print("Generating visualizations...")
        data_net = Network(height='100%', width='100%', bgcolor='#222222', font_color='white')

        sources = self.df_edges["series_y"]
        targets = self.df_edges["series_x"]
        name_src = self.df_edges["modality_y"] 
        name_tar = self.df_edges["modality_x"]
        patient_id = self.df_edges["patient_ID_x"]
        reference_ct = self.df_edges["reference_ct_y"]
        reference_rs = self.df_edges["reference_rs_y"]

        data_zip = zip(sources,targets,name_src,name_tar,patient_id,reference_ct,reference_rs)

        for i in data_zip:
            data_net.add_node(i[0],i[2],title=i[2],group=i[4])
            data_net.add_node(i[1],i[3],title=i[3],group=i[4])
            data_net.add_edge(i[0],i[1])
            node = data_net.get_node(i[0])
            node["title"] = "<br>Patient_id: {}<br>Series: {}<br>reference_ct: {}<br>reference_rs: {}".format(i[4],i[0],i[5],i[6])
            node = data_net.get_node(i[1])
            node["title"] = "<br>Patient_id: {}<br>Series: {}<br>reference_ct: {}<br>reference_rs: {}".format(i[4],i[1],i[5],i[6])

        neigbour_map = data_net.get_adj_list()
        for node in data_net.nodes:
            node["title"] += "<br>Number of connections: {}".format(len(neigbour_map[node['id']])) 
            node["value"] = len(neigbour_map[node['id']])


        vis_path = pathlib.Path(os.path.dirname(self.edge_path),"datanet.html").as_posix()
        data_net.show(vis_path)

    def _form_edges(self, df):
        '''
        For a given study id forms edge table
        '''

        df_list = []

        # Split into each modality
        plan = df[df["modality"] == "RTPLAN"]
        dose = df[df["modality"] == "RTDOSE"]
        struct = df[df["modality"] == "RTSTRUCT"]
        ct = df[df["modality"] == "CT"]
        mr = df[df["modality"] == "MR"]
        pet = df[df["modality"] == "PT"]

        edge_types = np.arange(7)
        for edge in edge_types:
            if edge==0:    # FORMS RTDOSE->RTSTRUCT, can be formed on both series and instance uid
                df_comb1    = pd.merge(struct, dose, left_on="instance_uid", right_on="reference_rs")
                df_comb2    = pd.merge(struct, dose, left_on="series", right_on="reference_rs")
                df_combined = pd.concat([df_comb1, df_comb2])
                #Cases where both series and instance_uid are the same for struct
                df_combined = df_combined.drop_duplicates(subset=["instance_uid_x"])

            elif edge==1:  # FORMS RTDOSE->CT 
                df_combined = pd.merge(ct, dose, left_on="series", right_on="reference_ct")

            elif edge==2:  # FORMS RTSTRUCT->CT on ref_ct to series
                df_ct = pd.merge(ct, struct, left_on="series", right_on="reference_ct")
                df_mr = pd.merge(mr, struct, left_on="series", right_on="reference_ct")
                df_combined = pd.concat([df_ct, df_mr])

            elif edge==3:  # FORMS RTSTRUCT->PET on ref_ct to series
                df_combined = pd.merge(pet, struct, left_on="series", right_on="reference_ct")

            elif edge==4:           # FORMS PET->CT on study
                df_combined = pd.merge(ct, pet, left_on="study", right_on="study")

            elif edge==5: 
                df_combined = pd.merge(plan, dose, left_on="instance_uid", right_on="reference_pl")

            else:
                df_combined = pd.merge(struct, plan, left_on="instance_uid", right_on="reference_rs")

            df_combined["edge_type"] = edge
            df_list.append(df_combined)

        df_edges = pd.concat(df_list, axis=0, ignore_index=True)
        return df_edges

    def _form_edge_study(self, df, all_study, study_id):
        '''
        For a given study id forms edge table
        '''
        
        df_study = df.loc[self.df["study"] == all_study[study_id]]
        df_list = []
        
        # Split into each modality
        plan = df_study.loc[df_study["modality"] == "RTPLAN"]
        dose = df_study.loc[df_study["modality"] == "RTDOSE"]
        struct = df_study.loc[df_study["modality"] == "RTSTRUCT"]
        ct = df_study.loc[df_study["modality"] == "CT"]
        mr = df_study.loc[df_study["modality"] == "MR"]
        pet = df_study.loc[df_study["modality"] == "PT"]

        edge_types = np.arange(7)
        for edge in edge_types:
            if edge==0:    # FORMS RTDOSE->RTSTRUCT, can be formed on both series and instance uid
                df_comb1    = pd.merge(struct, dose, left_on="instance_uid", right_on="reference_rs")
                df_comb2    = pd.merge(struct, dose, left_on="series", right_on="reference_rs")
                df_combined = pd.concat([df_comb1, df_comb2])
                #Cases where both series and instance_uid are the same for struct
                df_combined = df_combined.drop_duplicates(subset=["instance_uid_x"])

            elif edge==1:  # FORMS RTDOSE->CT 
                df_combined = pd.merge(ct, dose, left_on="series", right_on="reference_ct")

            elif edge==2:  # FORMS RTSTRUCT->CT on ref_ct to series
                df_ct = pd.merge(ct, struct, left_on="series", right_on="reference_ct")
                df_mr = pd.merge(mr, struct, left_on="series", right_on="reference_ct")
                df_combined = pd.concat([df_ct, df_mr])

            elif edge==3:  # FORMS RTSTRUCT->PET on ref_ct to series
                df_combined = pd.merge(pet, struct, left_on="series", right_on="reference_ct")

            elif edge==4:           # FORMS PET->CT on study
                df_combined = pd.merge(ct, pet, left_on="study", right_on="study")
            
            elif edge==5: 
                df_combined = pd.merge(plan, dose, left_on="instance", right_on="reference_pl")
            
            else:
                df_combined = pd.merge(struct, plan, left_on="instance", right_on="reference_rs")

            df_combined["edge_type"] = edge
            df_list.append(df_combined)
                
        df_edges = pd.concat(df_list, axis=0, ignore_index=True)
        self.df_master.append(df_edges)
    
    def parser(self, query_string: str) -> pd.DataFrame:
        '''
        For a given query string(Check the documentation), returns the dataframe consisting of two columns namely modality and folder location of the connected nodes
        Parameters
        ----------
        df
            Dataframe consisting of the crawled data
        df_edges
            Processed Dataframe forming a graph, stored in the form of edge table
        query_string
            Query string based on which dataset will be formed
        
        Query ideas:
        There are four basic supported modalities are RTDOSE, RTSTRUCT, CT, PT, MRI
        The options are, the string can be in any order:
        1) RTDOSE
        2) RTSTRUCT
        3) CT
        4) PT
        5) PT,RTSTRUCT
        6) CT,PT
        7) CT,RTSTRUCT
        8) CT,RTDOSE
        9) RTDOSE,RTSTRUCT,CT
        10) RTDOSE,CT,PT
        11) RTSTRUCT,CT,PT
        12) RTDOSE,RTSTRUCT,CT,PT
        '''
        #Basic processing of just one modality
        supp_mods   = ["RTDOSE", "RTSTRUCT", "CT", "PT", 'MR']
        edge_def    = {"RTSTRUCT,RTDOSE" : 0, "CT,RTDOSE" : 1, "CT,RTSTRUCT" : 2, "PET,RTSTRUCT" : 3, "CT,PT" : 4, 'MR,RTSTRUCT': 2}
        self.mods   = query_string.split(",")
        self.mods_n = len(self.mods)

        #Deals with single node queries
        if query_string in supp_mods:
            final_df = self.df.loc[self.df.modality == query_string, ["study", "patient_ID", "series", "folder"]]
            final_df.rename(columns = {"series": f"series_{query_string}", 
                                       "folder": f"folder_{query_string}"}, inplace=True)
        
        elif self.mods_n == 2:
            #Reverse the query string
            query_string_rev = (",").join(self.mods[::-1])
            if query_string in edge_def.keys():
                edge_type = edge_def[query_string]
                valid = query_string
            elif query_string_rev in edge_def.keys():
                edge_type = edge_def[query_string_rev]
                valid = query_string_rev
            else:
                raise ValueError("Invalid Query. Select valid pairs.")
            #For cases such as the CT-RTSTRUCT and CT-RTDOSE, there exists multiple pathways due to which just searching on the edgetype gives wrong results
            if edge_type in [0, 1, 2]:
                edge_list = [0, 1, 2]
                if edge_type==0:
                    #Search for subgraphs with edges 0 or (1 and 2)
                    regex_term = '((?=.*0)|((?=.*1)(?=.*2)))'
                    mod = [i for i in self.mods if i in ['CT', 'MR']][0] # making folder_mod CT/MR agnostic <-- still needs testing
                    final_df = self.graph_query(regex_term, edge_list, f"folder_{mod}")
                elif edge_type==1:
                    #Search for subgraphs with edges 1 or (0 and 2)
                    regex_term = '((?=.*1)|((?=.*0)(?=.*2)))'
                    final_df = self.graph_query(regex_term, edge_list, "RTSTRUCT")
                elif edge_type==2:
                    #Search for subgraphs with edges 2 or (1 and 0)
                    regex_term = '((?=.*2)|((?=.*0)(?=.*1)))'
                    final_df = self.graph_query(regex_term, edge_list, "RTDOSE") 
            else:
                final_df = self.df_edges.loc[self.df_edges.edge_type == edge_type, ["study_x","patient_ID_x","series_x","folder_x","series_y","folder_y"]]
                node_dest = valid.split(",")[0]
                node_origin = valid.split(",")[1]
                final_df.rename(columns={"study_x": "study", 
                                         "patient_ID_x": "patient_ID", 
                                         "series_x": f"series_{node_dest}", 
                                         "series_y": f"series_{node_origin}", 
                                         "folder_x": f"folder_{node_dest}", 
                                         "folder_y": f"folder_{node_origin}"}, inplace=True)

        elif self.mods_n > 2:
            #Processing of combinations of modality
            if (("CT" in query_string) or ('MR' in query_string)) & ("RTSTRUCT" in query_string) & ("RTDOSE" in query_string) & ("PT" not in query_string):
                #Fetch the required data. Checks whether each study has edge 2 and (1 or 0)
                regex_term = '(?=.*(1|0))(?=.*2)'
                edge_list = [0, 1, 2]
                final_df = self.graph_query(regex_term, edge_list) 

            elif (("CT" in query_string) or ('MR' in query_string))  & ("RTSTRUCT" in query_string) & ("RTDOSE" in query_string) & ("PT" in query_string):
                #Fetch the required data. Checks whether each study has edge 2,3,4 and (1 or 0)
                regex_term = '(?=.*(1|0))(?=.*2)(?=.*3)(?=.*4)'
                edge_list = [0, 1, 2, 3, 4]
                final_df = self.graph_query(regex_term, edge_list) 

            elif (("CT" in query_string) or ('MR' in query_string))  & ("RTSTRUCT" in query_string) & ("PT" in query_string) & ("RTDOSE" not in query_string):
                #Fetch the required data. Checks whether each study has edge 2,3,4
                regex_term = '(?=.*2)(?=.*3)(?=.*4)'
                edge_list = [2, 3, 4]
                final_df = self.graph_query(regex_term, edge_list) 
            
            elif (("CT" in query_string) or ('MR' in query_string))  & ("RTSTRUCT" not in query_string) & ("PT" in query_string) & ("RTDOSE" in query_string):
                #Fetch the required data. Checks whether each study has edge 4 and (1 or (2 and 0)). Remove RTSTRUCT later
                regex_term = '(?=.*4)((?=.*1)|((?=.*2)(?=.*0)))'
                edge_list = [0, 1, 2, 4]
                final_df = self.graph_query(regex_term, edge_list, "RTSTRUCT") 
            else:
                raise ValueError("Please enter the correct query")
        else:
            raise ValueError("Please enter the correct query")
        final_df.reset_index(drop=True, inplace=True)
        final_df["index_chng"] = final_df.index.astype(str) + "_" + final_df["patient_ID"].astype(str)
        final_df.set_index("index_chng", inplace=True)
        final_df.rename_axis(None, inplace=True)
        #change relative paths to absolute paths
        for col in final_df.columns:
            if col.startswith("folder"):
                # print(self.edge_path, os.path.dirname(self.edge_path))
                final_df[col] = final_df[col].apply(lambda x: pathlib.Path(os.path.split(os.path.dirname(self.edge_path))[0], x).as_posix() if isinstance(x, str) else x) #input folder joined with the rel path
        return final_df
    
    def graph_query(self, 
                    regex_term: str,
                    edge_list: List[int],
                    change_df: str = "",
                    return_components: bool = False,
                    remove_less_comp: bool = True):
        '''
        Based on the regex forms the final dataframe. You can 
        query the edge table based on the regex to get the 
        subgraph in which the queried edges will be present.
        
        The components are process further to get the final 
        dataframe of the required modalities.
        
        Parameters
        ----------
        regex_term
            To search the string in edge_type column of self.df_new which is aggregate of all the edges in a single study

        edge_list
            The list of edges that should be returned in the subgraph

        return_components
            True to return the dictionary of the componets present with the condition present in the regex

        change_df
            Use only when you want to remove columns containing that string

        remove_less_comp
            False when you want to keep components with modalities less than the modalitiy listed in the query
        '''
        if self.df_new is None:
            self._form_agg() #Form aggregates
        
        # Fetch the required data. Checks whether each study has edge 4 and (1 or (2 and 0)). Can remove later
        relevant_study_id = self.df_new.loc[(self.df_new.edge_type.str.contains(regex_term)), "study_x"].unique()
        
        # Based on the correct study ids, fetches the relevant edges
        df_processed = self.df_edges.loc[self.df_edges.study_x.isin(relevant_study_id) & (self.df_edges.edge_type.isin(edge_list))]
        
        # The components are deleted if it has less number of nodes than the passed modalities, change this so as to alter that condition
        final_df = self._get_df(df_processed, relevant_study_id, remove_less_comp)

        # Removing columns
        if len(change_df) > 0:
            # Find columns with change_df string present
            col_ids = [cols for cols in final_df.columns if change_df not in cols]
            final_df = final_df[col_ids]
        
        # if return_components:
        #     return self.final_dict
        # else:
        return final_df

    def _form_agg(self):
        '''
        Form aggregates for easier parsing, gets the edge types for each study and aggregates as a string. This way one can do regex based on what type of subgraph the user wants
        '''
        self.df_edges['edge_type_str'] = self.df_edges['edge_type'].astype(str)
        self.df_new = self.df_edges.groupby("study_x").agg({'edge_type_str':self.list_edges})
        self.df_new.reset_index(level=0, inplace=True) 
        self.df_new["edge_type"] = self.df_new["edge_type_str"]

    def _get_df(self,
                df_edges_processed,
                rel_studyids: List[str],
                remove_less_comp = True):
        '''
        Assumption
        ----------
        The components are determined based on the unique CTs. 
        Please ensure the data conforms to this case. Based on 
        our preliminary analysis, there are no cases where CT 
        and PT are present but are disconnected.

        Hence this assumption should hold for most of the cases
        This function returns dataframe consisting of folder 
        location and modality for subgraphs

        Parameters
        ----------
        df_edges_processed
            Dataframe processed containing only the desired edges from the full graph

        rel_studyids
            Relevant study ids to process(This operation is a bit costly 
            so better not to perform on full graph for maximum performance)

        remove_less_comp
            True for removing components with less number of edges than the query

        Changelog
        ---------
        * June 14th, 2022: Changing from studyID-based to sample-based for loop
        '''
        #Storing all the components across all the studies
        self.final_dict = []
        final_df = []
        #For checking later if all the required modalities are present in a component or not
        mods_wanted = set(self.mods)

        # per-sample
        for i in range(len(df_edges_processed)):
            row = df_edges_processed.iloc[i]
            series   = row.series_x
            modality = row.modality_x
            folder   = row.folder_x
            
            series_y = row.series_y
            modality_y = row.modality_y
            folder_y = row.folder_y

            temp = {"study": row.study_x,
                    series: {"modality": modality,
                             "folder": folder},
                    row.series_y: {"modality": modality_y,
                                   "folder": folder_y,
                                   "conn_to": modality}}

            folder_save = {'study': row.study_x,
                           'patient_ID': row.patient_ID_x,
                           f'series_{modality}': series,
                           f'folder_{modality}': folder,
                           f'series_{modality_y}': series_y,
                           f'series_{modality_y}': folder_y}



        #Determine the number of components
        for i in range(len(rel_studyids)): # per study_id
            df_temp = df_edges_processed.loc[df_edges_processed.study_x == rel_studyids[i]]
            CT_locs = df_temp.loc[df_temp.modality_x.isin(['CT', 'MR'])]
            comp = CT_locs.series_x.unique()
            A = []
            save_folder_comp = []
            #Initialization. For each component intilize a dictionary with the CTs and their connections
            for j in range(len(comp)):
                #For each component, this loop stores the CT and its connections
                temp = {}
                #For saving the components in a format easier for the main pipeline
                folder_save = {}
                temp["study"] = rel_studyids[i]
                temp[comp[j]] = {}
                
                df_connections = CT_locs.loc[CT_locs.series_x == comp[j]] 
                temp[comp[j]]["modality"] = df_connections["modality_x"].iloc[0] #CT/MR
                temp[comp[j]]["folder"] = df_connections["folder_x"].iloc[0]
                #Saving some items in folder_save dictionary
                folder_save["study"] = rel_studyids[i]
                folder_save["patient_ID"] = df_connections["patient_ID_x"].iloc[0]
                folder_save[f"series_{df_connections['modality_x'].iloc[0]}"] = comp[j]
                folder_save[f"folder_{df_connections['modality_x'].iloc[0]}"] = df_connections["folder_x"].iloc[0]
                temp_dfconn = df_connections[["series_y", "modality_y", "folder_y"]]

                for k in range(len(temp_dfconn)):
                    #This loop stores connection of the CT
                    temp[temp_dfconn.iloc[k,0]] = {"modality": temp_dfconn.iloc[k,1], "folder": temp_dfconn.iloc[k,2], "conn_to": temp[comp[j]]["modality"]}
                    #Checks if there is already existing connection
                    key, key_series = self._check_save(folder_save,temp_dfconn.iloc[k,1],temp[comp[j]]["modality"]) #CT/MR
                    folder_save[key_series] = temp_dfconn.iloc[k,0]
                    folder_save[key] = temp_dfconn.iloc[k,2]
                A.append(temp)
                save_folder_comp.append(folder_save)
            
            #For rest of the edges left out, the connections are formed by going through the dictionary. For cases such as RTstruct-RTDose and PET-RTstruct
            rest_locs = df_temp.loc[~df_temp.modality_x.isin(['CT', 'MR']), ["series_x", "modality_x","folder_x", "series_y", "modality_y", "folder_y"]]
            flag = 0
            for j in range(len(rest_locs)):
                for k in range(len(comp)):
                    if rest_locs.iloc[j,0] in A[k]:
                        A[k][rest_locs.iloc[j,3]] = {"modality": rest_locs.iloc[j,4], "folder": rest_locs.iloc[j,5], "conn_to": rest_locs.iloc[j,1]}
                        if rest_locs.iloc[j,4]=="RTDOSE":
                            #RTDOSE is connected via either RTstruct or/and CT, but we usually don't care, so naming it commonly
                            key, key_series = self._check_save(save_folder_comp[k],rest_locs.iloc[j,4], "CT")
                            save_folder_comp[k][key_series] = rest_locs.iloc[j,3]
                            save_folder_comp[k][key] = rest_locs.iloc[j,5]
                        else: #Cases such as RTSTRUCT-PT
                            #if there is already a connection and one more same category modality wants to connect
                            key, key_series = self._check_save(save_folder_comp[k],rest_locs.iloc[j,4],rest_locs.iloc[j,1])
                            save_folder_comp[k][key_series] = rest_locs.iloc[j,3]
                            save_folder_comp[k][key] = rest_locs.iloc[j,5]
                        flag = 0
                    else:
                        flag = 1
            if flag==1:
                raise ValueError(f"In studyID: {rel_studyids[i]}, one of the edges had no match to any of the components which start from CT/MR. Please check the data")

            remove_index = []
            if remove_less_comp:
                for j in range(len(comp)):
                    #Check if the number of nodes in a components isn't less than the query nodes, if yes then remove that component
                    mods_present = set([items.split("_")[1] for items in save_folder_comp[j].keys() if items.split("_")[0] == "folder"])
                    #Checking if all the reqd modalities are present in a component
                    if mods_wanted.issubset(mods_present) == True:
                        remove_index.append(j)
                save_folder_comp = [save_folder_comp[idx] for idx in remove_index]        
                A = [A[idx] for idx in remove_index]    

            self.final_dict.extend(A)
            final_df.extend(save_folder_comp)
        
        final_df = pd.DataFrame(final_df)
        return final_df
    
    @staticmethod
    def _check_save(save_dict,node,dest):
        key = f"folder_{node}_{dest}"
        key_series = f"series_{node}_{dest}"
        i = 1
        while key in save_dict.keys():
            key = f"folder_{node}_{dest}_{i}"
            key_series = f"series_{node}_{dest}_{i}"
            i +=1
        return key,key_series
    
    @staticmethod
    def list_edges(series):
        return reduce(lambda x, y:str(x) + str(y), series)

