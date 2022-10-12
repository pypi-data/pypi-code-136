import os
import json

from .Configuration import Configuration
from .Network import Network

from urllib3 import PoolManager
from urllib3 import Timeout
from urllib3 import Retry
from urllib.parse import urlencode

class Sbml4j(object):
    _configuration : Configuration
    _networkList : [Network]
    _shortUuidToNetworkMap : {}
    _nameToNetworkMap: {}
    _pm : PoolManager

    def __init__(self, configuration=None):
        self._pm = PoolManager(
        timeout=Timeout(connect=None, read=None),
        retries=Retry(1, redirect=0))
        if configuration == None:
            self._configuration = Configuration()
        else:
            self._configuration = configuration
        self.refreshNetworkList()
        self._configuration.isInSync = True


    @property
    def configuration(self):
        return self._configuration
    @configuration.setter
    def configuration(self, configuration):
        self._configuration = configuration

    @property
    def user(self):
        return self._configuration.user
    @user.setter
    def user(self, value):
        self._configuration.user = value

    @property
    def networkMap(self):
        return self._shortUuidToNetworkMap

    @property
    def nameToNetworkMap(self):
        return self._nameToNetworkMap

    def refreshNetworkList(self):
        self._networkList = self.generateNetworkList()
        self._shortUuidToNetworkMap = self.generateNetworkMap('uuid')
        self._nameToNetworkMap = self.generateNetworkMap('name')

    def checkSyncStatus(self):
        if not self._configuration.isInSync:
            #print("Configuration out of sync. Refreshing network list.")
            self.refreshNetworkList()
            self._configuration.isInSync = True
            
    ######################################## SBML methods #####################################################

    def uploadSBML(self, sbmlFiles, organism, datasource, datasourceVersion):
        self.checkSyncStatus()
        baseUrl = "{}/sbml?".format(self._configuration.url)
        # required arguments
        args_dict = {'organism': organism, 'source': datasource, 'version': datasourceVersion}

        # encode the arguments
        encoded_args = urlencode(args_dict)
        urlString = baseUrl + encoded_args

        if isinstance(sbmlFiles, list):
            files_dict = {}
            for file in sbmlFiles:
                with open(file) as sbml:
                    response = self._pm.request(
                        "POST",
                        urlString,
                        fields={
                            'files': (os.path.basename(sbml.name), sbml.read())
                        },
                        headers = self._configuration.headers
                    )
                    if response.status > 399:
                        if not 'reason' in response.headers.keys():
                            raise Exception("Unknown Error fetching resource: HttpStatus: {}; Header of response: {}".format(response.status, response.headers))
                        else:
                            raise Exception("Could not create resource. Reason: {}".format(response.headers['reason']))
                    else:
                        pathwayInventoryItemList = json.loads(response.data.decode('utf-8'))
                        files_dict[file]=pathwayInventoryItemList[0]
        return files_dict


    def getEntityInfo(self, geneSymbol):
        self.checkSyncStatus()
        baseUrl = "{}/entityInfo?".format(self._configuration.url)
        if isinstance(geneSymbol, list):
            geneSymbolParam = ",".join(geneSymbol)
        else:
            geneSymbolParam = geneSymbol
        args_dict = {'geneSymbol': geneSymbolParam}
        
        # encode the arguments
        encoded_args = urlencode(args_dict)
        urlString = baseUrl + encoded_args
        response = self._pm.request("GET", urlString,
                                   headers=self._configuration.headers)
        
        if response.status > 399:
            if not 'reason' in response.headers.keys():
                raise Exception("Unknown Error fetching resource: HttpStatus: {}; Header of response: {}".format(response.status, response.headers))
            else:
                raise Exception("Could not fetch resource. Reason: {}".format(response.headers['reason']))
        else:
            return json.loads(response.data.decode('utf-8'))
    
    
    def getIdMap(self, symbol, separator=",", idSystem=None):
        self.checkSyncStatus()
        baseUrl = "{}/idMap?".format(self._configuration.url)
        
        if isinstance(symbol, list):
            symbolParam = separator.join(symbol)
        else:
            symbolParam = symbol
        args_dict = {'symbol': symbolParam, 'separator': separator}
        
        if idSystem != None:
            args_dict['idSystem'] = idSystem
        
        
        # encode the arguments
        encoded_args = urlencode(args_dict)
        urlString = baseUrl + encoded_args
        response = self._pm.request("GET", urlString,
                                   headers=self._configuration.headers)
        
        if response.status > 399:
            if not 'reason' in response.headers.keys():
                raise Exception("Unknown Error fetching resource: HttpStatus: {}; Header of response: {}".format(response.status, response.headers))
            else:
                raise Exception("Could not fetch resource. Reason: {}".format(response.headers['reason']))
        else:
            return json.loads(response.data.decode('utf-8'))
        
    ######################################## GraphML methods #####################################################
    
    def uploadGraphML(self, graphMLFiles, parentUUID=None, networkname=None, doPrefixName=None, doSuffixName=None):
        self.checkSyncStatus()
        baseUrl = "{}/graphml?".format(self._configuration.url)
        # required arguments
        args_dict = {}
        # optional arguments
        if parentUUID != None:
            args_dict['parentUUID'] = parentUUID
        if networkname != None:
            args_dict['networkname'] = networkname
        if doPrefixName != None:
            args_dict['prefixName'] = doPrefixName
        if doSuffixName != None:
            args_dict['suffixName'] = doSuffixName
    
        urlString = baseUrl
        if len(args_dict) > 0:
            # encode the arguments
            encoded_args = urlencode(args_dict)
            urlString = urlString + encoded_args
    
        if not isinstance(graphMLFiles, list):
            graphMLFiles = [graphMLFiles]
            
        files_dict = {}
        for file in graphMLFiles:
            with open(file) as graphml:
                response = self._pm.request(
                    "POST",
                    urlString,
                    fields={
                        'files': (os.path.basename(graphml.name), graphml.read())
                    },
                    headers = self._configuration.headers
                )
                if response.status > 399:
                    if not 'reason' in response.headers.keys():
                        raise Exception("Unknown Error fetching resource: HttpStatus: {}; Header of response: {}".format(response.status, response.headers))
                    else:
                        raise Exception("Could not create resource. Reason: {}".format(response.headers['reason']))
                else:
                    networkInventoryItemList = json.loads(response.data.decode('utf-8'))
                    files_dict[file]=networkInventoryItemList[0]
        self._configuration.isInSync=False
        return json.loads(response.data.decode('utf-8'))

    ####################################### Provenance methods ###################################################

    def getProvenance(self, uuid, user):
        baseUrl = "{}/prov/{}".format(self._configuration.url, uuid)
        
        response = self._pm.request("GET", baseUrl,
                                    headers=self._configuration.headers)
        if response.status > 399:
            if not 'reason' in response.headers.keys():
                raise Exception("Unknown Error fetching resource: HttpStatus: {}; Header of response: {}".format(response.status, response.headers))
            else:
                raise Exception("Could not fetch resource. Reason: {}".format(response.headers['reason']))
        else:
            return json.loads(response.data.decode("utf-8"))
        
    def addProvenance(self, uuid, name, jsonBody):
        self.checkSyncStatus()
        
        # requestBody (needs to be json, and we simply use the dumps method to convert the provided data into json)
        if not isinstance(jsonBody , dict):
            raise Exception("jsonBody method parameter needs to be a dictionary type.")
        
        baseUrl = "{}/prov/{}?".format(
                    self._configuration.url,
                    uuid
                    )
        # required arguments
        args_dict = {'name': name}
        
        # encode the arguments
        encoded_args = urlencode(args_dict)
        urlString = baseUrl + encoded_args

        encoded_data = json.dumps(jsonBody).encode('utf-8')
        headers_dict = self._configuration.headers
        # our content does not get recognized as json, so we set the header explicitly
        headers_dict['Content-Type'] = 'application/json'
        
        # send the request
        response = self._pm.request(
            "PUT",
            urlString,
            body=encoded_data,
            headers=headers_dict
        )
                
        # reset the header as other requests cannot set it themselves otherwise
        del headers_dict['Content-Type']
        
        if response.status > 399:
            if not 'reason' in response.headers.keys():
                raise Exception("Unknown Error fetching resource: HttpStatus: {};\n Message: {}\n Header of response: {}".format(response.status, response.data, response.headers))
            else:
                raise Exception("Could not get resource. Reason: {}".format(response.headers['reason']))
        else:
           provenanceInfoItem = json.loads(response.data.decode('utf-8'))
           return provenanceInfoItem

    ######################################## Pathway methods #####################################################

    def pathwayList(self, hideCollections=None):
        baseUrl = "{}/pathways".format(self._configuration.url)
        if hideCollections != None and (hideCollections == True or hideCollections == False):
            urlString = baseUrl + "?hideCollections=" + hideCollections
        else:
            urlString = baseUrl

        response = self._pm.request("GET", urlString,
                                   headers=self._configuration.headers)

        if response.status > 399:
            if not 'reason' in response.headers.keys():
                raise Exception("Unknown Error fetching resource: HttpStatus: {}; Header of response: {}".format(response.status, response.headers))
            else:
                raise Exception("Could not fetch resource. Reason: {}".format(response.headers['reason']))
        else:
            return json.loads(response.data)


    def pathwayUUIDs(self, hideCollections=None):
        baseUrl = "{}/pathwayUUIDs".format(self._configuration.url)

        if hideCollections != None:
            if hideCollections == True:
                urlString = baseUrl + "?hideCollections=True"
            elif hideCollections == False:
                urlString = baseUrl + "?hideCollections=False"
            else:
                raise Exception("Parameter hideCollections needs to be either True or False, or omitted. You provided:{}".format(hideCollections))
        else:
            urlString = baseUrl

        response = self._pm.request("GET", urlString,
                                   headers=self._configuration.headers)

        if response.status > 399:
            if not 'reason' in response.headers.keys():
                raise Exception("Unknown Error fetching resource: HttpStatus: {}; Header of response: {}".format(response.status, response.headers))
            else:
                raise Exception("Could not fetch resource. Reason: {}".format(response.headers['reason']))
        else:
            return json.loads(response.data)

    def createPathwayCollection(self, collectionName, collectionDesc, pathways):
        baseUrl = "{}/pathwayCollection".format(self._configuration.url)
        if not isinstance(pathways, list):
            raise Exception("parameter pathways must be of type list (of pathwayUUID-Strings), found {}".format (type(pathways)))
        else:
            data = {'name': collectionName,
                    'description': collectionDesc,
                    'sourcePathwayUUIDs': pathways}
            encoded_data = json.dumps(data).encode('utf-8')

        headers_dict = self._configuration.headers
        # our content does not get recognized as json, so we set the header explicitly
        headers_dict['Content-Type'] = 'application/json'

        # send the request
        response = self._pm.request(
            "POST",
            baseUrl,
            body=encoded_data,
            headers=headers_dict
        )
        # reset the header as other requests cannot set it themselves otherwise
        del headers_dict['Content-Type']
        if response.status > 399:
            if not 'reason' in response.headers.keys():
                raise Exception("Unknown Error while creating pathwayCollection resource: HttpStatus: {};\n Message: {}\n Header of response: {}".format(response.status, response.data, response.headers))
            else:
                raise Exception("Could not create pathwayCollection. Reason: {}".format(response.headers['reason']))
        else:
            return response.data.decode('utf-8')

    def mapPathway(self, pathwayUUID, mappingType, networkname=None, doPrefixName=None, doSuffixName=None):
        baseUrl = "{}/mapping/{}?".format(self._configuration.url, pathwayUUID)

        # required arguments
        args_dict = {'mappingType': mappingType}
        # optional arguments
        if networkname != None:
            args_dict['networkname'] = networkname
        if doPrefixName != None:
            args_dict['prefixName'] = doPrefixName
        if doSuffixName != None:
            args_dict['suffixName'] = doSuffixName

        # encode the arguments
        encoded_args = urlencode(args_dict)
        urlString = baseUrl + encoded_args
        # send the request
        response = self._pm.request(
            "POST",
            urlString,
            headers=self._configuration.headers
        )
        if response.status > 399:
            if not 'reason' in response.headers.keys():
                raise Exception("Unknown Error mapping Pathway: HttpStatus: {};\n Message: {}\n Header of response: {}".format(response.status, response.data, response.headers))
            else:
                raise Exception("Could not map Pathway. Reason: {}".format(response.headers['reason']))
        else:
            self._configuration.isInSync=False
            return json.loads(response.data.decode('utf-8'))

    ######################################## Network methods #####################################################
    def addNetwork(self, value):
        if isinstance(value, Network):
            self._networkList.append(value)
            self._shortUuidToNetworkMap[value.uuid[:8]] = value
            self._nameToNetworkMap[value.name] = value
        elif isinstance(value, list):
            for elem in value:
                self.addNetwork(elem)
        elif isinstance(value, dict):
            newNetwork = Network(value, self)
            self.addNetwork(newNetwork)
        else:
            raise Exception("Cannot add {} to list of networks.\n Expected type Network or dict of a network or list of Network entities or list of dicts of networks, found {}".format(value, type(value)))

    def generateNetworkList(self):
        return [Network(netInvItem, self) for netInvItem in json.loads(self.retrieveNetworkList().data)]

    def generateNetworkMap(self, key):
        localMap = {}
        for netItem in self._networkList:
            if (key=="uuid"):
                localMap[netItem.uuid[:8]] = netItem
            elif (key=="name"):
                localMap[netItem.name] = netItem
        return localMap

    def retrieveNetworkList(self):
        response = self._pm.request("GET", "{}/networks".format(self._configuration.url),
            headers = self._configuration.headers)
        return response

    def listNetworks(self):
        self.checkSyncStatus()
        for name, net in self._nameToNetworkMap.items():
            print("{}: {}".format(name, net))

    def getNetworks(self):
        self.checkSyncStatus()
        return self._nameToNetworkMap

    def getNetwork(self, uuid):
        self.checkSyncStatus()
        networkInfoDict = self._shortUuidToNetworkMap[uuid[:8]].getInfoDict()
        return Network(networkInfoDict, self)

    def getNetworkByName(self, name):
        self.checkSyncStatus()
        networkInfoDict = self._nameToNetworkMap[name].getInfoDict()
        return Network(networkInfoDict, self)

    def copyNetwork(self, uuid, networkname=None, doPrefixName=None, doSuffixName=None):
        self.checkSyncStatus()
        baseUrl = "{}/networks?".format(self._configuration.url)

        # required arguments
        args_dict = {'parentUUID': uuid}
        # optional arguments
        if networkname != None:
            args_dict['networkname'] = networkname
        if doPrefixName != None:
            args_dict['prefixName'] = doPrefixName
        if doSuffixName != None:
            args_dict['suffixName'] = doSuffixName

        # encode the arguments
        encoded_args = urlencode(args_dict)
        urlString = baseUrl + encoded_args

        response = self._pm.request("POST",
                                    urlString,
                                    headers = self._configuration.headers)
        if response.status > 399:
            if not 'reason' in response.headers.keys():
                raise Exception("Unknown Error fetching resource: HttpStatus: {}; Header of response: {}".format(response.status, response.headers))
            else:
                raise Exception("Could not create resource. Reason: {}".format(response.headers['reason']))
        else:
            copiedNetworkDict = json.loads(response.data.decode("utf-8"))
            self.addNetwork(copiedNetworkDict)
            return copiedNetworkDict

    def addCsvDataToNetwork(self, uuid, csvFile, dataName, networkname=None, doPrefixName=None, match=None, doDerive=None):
        self.checkSyncStatus()
        # build the url
        baseUrl = "{}/networks/{}/csv?".format(
                    self._configuration.url,
                    uuid)
        # required arguments
        args_dict = {'type': dataName}
        # optional arguments
        if networkname != None:
            args_dict['networkname'] = networkname
        if doPrefixName != None:
            args_dict['prefixName'] = doPrefixName
        if match != None:
            args_dict['match'] = match
        if doDerive != None:
            args_dict['derive'] = doDerive

        # encode the arguments
        encoded_args = urlencode(args_dict)
        urlString = baseUrl + encoded_args
        with open(csvFile) as fp:
            file_data = fp.read()

        response = self._pm.request(
            "POST",
            urlString,
            fields={
                'data': (csvFile, file_data)
            },
            headers = self._configuration.headers
        )
        if response.status > 399:
            if not 'reason' in response.headers.keys():
                raise Exception("Unknown Error fetching resource: HttpStatus: {}; Header of response: {}".format(response.status, response.headers))
            else:
                raise Exception("Could not create resource. Reason: {}".format(response.headers['reason']))
        else:
            csvNetworkDict = json.loads(response.data.decode('utf-8'))
            self.addNetwork(csvNetworkDict)
            return csvNetworkDict


    def getContext(self,
                   uuid,
                   geneList,
                   terminateAt=None,
                   direction=None,
                   minSize=None,
                   maxSize=None,
                   directed=None,
                   weightPropertyName=None):
        self.checkSyncStatus()
        prior_accept = self._configuration.accept
        self._configuration.accept = "application/octet-stream"
        urlString = "{}/networks/{}/context".format(
                    self._configuration.uuid,
                    uuid)
        fields_dict = {}

        # geneList must be list object
        if not isinstance(geneList, list):
            raise Exception("parameter geneList must be of type list, found {}".format (type(geneList)))
        else:
            fields_dict['genes'] = ", ".join(geneList)
        if minSize != None:
            fields_dict['minSize'] = minSize
        if maxSize != None:
            fields_dict['maxSize'] = maxSize
        if terminateAt != None:
            fields_dict['terminateAt'] = terminateAt
        if direction != None:
            fields_dict['direction'] = direction
        if directed != None:
            fields_dict['directed'] = directed
        if weightPropertyName != None:
            fields_dict['weightproperty'] = weightPropertyName

        response = self._pm.request(
            "GET",
            urlString,
            fields=fields_dict,
            headers=self._configuration.headers
        )
        # reset the accept header to the state before this request
        self._configuration.accept = prior_accept
        if response.status > 399:
            if not 'reason' in response.headers.keys():
                raise Exception("Unknown Error fetching resource: HttpStatus: {}; Header of response: {}".format(response.status, response.headers))
            else:
                raise Exception("Could not get resource. Reason: {}".format(response.headers['reason']))
        else:
            return response.data

    def postContext(self,
                    uuid,
                    geneList,
                    terminateAt=None,
                    direction=None,
                    minSize=None,
                    maxSize=None,
                    networkname=None,
                    doPrefixName=None,
                    weightPropertyName=None):
        self.checkSyncStatus()
        baseUrl = "{}/networks/{}/context".format(
                    self._configuration.url,
                    uuid
                    )

        # no required arguments

        args_dict = {}
        # optional arguments
        if minSize != None:
            args_dict['minSize'] = minSize
        if maxSize != None:
            args_dict['maxSize'] = maxSize
        if terminateAt != None:
            args_dict['terminateAt'] = terminateAt
        if direction != None:
            args_dict['direction'] = direction
        if networkname != None:
            args_dict['networkname'] = networkname
        if doPrefixName != None:
            args_dict['prefixName'] = doPrefixName
        if weightPropertyName != None:
            args_dict['weightproperty'] = weightPropertyName

        if len(args_dict) > 0:
            baseUrl += "?"
        # encode the arguments
        encoded_args = urlencode(args_dict)
        urlString = baseUrl + encoded_args
        # request body
        # geneList must be list object
        if not isinstance(geneList, list):
            raise Exception("parameter geneList must be of type list, found {}".format (type(geneList)))
        else:
            data = {'genes': geneList}
            encoded_data = json.dumps(data).encode('utf-8')

        headers_dict = self._configuration.headers
        # our content does not get recognized as json, so we set the header explicitly
        headers_dict['Content-Type'] = 'application/json'

        # send the request
        response = self._pm.request(
            "POST",
            urlString,
            body=encoded_data,
            headers=headers_dict
        )
        # reset the header as other requests cannot set it themselves otherwise
        del headers_dict['Content-Type']
        if response.status > 399:
            if not 'reason' in response.headers.keys():
                raise Exception("Unknown Error fetching resource: HttpStatus: {};\n Message: {}\n Header of response: {}".format(response.status, response.data, response.headers))
            else:
                raise Exception("Could not get resource. Reason: {}".format(response.headers['reason']))
        else:
            contextNetworkDict = json.loads(response.data.decode('utf-8'))
            self.addNetwork(contextNetworkDict)
            return contextNetworkDict


    def getNetworkGraphML(self, network, directed=None):
        self.checkSyncStatus()
        baseUrl = "{}/networks/{}".format(
                    self._configuration.url,
                    network.uuid)
        if directed != None:
            urlString = baseUrl + "?directed={}".format(directed)
        else:
            urlString = baseUrl

        prior_accept = self._configuration.accept
        self._configuration.accept = "application/octet-stream"

        response = self._pm.request("GET", urlString,
                                    headers = self._configuration.headers)

        # reset the accept header to the state before this request
        #print("Previous accept is: {}".format(prior_accept))
        self._configuration.accept = prior_accept
        if response.status > 399:
            if response.headers['reason'] == None:
                raise Exception("Unknown Error fetching resource: HttpStatus: {}; Header of response: {}".format(response.status, response.headers))
            else:
                raise Exception("Could not get resource. Reason: {}".format(response.headers['reason']))
        else:
            return response.data


    def getNetworkOptions(self, uuid):
        self.checkSyncStatus()
        baseUrl = "{}/networks/{}/options".format(
                    self._configuration.url,
                    uuid)
        response = self._pm.request("GET", baseUrl,
                                   headers = self._configuration.headers)
        if response.status > 399:
            if response.headers['reason'] == None:
                raise Exception("Unknown Error fetching resource: HttpStatus: {}; Header of response: {}".format(response.status, response.headers))
            else:
                raise Exception("Could not get resource. Reason: {}".format(response.headers['reason']))
        else:
            return json.loads(response.data.decode("utf-8"))

    def filterNetwork(self, uuid, networkname=None, doPrefixName=None, nodeSymbols=None, nodeTypes=None, relationSymbols=None, relationTypes=None):
        self.checkSyncStatus()
        baseUrl = "{}/networks/{}/filter".format(
                    self._configuration.url,
                    uuid
                    )

        # no required arguments

        args_dict = {}
        # optional arguments
        if networkname != None:
            args_dict['networkname'] = networkname
        if doPrefixName != None:
            args_dict['prefixName'] = doPrefixName

        if len(args_dict) > 0:
            baseUrl += "?"
        # encode the arguments
        encoded_args = urlencode(args_dict)
        urlString = baseUrl + encoded_args
        # request body
        # filterOptions
        if nodeSymbols==None and nodeTypes==None and relationSymbols==None and relationTypes==None:
            raise Exception("At least one List (nodeSymbols, nodeTypes, relationSymbols, relationTypes, relationSymbols) has to be provided.")
        else:
            data = {}
            if nodeSymbols != None:
                data['nodeSymbols'] = nodeSymbols
            if nodeTypes != None:
                data['nodeTypes'] = nodeTypes
            if relationSymbols != None:
                data['relationSymbols'] = relationSymbols
            if relationTypes != None:
                data['relationTypes'] = relationTypes

            if data:
                encoded_data = json.dumps(data).encode('utf-8')
                headers_dict = self._configuration.headers
                # our content does not get recognized as json, so we set the header explicitly
                headers_dict['Content-Type'] = 'application/json'

                # send the request
                response = self._pm.request(
                    "POST",
                    urlString,
                    body=encoded_data,
                    headers=headers_dict
                )
                # reset the header as other requests cannot set it themselves otherwise
                del headers_dict['Content-Type']
                if response.status > 399:
                    if not 'reason' in response.headers.keys():
                        raise Exception("Unknown Error fetching resource: HttpStatus: {};\n Message: {}\n Header of response: {}".format(response.status, response.data, response.headers))
                    else:
                        raise Exception("Could not get resource. Reason: {}".format(response.headers['reason']))
                else:
                    filteredNetworkDict = json.loads(response.data.decode('utf-8'))
                    self.addNetwork(filteredNetworkDict)
                    return filteredNetworkDict


    def annotateNetwork(self, uuid, annotationObject, networkname=None, doPrefixName=None):
        self.checkSyncStatus()
        baseUrl = "{}/networks/{}/annotation".format(
                    self._configuration.url,
                    uuid
                    )

        # no required arguments

        args_dict = {}
        # optional arguments
        if networkname != None:
            args_dict['networkname'] = networkname
        if doPrefixName != None:
            args_dict['prefixName'] = doPrefixName

        if len(args_dict) > 0:
            baseUrl += "?"
        # encode the arguments
        encoded_args = urlencode(args_dict)
        urlString = baseUrl + encoded_args
        # request body
        # annotationOptions in annotationObject
        doAnnotateNodes = False
        doAnnotateRelations = False
        if annotationObject.get('nodeAnnotationName'):
            doAnnotateNodes = True
        if annotationObject.get('relationAnnotationName'):
            doAnnotateRelations = True

        data = {}
        if doAnnotateNodes and annotationObject.get('nodeAnnotationName') and annotationObject.get('nodeAnnotation'):
            data['nodeAnnotationName'] = annotationObject.get('nodeAnnotationName')
            data['nodeAnnotation'] = annotationObject.get('nodeAnnotation')
        if doAnnotateRelations and annotationObject.get('relationAnnotationName') and annotationObject.get('relationAnnotation'):
            data['relationAnnotationName'] = annotationObject.get('relationAnnotationName')
            data['relationAnnotation'] = annotationObject.get('relationAnnotation')

        if data:
            encoded_data = json.dumps(data).encode('utf-8')
            headers_dict = self._configuration.headers
            # our content does not get recognized as json, so we set the header explicitly
            headers_dict['Content-Type'] = 'application/json'

            # send the request
            response = self._pm.request(
                "POST",
                urlString,
                body=encoded_data,
                headers=headers_dict
            )
            # reset the header as other requests cannot set it themselves otherwise
            del headers_dict['Content-Type']
            if response.status > 399:
                if not 'reason' in response.headers.keys():
                    raise Exception("Unknown Error fetching resource: HttpStatus: {};\n Message: {}\n Header of response: {}".format(response.status, response.data, response.headers))
                else:
                    raise Exception("Could not get resource. Reason: {}".format(response.headers['reason']))
            else:
               annotatedNetworkDict = json.loads(response.data.decode('utf-8'))
               self.addNetwork(annotatedNetworkDict)
               return annotatedNetworkDict
        else:
            raise Exception("No annotation data found. Cannot annotate network.")


    # Add provenanceAnnotation to network
    def addProvenanceToNetwork(self, uuid, name, jsonBody):
        self.checkSyncStatus()
        
        # requestBody (needs to be json, and we simply use the dumps method to convert the provided data into json)
        if not isinstance(jsonBody , dict):
            raise Exception("jsonBody method parameter needs to be a dictionary type.")
        
        baseUrl = "{}/networks/{}/prov?".format(
                    self._configuration.url,
                    uuid
                    )
        # required arguments
        args_dict = {'name': name}
        
        # encode the arguments
        encoded_args = urlencode(args_dict)
        urlString = baseUrl + encoded_args

        encoded_data = json.dumps(jsonBody).encode('utf-8')
        headers_dict = self._configuration.headers
        # our content does not get recognized as json, so we set the header explicitly
        headers_dict['Content-Type'] = 'application/json'
        
        # send the request
        response = self._pm.request(
            "PUT",
            urlString,
            body=encoded_data,
            headers=headers_dict
        )
                
        # reset the header as other requests cannot set it themselves otherwise
        del headers_dict['Content-Type']
        
        if response.status > 399:
            if not 'reason' in response.headers.keys():
                raise Exception("Unknown Error fetching resource: HttpStatus: {};\n Message: {}\n Header of response: {}".format(response.status, response.data, response.headers))
            else:
                raise Exception("Could not get resource. Reason: {}".format(response.headers['reason']))
        else:
           provenanceInfoItem = json.loads(response.data.decode('utf-8'))
           return provenanceInfoItem
       
        
    # retrieve provenance report for network
    def getProvenanceForNetwork(self, uuid):
        self.checkSyncStatus()
        baseUrl = "{}/networks/{}/prov".format(
                    self._configuration.url,
                    uuid
                    )
        response = self._pm.request("GET", baseUrl,
                                   headers = self._configuration.headers)
        if response.status > 399:
            if response.headers['reason'] == None:
                raise Exception("Unknown Error fetching resource: HttpStatus: {}; Header of response: {}".format(response.status, response.headers))
            else:
                raise Exception("Could not get resource. Reason: {}".format(response.headers['reason']))
        else:
            return json.loads(response.data.decode("utf-8"))
        
        
    ######################################## Warehouse methods #####################################################
    
    def getFileorigin(self, uuid):
        self.checkSyncStatus()
        baseUrl = "{}/fileorigin/{}".format(
                    self._configuration.url,
                    uuid
                    )
        response = self._pm.request("GET", baseUrl,
                                   headers = self._configuration.headers)
        if response.status > 399:
            if response.headers['reason'] == None:
                raise Exception("Unknown Error fetching resource: HttpStatus: {}; Header of response: {}".format(response.status, response.headers))
            else:
                raise Exception("Could not get resource. Reason: {}".format(response.headers['reason']))
        else:
            return json.loads(response.data.decode("utf-8"))
        
    def getDatabaseUUID(self, orgCode, source, version):
        self.checkSyncStatus()
        baseUrl = "{}/databaseUUID?".format(
                    self._configuration.url)
    
        # required arguments
        args_dict = {'organism': orgCode, "source": source, "version": version}
        # encode the arguments
        encoded_args = urlencode(args_dict)
        urlString = baseUrl + encoded_args
        
        response = self._pm.request("GET", urlString,
                                   headers = self._configuration.headers)
        if response.status > 399:
            if response.headers['reason'] == None:
                raise Exception("Unknown Error fetching resource: HttpStatus: {}; Header of response: {}".format(response.status, response.headers))
            else:
                raise Exception("Could not get resource. Reason: {}".format(response.headers['reason']))
        else:
            return json.loads(response.data.decode("utf-8"))
        
