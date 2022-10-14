from iWAN import iWAN #pip install iWAN
import json
from pubkey2address import Gpk2BtcAddr,Gpk2DotAddr,Gpk2XrpAddr #pip install pubkey2address
from iWAN_Request import iWAN_Request
from monitor_utility.multicallUtility import EMultilCall, eCall,to_baseUnit
from monitor_utility.RpcProviderUtility import PROVIDER_SELECTOR
from web3 import Web3
class TokenPairsUtility:
    '''
    LockedAccounts;
    TokenPairs related infomations
    '''
    def __init__(self,net,iWAN_Config,chainInfo:dict,crossPoolTokenInfo:dict,evmChainCrossSc:dict,print_flag=False):
        '''
        :param net: 'main'/'test'
        :param chainInfo : 'https://raw.githubusercontent.com/Nevquit/configW/main/chainInfos.json'
                crossPoolTokenInfo: "https://raw.githubusercontent.com/Nevquit/configW/main/crossPoolTokenInfo.json"
                evmChainCrossSc :"https://raw.githubusercontent.com/Nevquit/configW/main/evmChainCrossSc.json"

        :param iWAN_Config: path: ".iWAN_config.json"
                {
                    "secretkey": "your secretkey",
                    "Apikey": "your apikey",
                    "url_test": "wss://apitest.wanchain.org:8443/ws/v3/",
                    "url_main": "wss://api.wanchain.org:8443/ws/v3/"
                }

        '''
        with open(iWAN_Config,'r') as f:
            config = json.load(f)
        self.net = net
        self.iwan = iWAN.iWAN(config["url_{}".format(net)],config['secretkey'],config['Apikey'])
        self.print_flag = print_flag
        self.chainInfo = chainInfo[net]
        self.poolTokenInfo = crossPoolTokenInfo[net]
        self.evmLockedAccounts = evmChainCrossSc[net]
    def pprint(self,*args,**kwargs):
        if self.print_flag :
            print(*args,**kwargs)
    def getTokenPairs(self):
        '''
        :return:
            {
                "jsonrpc": "2.0",
                "id": 1,
                "result": [
                    {
                        "id": "1",
                        "fromChainID": "2147483708",
                        "fromAccount": "0x0000000000000000000000000000000000000000",
                        "toChainID": "2153201998",
                        "toAccount": "0xe3ae74d1518a76715ab4c7bedf1af73893cd435a",
                        "ancestorSymbol": "ETH",
                        "ancestorDecimals": "18",
                        "ancestorAccount": "0x0000000000000000000000000000000000000000",
                        "ancestorName": "ethereum",
                        "ancestorChainID": "2147483708",
                        "name": "wanETH@wanchain",
                        "symbol": "wanETH",
                        "decimals": "18"
                    }
                ]
            }
        '''
        tokenPairs = self.iwan.sendRequest(iWAN_Request.getAllTokenPairs())
        return tokenPairs
    def get_xrp_token_pairs(self):
        '''
        return:
        [                    {
                        "id": "1",
                        "fromChainID": "2147483708",
                        "fromAccount": "0x0000000000000000000000000000000000000000",
                        "toChainID": "2153201998",
                        "toAccount": "0xe3ae74d1518a76715ab4c7bedf1af73893cd435a",
                        "ancestorSymbol": "ETH",
                        "ancestorDecimals": "18",
                        "ancestorAccount": "0x0000000000000000000000000000000000000000",
                        "ancestorName": "ethereum",
                        "ancestorChainID": "2147483708",
                        "name": "wanETH@wanchain",
                        "symbol": "wanETH",
                        "decimals": "18"
                    }
                    ]
        '''
        xrp_token_tokenPairs = []
        tokenPairs_all = self.getTokenPairs()['result']
        for token_pair in tokenPairs_all:
            if token_pair['fromChainID'] == "2147483792" and \
                    token_pair['fromAccount'] != "0x0000000000000000000000000000000000000000":
                xrp_token_tokenPairs.append(token_pair)
        return xrp_token_tokenPairs


    def getChainInfo(self):
        '''
        :param:
        :return:
        '''
        return self.chainInfo
    def getPoolTokenInfo(self):
        return self.poolTokenInfo
    def getEVMLockedAccounts(self):
        return self.evmLockedAccounts
    def getNoEVMLockedAccounts(self,grInfo):
        '''
        Need update this function when add new noEvm chains
        :param grInfo:
        :return:
        '''
        BTCAddr = Gpk2BtcAddr.GPK2BTCADDRESS(grInfo,net=self.net)
        btcAddress = BTCAddr.Public_key_to_address('BTC')
        ltcAddress = BTCAddr.Public_key_to_address('LTC')
        dogeAddress = BTCAddr.Public_key_to_address('DOGE')
        xrpAddress = Gpk2XrpAddr.GPK2XRPADDRESS().getSmXrpAddr(grInfo)
        dotAddress = Gpk2DotAddr.GPK2DOTADDRESS().getSmDotAddr(grInfo,self.net)
        noEVMLockedAccout = {'LTC':ltcAddress,'XRP':xrpAddress,'BTC':btcAddress,'DOGE':dogeAddress,'DOT':dotAddress}
        return noEVMLockedAccout
    def getLockedAccount(self,grInfo):
        LockedAccounts = {}
        evmLockedAccounts = self.getEVMLockedAccounts()
        noEVMLockedAccout = self.getNoEVMLockedAccounts(grInfo)
        LockedAccounts.update(evmLockedAccounts)
        LockedAccounts.update(noEVMLockedAccout)
        return LockedAccounts
    def getLockedAccountForMultiGrps(self,working_groups:list):
        '''
        :param working_groups: [group1ID,group2ID]
        :return:
        '''
        LockedAccs_allGroups = {}
        for wk_grp in working_groups:
            grInfo = self.iwan.sendRequest(iWAN_Request.getStoremanGrpInfo(wk_grp))
            self.pprint(grInfo)
            LockedAccs = self.getLockedAccount(grInfo)
            for chain, locked_account in LockedAccs.items():
                if not LockedAccs_allGroups.get(chain):
                    LockedAccs_allGroups[chain] = [locked_account]
                else:
                    if locked_account not in LockedAccs_allGroups[chain]:
                        LockedAccs_allGroups[chain].append(locked_account)
        return LockedAccs_allGroups
    def getChainDict(self):
        '''
        :return: chainIdDict,chainAbbr,noEVMChains
        '''
        chainIdDict={}
        chainAbbr = {}
        noEVMChains = []
        chainInfo = self.getChainInfo()
        for chainID in chainInfo.keys():
            chainName = chainInfo[chainID]["chainName"]
            chainIdDict[chainID] = chainName

            chainType = chainInfo[chainID]["chainType"]
            chainAbbr[chainName] = chainType

            evm = chainInfo[chainID]["evm"]
            if not evm:
                noEVMChains.append(chainType)
        return chainIdDict, chainAbbr, noEVMChains
    def getPoolTokenDict(self):
        poolTokenDict = {}
        poolTokenInfo = self.getPoolTokenInfo()
        poolTokenIDList = [int(i) for i in list(poolTokenInfo.keys())]
        for tokenPairID in poolTokenIDList:
            Asset = poolTokenInfo[str(tokenPairID)]['Asset']
            chainType = poolTokenInfo[str(tokenPairID)]['chainType']
            if not poolTokenDict.get(Asset):
                poolTokenDict[Asset] = {chainType:{}}
            if not  poolTokenDict[Asset].get(chainType):
                poolTokenDict[Asset][chainType] = {}
            poolTokenDict[Asset][chainType]['TokenAddress'] = poolTokenInfo[str(tokenPairID)]['TokenAddress']
            poolTokenDict[Asset][chainType]['PoolScAddress'] = poolTokenInfo[str(tokenPairID)]['PoolScAddress']
            poolTokenDict[Asset][chainType]['originalAmount'] = poolTokenInfo[str(tokenPairID)]['originalAmount']
        return poolTokenDict, poolTokenIDList
    def getassetCCDit(self):
        '''
        :return: assetCCDit:
                {
                    "ETH": {
                        "OriginalChains": {
                            "Ethereum": {
                                "TokenAddr": "0x0000000000000000000000000000000000000000",
                                "ancestorDecimals": "18",
                                "assetType": "coin_evm"
                            }
                        },
                        "MapChain": {
                            "Wanchain": {
                                "TokenAddr": "0xe3ae74d1518a76715ab4c7bedf1af73893cd435a",
                                "decimals": "18",
                                "assetType": "token_evm"
                            },
                            "Avalanche": {
                                "TokenAddr": "0x265fc66e84939f36d90ee38734afe4a770d2c114",
                                "decimals": "18",
                                "assetType": "token_evm"
                            },
                            "Moonriver": {
                                "TokenAddr": "0x576fde3f61b7c97e381c94e7a03dbc2e08af1111",
                                "decimals": "18",
                                "assetType": "token_evm"
                            },
                            "XinFin": {
                                "TokenAddr": "0x1289f70b8a16797cccbfcca8a845f36324ac9f8b",
                                "decimals": "18",
                                "assetType": "token_evm"
                            },
                            "OKT": {
                                "TokenAddr": "0x4d14963528a62c6e90644bfc8a419cc41dc15588",
                                "decimals": "18",
                                "assetType": "token_evm"
                            }
                        }
                    }
        supportChains = ["Wanchain","Ethereum","BSC"]
        '''
        assetCCDit = {}
        supportMapChains = []
        tokenPairs = self.getTokenPairs()
        chainIdDict, chainAbbr, noEVMChains = self.getChainDict()
        # print(noEVMChains)
        poolTokenDict, poolTokenIDList = self.getPoolTokenDict()
        for tokenPair in tokenPairs['result']:
            '''
            tokenPair ={
                        "id": "1",
                        "fromChainID": "2147483708",
                        "fromAccount": "0x0000000000000000000000000000000000000000",
                        "toChainID": "2153201998",
                        "toAccount": "0xe3ae74d1518a76715ab4c7bedf1af73893cd435a",
                        "ancestorSymbol": "ETH",
                        "ancestorDecimals": "18",
                        "ancestorAccount": "0x0000000000000000000000000000000000000000",
                        "ancestorName": "ethereum",
                        "ancestorChainID": "2147483708",
                        "name": "wanETH@wanchain",
                        "symbol": "wanETH",
                        "decimals": "18" #to chain decimal
                    }
            '''
            '''
                    {
                        "id": "3",
                        "fromChainID": "2147483708",
                        "fromAccount": "0x514910771af9ca656af840dff83e8264ecf986ca",
                        "toChainID": "2153201998",
                        "toAccount": "0x06da85475f9d2ae79af300de474968cd5a4fde61",
                        "ancestorSymbol": "LINK",
                        "ancestorDecimals": "18",
                        "ancestorAccount": "0x514910771af9ca656af840dff83e8264ecf986ca",
                        "ancestorName": "ChainLink Token",
                        "ancestorChainID": "2147483708",
                        "name": "wanLINK@wanchain",
                        "symbol": "wanLINK",
                        "decimals": "18"
                    }
            '''
            if chainIdDict.get(tokenPair['fromChainID']):# to ensure the new chain has been added to chainInfo(github:https://github.com/Nevquit/configW/blob/main/chainInfos.json)
                # init the asset dict
                asset = tokenPair['ancestorSymbol']
                if not assetCCDit.get(asset):
                    assetCCDit[asset]={'OriginalChains':{},'MapChain':{}}

                # fill the OriginalChain part
                if tokenPair['ancestorChainID'] == tokenPair['fromChainID']:
                    OriginalChain = chainIdDict[tokenPair['ancestorChainID']]
                    if chainAbbr[OriginalChain] in noEVMChains:
                        if tokenPair['fromAccount'] == '0x0000000000000000000000000000000000000000':
                            assetType = 'coin_{}'.format(chainAbbr[OriginalChain])
                        else:
                            assetType = 'token_{}'.format(chainAbbr[OriginalChain])
                    elif tokenPair['fromAccount'] == '0x0000000000000000000000000000000000000000':
                        assetType = 'coin_evm'
                    else:
                        assetType = 'token_evm'
                    assetCCDit[asset]['OriginalChains'][OriginalChain]={'TokenAddr':tokenPair['fromAccount'],'ancestorDecimals': tokenPair['ancestorDecimals'],'assetType':assetType,'chainType':chainAbbr[OriginalChain],'ccType':'normal'}

                # fill the MapChain part
                MapChain = chainIdDict[tokenPair['toChainID']]
                if chainAbbr[MapChain] in noEVMChains:
                    if tokenPair['toAccount'] == '0x0000000000000000000000000000000000000000':
                        assetType = 'coin_{}'.format(chainAbbr[MapChain])
                    else:
                        assetType = 'token_{}'.format(chainAbbr[MapChain])
                elif tokenPair['toAccount'] == '0x0000000000000000000000000000000000000000':
                    assetType = 'coin_evm'
                else:
                    assetType = 'token_evm'
                ## tag special cross type, need add asset to original chains if the asset is pool token
                if int(tokenPair['id']) in poolTokenIDList:
                    assetCCDit[asset]['OriginalChains'][MapChain] = {'TokenAddr': tokenPair['toAccount'],'ancestorDecimals': tokenPair.get('decimals',tokenPair['ancestorDecimals']), 'assetType': assetType, 'chainType': chainAbbr[MapChain],'ccType':'pool'}
                assetCCDit[asset]['MapChain'][MapChain] = {'TokenAddr':tokenPair['toAccount'],'decimals':tokenPair.get('decimals',tokenPair['ancestorDecimals']),'assetType':assetType,'chainType':chainAbbr[MapChain]}

                # summary mapped chains
                supportMapChains.append(MapChain)


        #delete the original chain from mappchain dic
        for asset,assetDetail in assetCCDit.items():
            oriChains = list(assetDetail['OriginalChains'].keys())
            for chain in oriChains:
                assetDetail['MapChain'].pop(chain,'')

        return assetCCDit,list(set(supportMapChains))
    def batchGetEvmMintedTokenTotalSupply(self,providers: dict, callsDic: dict, assetCCDit: dict, chainAbbr: dict,chainAbbr_reverse: dict):
        '''
        :param net: main/test
        :param  providers: {"ETH":"http://eth.rpc","WAN":"https://wan.rpc"}
                callsDic: 'https://github.com/Nevquit/configW/blob/main/muticallcallsBatch_{}.json'.format(net)
                assetCCDit:'https://github.com/Nevquit/configW/blob/main/crossAssetsDict_{}.json'.format(net)
                chainAbbr:'https://github.com/Nevquit/configW/blob/main/chainType.json'
                chainAbbr_reverse :'https://github.com/Nevquit/configW/blob/main/chainType_Reverse.json'
        :return: result: unit ETH  # {"TotallSupply":"Ethereum":{'USDT': 185891455, 'USDC': 62836966799090123418}}}
        '''
        result_raw = {
            "TotallSupply": {}}
        result = {"TotallSupply": {}}

        # Put the calls based chain, {'WAN':[calls],'ETH':[calls]}
        for ast, infos in assetCCDit.items():
            for chainname, tokenInfo in infos['MapChain'].items():
                if tokenInfo['assetType'] == 'token_evm':
                    callsDic[chainAbbr[chainname]].append(eCall(tokenInfo['TokenAddr'], 'totalSupply()(uint256)', [['{}'.format(ast), to_baseUnit]]))
        # get the totall supply via chain
        for chainType, calls in callsDic.items():
            multiTotallSupply = EMultilCall(calls, _w3=Web3(Web3.HTTPProvider(providers[chainType])))()
            result_raw["TotallSupply"][chainType] = multiTotallSupply
        # summarize the token total supply for the different chains
        for chainType, asstsDic in result_raw['TotallSupply'].items():
            for asset, value in asstsDic.items():
                decimals = int(assetCCDit[asset]['MapChain'][chainAbbr_reverse[chainType]]['decimals'])
                if not result['TotallSupply'].get(asset, None):
                    result['TotallSupply'][asset] = int(value) / (1 * 10 ** decimals)
                else:
                    result['TotallSupply'][asset] += int(value) / (1 * 10 ** decimals)
        return result
    def batchGetEvmTokenBalance(self,providers,tokenInfo: dict, evmLockedAccount: list, chainType):
        '''
        :param tokenInfo:
            {
                "USDT": {
                    "TokenAddr": "0000",
                    "ancestorDecimals": "6"
                },
                "USDC": {
                    "TokenAddr": "0000",
                    "ancestorDecimals": "6"
                }
            }
        :param evmLockedAccounts:['0x01','0x02']
        :param chainType:
        :param providers: {"ETH":"http://eth.rpc","WAN":"https://wan.rpc"}
        :return:
                {
                    "ETH": {
                        "USDT": 100,   #unit: ETH
                        "USDC": 300
                    }
                }
        '''
        result = {chainType: {}}
        calls = []
        for asset, tokenScInfo in tokenInfo.items():
            calls.append(eCall(tokenScInfo['TokenAddr'], ['balanceOf(address)(uint256)', evmLockedAccount],[['{}'.format(asset), to_baseUnit]]))
        multiCallResult = EMultilCall(calls, _w3=Web3(Web3.HTTPProvider(providers[chainType])))()
        for asset, tokenScInfo in tokenInfo.items():
            try:
                if not result[chainType].get(asset, None):
                    result[chainType][asset] = {}
                result[chainType][asset] = int(multiCallResult[asset]) / (1 * 10 ** int(tokenScInfo['ancestorDecimals']))
            except:
                result[chainType][asset] = None
        return result
    def batchGetEvmLockedTokenBalance(self,providers,assetCCDit: dict):
        '''
        :param providers: {"ETH":"http://eth.rpc","WAN":"https://wan.rpc"}
        :param accs: evmLocked accounts
        :param chainType:
        :return:
        '''
        #init
        tokenChain_dics = {}
        result = {'evmLockedAmount':{}}
        '''
        {
                "ETH": {
                    "USDT": {
                        "TokenAddr": "0000",
                        "ancestorDecimals": "6"
                    },
                    "USDC": {
                        "TokenAddr": "0000",
                        "ancestorDecimals": "6"
                    }
                },
                "WAN": {
                    "USDT": {
                        "TokenAddr": "0000",
                        "ancestorDecimals": "6"
                    },
                    "USDC": {
                        "TokenAddr": "0000",
                        "ancestorDecimals": "6"
                    }
                }
        }
        '''
        #classify evm token info based chain
        for asset, infos in assetCCDit.items():
            for chain, tokenInfo in infos['OriginalChains']:
                if tokenInfo['TokenAddr'] != '0x0000000000000000000000000000000000000000' and tokenInfo['assetType'] == "token_evm":
                    if not tokenChain_dics.get(tokenInfo['chainType']):
                        tokenChain_dics[tokenInfo['chainType']] = {}
                    tokenChain_dics[tokenInfo['chainType']].update({asset: {'TokenAddr': tokenInfo['TokenAddr'], 'ancestorDecimals': tokenInfo['ancestorDecimals']}})

        #batch get token balance based chain
        for chainType, tokensInfo in tokenChain_dics.items():
            TokenBalance = self.batchGetEvmTokenBalance(providers,tokensInfo, self.evmLockedAccounts[chainType],chainType)
            for asset, lockedAmount in TokenBalance[chainType].items():
                if not result['evmLockedAmount'].get(asset):
                    result['evmLockedAmount'][asset] = 0
                if lockedAmount != None:
                    result['evmLockedAmount'][asset] += lockedAmount
                else:
                    result['evmLockedAmount'][asset] = None
        return result

