class Network(object):
    # this class is the main object the user is working with
    # it gets initialized after a call to sbml4j.getNetwork()
    # a network should hold all the metadata that is available in the networkInventoryItem
    # also it should hold a reference to a parent network (if applicable)
    # all endpoints in the networks category of sbml4j should be available on this class
    # everytime a new network is created due to a REST call (i.e. addCsvData) it should update the current object
    # and keep a reference to the parent network somehow.
    # How exactly this can be done I have to see.
    uuid: str
    name: str
    organismCode: str
    numberOfNodes: int
    numberOfRelations: int
    numberOfReactions: int
    nodeTypes: list
    relationTypes: list
    networkMappingType: str

    sbml4jApi = None
        
    def __init__(self, dict_from_api, api):
        # keep a reference to the api to route calls through
        self.sbml4jApi = api
        #print("Initializing Network instance")
        #print(dict_from_api)
        self.updateInfo(dict_from_api)

    def updateInfo(self, dict_with_info):
        #print("Updating network with info from :\n{}".format(dict_with_info))
        #for key, value in dict_with_info.items():
        self.uuid = dict_with_info['uuid']
        self.name = dict_with_info['name']
        self.organism_code = dict_with_info['organismCode']
        self.numberOfNodes = dict_with_info['numberOfNodes'] if 'numberOfNodes' in dict_with_info and dict_with_info['numberOfNodes'] != None else 0
        self.numberOfRelations = dict_with_info['numberOfRelations'] if 'numberOfRelations' in dict_with_info and dict_with_info['numberOfRelations'] != None else 0
        self.numberOfReactions = dict_with_info['numberOfReactions'] if 'numberOfReactions' in dict_with_info and dict_with_info['numberOfReactions'] != None else 0
        self.nodeTypes = dict_with_info['nodeTypes'] if 'nodeTypes' in dict_with_info and dict_with_info['nodeTypes'] != None else list()
        self.relationTypes = dict_with_info['relationTypes'] if 'relationTypes' in dict_with_info and dict_with_info['relationTypes'] != None else list()
        self.networkMappingType = dict_with_info['networkMappingType']
    
    def getInfoDict(self):
        dict_with_info = {
            'uuid' : self.uuid,
            'name' : self.name,
            'organismCode' : self.organism_code,
            'numberOfNodes' : self.numberOfNodes,
            'numberOfRelations' : self.numberOfRelations,
            'numberOfReactions' : self.numberOfReactions,
            'nodeTypes' : self.nodeTypes,
            'relationTypes' : self.relationTypes,
            'networkMappingType' : self.networkMappingType
        }
        return dict_with_info
    
    def __str__(self):
        return '{}-Network with {} nodes and {} relationships'.format(
            self.networkMappingType, self.numberOfNodes, self.numberOfRelations)
    
    
    ############
    # Retrieve the contents of the network in the GraphML format
    # decodes the output in utf-8 if not overwritten
    def graphML(self, directed=None, coding=None):
        # fire request
        try:
            resp = self.sbml4jApi.getNetworkGraphML(self, directed)
        except Exception as e:
            print(e)
            return None # Do we actually want to break here and terminate execution?
        else:
            if coding == None:
                return resp.decode('utf-8')
            else:
                return resp.decode(coding)
 
    ############
    # Create a copy of a network
    # The network will be identical to the given network
    # except getting a new name and a new uuid
    def copy(self, networkname=None, doPrefixName=False, doSuffixName=None):
        dict_with_new_info = self.sbml4jApi.copyNetwork(self.uuid, networkname, doPrefixName, doSuffixName)
        self.updateInfo(dict_with_new_info)
    
    ############
    # Add Data from a csv file to the network
    # The csv file needs have the gene symbol in the first column
    # all additional columns get added as annotations to the nodes
    # The given dataName will be added as Label to the gene-node and can be used in context searches
    # A name can be given to the resulting network, if ommited the old network name will prefixed with "Added_{dataName}_to_"
    def addCsvData(self, csvFile, dataName, networkname=None, doPrefixName=None, match=None, doDerive=None):
        dict_with_new_info = self.sbml4jApi.addCsvDataToNetwork(self.uuid, csvFile, dataName, networkname, doPrefixName, match, doDerive)
        self.updateInfo(dict_with_new_info)
        
    ############
    # Context
    # POST's a context for a network
    #     Searches the context, persists it as a new network
    #     and updates this Network instance to reflect the new network
    def createContext(self, 
                      geneList, 
                      terminateAt=None, 
                      direction=None, 
                      minSize=None, 
                      maxSize=None, 
                      networkname=None,
                      doPrefixName=None,
                      weightPropertyName=None):
        dict_with_new_info = self.sbml4jApi.postContext(self.uuid, geneList, terminateAt, direction, minSize, maxSize, networkname, doPrefixName, weightPropertyName)
        self.updateInfo(dict_with_new_info)
   
    ############
    # Context
    # There are two ways to generate a context
    # GET's a context from a network
    #     Searches the context and returns it as GraphML, leaving the network unchanged      
    def getContext(self, geneList, terminateAt=None, direction=None, minSize=None, maxSize=None, directed=None, coding=None, weightPropertyName=None):
        try:
            resp = self.sbml4jApi.getContext(self.uuid, geneList, terminateAt, direction, minSize, maxSize, directed, weightPropertyName)
        except Exception as e:
            print(e)
            return None # Do we actually want to break here and terminate execution?
        else:
            if coding == None:
                return resp.decode('utf-8')
            else:
                return resp.decode(coding)
    
    ############
    # Calcualte a shortest path between two given genes
    # This also uses the multi-gene context endpoint
    # which does calculate the shortest path for the two genes
    # and a neighborhood around the genes, whose size can be given.
    # With a size of zero, it results in only the shortest path between the two genes
    def shortestPath(self, gene1, gene2, directed=None, weightPropertyName=None, coding=None):
        try:
            resp = self.sbml4jApi.getContext(uuid=self.uuid, geneList=[gene1, gene2], minSize=0, maxSize=0, directed=directed, weightPropertyName=weightPropertyName)
        except Exception as e:
            print(e)
            return None # Do we actually want to break here and terminate execution?
        else:
            if coding == None:
                return resp.decode('utf-8')
            else:
                return resp.decode(coding)
    ###########
    # Get available options for filtering and annotating the network
    # This returns a dictionary containing two objects:
    #   1. The filter object dictionary
    #     It contains four elements declaring filtering of a network
    #     1.1. Node Filtering
    #     1.1.A nodeSymbols - A List containing all node symbols found in the network
    #     1.1.B nodeTypes - A List containing all node types found in the network 
    #     1.2.A relationSymbols - A List containing all relation symbols found in the network
    #     1.2.B relationTypes - A List containing all relation types found in the network
    #   2. The annotation object dictionary
    #     It contains four elements for declaring annotations to be added to the network
    #     2.1.A nodeAnnotationName - String item denoting the name of the annotation to be put on the nodes of the network
    #                                If this is not filled (kept at None), no node annotation will be added, if this annotation object is sent back to the service
    #     2.1.B nodeAnnotation - A dictionary where the keys are the node symbols of all nodes in the network and the values are of None-Type.
    #                            When nodeAnnotationName is provided, the values for present keys are annotated under the given name
    #     2.2.A relationAnnotationName - String item denoting the name of the annotation to be put on the relations of the network
    #                                If this is not filled (kept at None), no relation annotation will be added, if this annotation object is sent back to the service
    #     2.2.B relationAnnotation - A dictionary where the keys are the relation symbols of all relations in the network and the values are of None-Type.
    #                            When relationAnnotationName is provided, the values for present keys are annotated under the given name
    def getOptions(self):
        resp = self.sbml4jApi.getNetworkOptions(self.uuid)
        return resp

    ###########
    # Filter this network according to the contents of the provided filterDict dictionary
    # The filterDict dictionary can be obtained from the getOptions method (the filter object dictionary)
    def filter(self, filterDict, networkname=None, doPrefixName=None):
        if not filterDict:
            raise Exception("No data in filterDict. Provide at least one element in filterDict: nodeSymbols, nodeTypes, relationSymbols, relationTypes)")
        else:
            filterNodeSymbols = None
            filterNodeTypes = None
            filterRelationSymbols = None
            filterRelationTypes = None
            for (key, value) in filterDict.items():
                #print("Checking {} with value {}".format(key, value))
                if "nodeSymbols" == key:
                    filterNodeSymbols = value
                if "nodeTypes" == key:
                    filterNodeTypes = value
                if "relationSymbols" == key:
                    filterRelationSymbols = value
                if "relationTypes" == key:
                    filterRelationTypes = value
    
            dict_with_new_info = self.sbml4jApi.filterNetwork(self.uuid, nodeSymbols=filterNodeSymbols, nodeTypes=filterNodeTypes, relationSymbols=filterRelationSymbols, relationTypes=filterRelationTypes, networkname=networkname, doPrefixName=doPrefixName)
            self.updateInfo(dict_with_new_info)

    ############
    # Filter this network by any combination of input parameters nodeSymbols, nodeTypes, relationSymbols, relationTypes
    # Any of these elements that is omitted will be filled in from the getOptions method
    # This means that it allows all elements in the respective lists and does not filter out any of them except if the given filter criteria also rule them out
    def filterBy(self, nodeSymbols=None, nodeTypes=None, relationSymbols=None, relationTypes=None, networkname=None, doPrefixName=None):
        fullFilterOptions = self.getOptions().get('filter')
        filterOptions = {}       
        filterOptions['nodeSymbols'] = fullFilterOptions.get('nodeSymbols') if nodeSymbols == None else nodeSymbols
        filterOptions['nodeTypes'] = fullFilterOptions.get('nodeTypes') if nodeTypes == None else nodeTypes
        filterOptions['relationSymbols'] = fullFilterOptions.get('relationSymbols') if relationSymbols == None else relationSymbols
        filterOptions['relationTypes'] = fullFilterOptions.get('relationTypes') if relationTypes == None else relationTypes
        self.filter(filterOptions, networkname, doPrefixName)

    ############
    # Annotate this network using the elements in the annotationDict dictionary object
    # The annotationDict dictionary can be obtained from the getOptions method (the annotation object dictionary)
    def annotate(self, annotationDict, networkname=None, doPrefixName=None):
        if not annotationDict:
            raise Exception("No data in annotationDict. Provide either annotation information for nodes (nodeAnnotationName, nodeAnnotation), relations (relationAnnotationName, relationAnnotation) or both")
        else:
            dict_with_new_info = self.sbml4jApi.annotateNetwork(self.uuid, annotationDict, networkname, doPrefixName)
            self.updateInfo(dict_with_new_info)

    ############
    # Add free form provenance information to the network
    # Must provide a name for the provenance item
    # Must provide a dictionary of data as jsonBody
    def addProvenance(self, name, jsonBody):
        try:
            resp = self.sbml4jApi.addProvenanceToNetwork(self.uuid, name, jsonBody)
        except Exception as e:
            print(e)
            return False
        else:
            return resp
        
    ############
    # Retrieve the provenanceReport for the network
    def getProvenance(self):
        try:
            resp = self.sbml4jApi.getProvenanceForNetwork(self.uuid)
        except Exception as e:
            print(e)
            return False
        else:
            return resp