if __name__ == '__main__':
    iWAN_Config = 'E:\Automation\github\cross_asset_monitor\.iWAN_config.json'
    net = 'test'
    chainInfo = json.loads('''{
                "main": {
                    "1073741826": {
                        "chainName": "Arbitrum",
                        "chainType": "ARETH",
                        "evm": true,
                        "crossScAddr": "0xf7ba155556e2cd4dfe3fe26e506a14d2f4b97613"
                    },
                    "2147484262": {
                        "chainName": "Optimism",
                        "chainType": "OETH",
                        "evm": true,
                        "crossScAddr": ""
                    },
                    "2153201998": {
                        "chainName": "Wanchain",
                        "chainType": "WAN",
                        "evm": true,
                        "crossScAddr": "0xe85b0D89CbC670733D6a40A9450D8788bE13da47"
                    },
                    "2147483708": {
                        "chainName": "Ethereum",
                        "chainType": "ETH",
                        "evm": true,
                        "crossScAddr": "0xfCeAAaEB8D564a9D0e71Ef36f027b9D162bC334e"
                    },
                    "2147483648": {
                        "chainName": "Bitcoin",
                        "chainType": "BTC",
                        "evm": false,
                        "crossScAddr": ""
                    },
                    "2147484362": {
                        "chainName": "BSC",
                        "chainType": "BNB",
                        "evm": true,
                        "crossScAddr": "0xc3711bdbe7e3063bf6c22e7fed42f782ac82baee"
                    },
                    "2147483792": {
                        "chainName": "XRP L",
                        "chainType": "XRP",
                        "evm": false,
                        "crossScAddr": ""
                    },
                    "2147483650": {
                        "chainName": "Litecoin",
                        "chainType": "LTC",
                        "evm": false,
                        "crossScAddr": ""
                    },
                    "2147492648": {
                        "chainName": "Avalanche",
                        "chainType": "AVAX",
                        "evm": true,
                        "crossScAddr": "0x74e121a34a66D54C33f3291f2cdf26B1cd037c3a"
                    },
                    "1073741825": {
                        "chainName": "Moonriver",
                        "chainType": "MOVR",
                        "evm": true,
                        "crossScAddr": "0xde1ae3c465354f01189150f3836c7c15a1d6671d"
                    },
                    "2147484002": {
                        "chainName": "Polkadot",
                        "chainType": "DOT",
                        "evm": false,
                        "crossScAddr": ""
                    },
                    "2147484655": {
                        "chainName": "Fantom",
                        "chainType": "FTM",
                        "evm": true,
                        "crossScAddr": "0xccffe9d337f3c1b16bd271d109e691246fd69ee3"
                    },
                    "1073741828": {
                        "chainName": "Moonbeam",
                        "chainType": "GLMR",
                        "evm": true,
                        "crossScAddr": "0x6372aEc6263AA93EAceDC994D38aa9117B6b95B5"
                    },
                    "2147484198": {
                        "chainName": "XinFin",
                        "chainType": "XDC",
                        "evm": true,
                        "crossScAddr": "xdcf7ba155556e2cd4dfe3fe26e506a14d2f4b97613"
                    },
                    "2147484614": {
                        "chainName": "Polygon",
                        "chainType": "MATIC",
                        "evm": true,
                        "crossScAddr": "0x2216072a246a84f7b9ce0f1415dd239c9bf201ab"
                    },
                    "2147484644": {
                        "chainName": "OKT",
                        "chainType": "OKT",
                        "evm": true,
                        "crossScAddr": "0xf7ba155556e2cd4dfe3fe26e506a14d2f4b97613"
                    },
                    "1073741829": {
                        "chainName": "CLV",
                        "chainType": "CLV",
                        "evm": true,
                        "crossScAddr": "0xf7ba155556e2cd4dfe3fe26e506a14d2f4b97613"
                    }
                },
                "test": {
                    "1073741826": {
                        "chainName": "Arbitrum",
                        "chainType": "ARETH",
                        "evm": true,
                        "crossScAddr": "0xbf0deb5cd8e072018632e9646b4fe998d4047a86"
                    },
                    "2147483843": {
                        "chainName": "Tron",
                        "chainType": "TRX",
                        "evm": true,
                        "crossScAddr": "41f1b7f2e5aaccce1e39ad9baa8ff6aa828a01ce19"
                    },
                    "2147484262": {
                        "chainName": "Optimism",
                        "chainType": "OETH",
                        "evm": true,
                        "crossScAddr": "0x0467bf248bddb10e4465214e9baf404ff8e93332"
                    },
                    "2153201998": {
                        "chainName": "Wanchain",
                        "chainType": "WAN",
                        "evm": true,
                        "crossScAddr": "0x62de27e16f6f31d9aa5b02f4599fc6e21b339e79"
                    },
                    "2147483708": {
                        "chainName": "Ethereum",
                        "chainType": "ETH",
                        "evm": true,
                        "crossScAddr": "0x7b985c9379a13d2adf685aee9cb6d2e3f1809ffb"
                    },
                    "2147483648": {
                        "chainName": "Bitcoin",
                        "chainType": "BTC",
                        "evm": false,
                        "crossScAddr": ""
                    },
                    "2147484362": {
                        "chainName": "BSC",
                        "chainType": "BNB",
                        "evm": true,
                        "crossScAddr": "0xb12513cfcb13b7be59ba431c040b7206b0a211b9"
                    },
                    "2147483792": {
                        "chainName": "XRP L",
                        "chainType": "XRP",
                        "evm": false,
                        "crossScAddr": ""
                    },
                    "2147483650": {
                        "chainName": "Litecoin",
                        "chainType": "LTC",
                        "evm": false,
                        "crossScAddr": ""
                    },
                    "2147492648": {
                        "chainName": "Avalanche",
                        "chainType": "AVAX",
                        "evm": true,
                        "crossScAddr": "0x4c200a0867753454db78af84d147bd03e567f234"
                    },
                    "1073741825": {
                        "chainName": "moonbase",
                        "chainType": "MOVR",
                        "evm": true,
                        "crossScAddr": "0x9274be9167c7dba7f81b61d3870e0272cb8474f6"
                    },
                    "2147484002": {
                        "chainName": "WND",
                        "chainType": "WND",
                        "evm": false,
                        "crossScAddr": ""
                    },
                    "2147484655": {
                        "chainName": "Fantom",
                        "chainType": "FTM",
                        "evm": true,
                        "crossScAddr": "0x265fc66e84939f36d90ee38734afe4a770d2c114"
                    },
                    "2147484198": {
                        "chainName": "XinFin",
                        "chainType": "XDC",
                        "evm": true,
                        "crossScAddr": "0x18edfe1e49ca89157384832482c66e95ea9b0fca"
                    },
                    "2147484614": {
                        "chainName": "Polygon",
                        "chainType": "MATIC",
                        "evm": true,
                        "crossScAddr": "0xb5bf1013898a93f0bd902f6e346ed6cbb627b791"
                    },
                    "2147484644": {
                        "chainName": "OKT",
                        "chainType": "OKT",
                        "evm": true,
                        "crossScAddr": "0x5292b2936dad44edfbfb2929f9f246304167843b"
                    },
                    "1073741829": {
                        "chainName": "CLV",
                        "chainType": "CLV",
                        "evm": true,
                        "crossScAddr": "0xcef19151f44fc3df678554f35c1dd7f29afacde8"
                    }
                }
            }
            ''')
    crossPoolTokenInfo = json.loads('''{
	"main": {
		"74": {
			"Asset": "VEE",
			"TokenAddress": "0x3709e8615e02c15b096f8a9b460ccb8ca8194e86",
			"PoolScAddress": "0xae110a0e6e5ddb0108f6d752f754b575d62b7534",
			"originalAmount": 0,
			"chainType": "AVAX"
		},
		"178": {
			"Asset": "FINN",
			"TokenAddress": "0xbD4191828AEFF23Fb9E0249A5AE583a4B9425e49",
			"PoolScAddress": "0xbd4191828aeff23fb9e0249a5ae583a4b9425e49",
			"originalAmount": 75000000,
			"chainType": "CLV"
		}
	},
	"test": {
		"74": {
			"Asset": "VEE",
			"TokenAddress": "0x372d0695e75563d9180f8ce31c9924d7e8aaac47",
			"PoolScAddress": "0x372d0695e75563d9180f8ce31c9924d7e8aaac47",
			"originalAmount": 500000,
			"chainType": "AVAX"
		},
		"178": {
			"Asset": "FINN",
			"TokenAddress": "0xbD4191828AEFF23Fb9E0249A5AE583a4B9425e49",
			"PoolScAddress": "0x4f0aac04c190fb1aef5c55f81b41f72615c820c4",
			"originalAmount": 100000,
			"chainType": "CLV"
		}
	}
}''')
    evmChainCrossSc = json.loads('''{
	"main": {
		"ETH": "0xfCeAAaEB8D564a9D0e71Ef36f027b9D162bC334e",
		"WAN": "0xe85b0D89CbC670733D6a40A9450D8788bE13da47",
		"BNB": "0xc3711bdbe7e3063bf6c22e7fed42f782ac82baee",
		"AVAX": "0x74e121a34a66D54C33f3291f2cdf26B1cd037c3a",
		"MOVR": "0xde1ae3c465354f01189150f3836c7c15a1d6671d",
		"FTM": "0xccffe9d337f3c1b16bd271d109e691246fd69ee3",
		"GLMR": "0x6372aEc6263AA93EAceDC994D38aa9117B6b95B5",
		"XDC": "xdcf7ba155556e2cd4dfe3fe26e506a14d2f4b97613",
		"MATIC": "0x2216072a246a84f7b9ce0f1415dd239c9bf201ab",
		"OKT": "0xf7ba155556e2cd4dfe3fe26e506a14d2f4b97613",
		"CLV": "0xf7ba155556e2cd4dfe3fe26e506a14d2f4b97613",
		"ARETH": "0xf7ba155556e2cd4dfe3fe26e506a14d2f4b97613"
	},
	"test": {
		"ETH": "0x7b985c9379a13d2adf685aee9cb6d2e3f1809ffb",
		"WAN": "0x62de27e16f6f31d9aa5b02f4599fc6e21b339e79",
		"BNB": "0xb12513cfcb13b7be59ba431c040b7206b0a211b9",
		"AVAX": "0x4c200a0867753454db78af84d147bd03e567f234",
		"MOVR": "0x9274be9167c7dba7f81b61d3870e0272cb8474f6",
		"FTM": "0x265fc66e84939f36d90ee38734afe4a770d2c114",
		"XDC": "0x18edfe1e49ca89157384832482c66e95ea9b0fca",
		"MATIC": "0xb5bf1013898a93f0bd902f6e346ed6cbb627b791",
		"OKT": "0x5292b2936dad44edfbfb2929f9f246304167843b",
		"CLV": "0xcef19151f44fc3df678554f35c1dd7f29afacde8",
		"ARETH": "0xbf0deb5cd8e072018632e9646b4fe998d4047a86",
		"TRX": "41f1b7f2e5aaccce1e39ad9baa8ff6aa828a01ce19",
		"OETH": "0x0467bf248bddb10e4465214e9baf404ff8e93332"
	}
}''')
    token_utl = TokenPairsUtility(net,iWAN_Config,chainInfo,crossPoolTokenInfo,evmChainCrossSc)

    print(token_utl.getTokenPairs())



