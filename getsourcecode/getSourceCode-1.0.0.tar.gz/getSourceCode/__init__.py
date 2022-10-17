# -*- coding: utf-8 -*-
import time
from argparse import RawTextHelpFormatter
from random import randint
import requests
import argparse
import base64
import json
import os
import re

apiKeys = {
    "cronos": [],
    "heco": [
        "JCTU517KN68FM9APHJWPQ7FVPHKFIAUCZB",
        "GWB1A9WKKFVQCE572YH8TA6CHRNVE42R41",
        "ZD6TXYMR7CPM2AVR8I2CNKVF3TMHIQRTKF",
        "MTZUEG344W46RK9HU8ZI8G2HQB91RU474Q",
        "RQ6ZMRWVSE33BEKZ999AYDKX1HU1A2Z5V2",
        "IG8YQGB4ZZCRXNDB7RY3H2SIYPM6SSB67F",
        "3VY6FNPNPWKZ5EXQFXQP6TZUGUR3FSDM11",

    ],
    "heco-testnet": [
        "JCTU517KN68FM9APHJWPQ7FVPHKFIAUCZB",
        "GWB1A9WKKFVQCE572YH8TA6CHRNVE42R41",
        "ZD6TXYMR7CPM2AVR8I2CNKVF3TMHIQRTKF",
        "MTZUEG344W46RK9HU8ZI8G2HQB91RU474Q",
        "RQ6ZMRWVSE33BEKZ999AYDKX1HU1A2Z5V2",
        "IG8YQGB4ZZCRXNDB7RY3H2SIYPM6SSB67F",
        "3VY6FNPNPWKZ5EXQFXQP6TZUGUR3FSDM11",

    ],
    "eth": [
        "B69GNP1IXCXJUGTWVCZPW4PS6KFDQ9MNJ1",
        "TRUHXX8K4D5E4665M22FUYZ6F4ZP4SC6UQ",
        "373ZPPAM1QZYS55Q5AW24BKW124BGPMPIA",
        "75FE5RHNXQJPRY6A4EGXTWJKE4M7783W6F",
        "TRUHXX8K4D5E4665M22FUYZ6F4ZP4SC6UQ",
        "Q8K1J5WIXHVQWV1XHVFF1INTPHWFZP5AZV",
        "KWPEX5CZ437P2JRB2U7WZ37VQFAVZFXXP6"
    ],
    "goerli": [
        "B69GNP1IXCXJUGTWVCZPW4PS6KFDQ9MNJ1",
        "TRUHXX8K4D5E4665M22FUYZ6F4ZP4SC6UQ",
        "373ZPPAM1QZYS55Q5AW24BKW124BGPMPIA",
        "75FE5RHNXQJPRY6A4EGXTWJKE4M7783W6F",
        "TRUHXX8K4D5E4665M22FUYZ6F4ZP4SC6UQ",
        "Q8K1J5WIXHVQWV1XHVFF1INTPHWFZP5AZV",
        "KWPEX5CZ437P2JRB2U7WZ37VQFAVZFXXP6"
    ],
    "rinkeby": [
        "B69GNP1IXCXJUGTWVCZPW4PS6KFDQ9MNJ1",
        "TRUHXX8K4D5E4665M22FUYZ6F4ZP4SC6UQ",
        "373ZPPAM1QZYS55Q5AW24BKW124BGPMPIA",
        "75FE5RHNXQJPRY6A4EGXTWJKE4M7783W6F",
        "TRUHXX8K4D5E4665M22FUYZ6F4ZP4SC6UQ",
        "Q8K1J5WIXHVQWV1XHVFF1INTPHWFZP5AZV",
        "KWPEX5CZ437P2JRB2U7WZ37VQFAVZFXXP6"
    ],
    "ropsten": [
        "B69GNP1IXCXJUGTWVCZPW4PS6KFDQ9MNJ1",
        "TRUHXX8K4D5E4665M22FUYZ6F4ZP4SC6UQ",
        "373ZPPAM1QZYS55Q5AW24BKW124BGPMPIA",
        "75FE5RHNXQJPRY6A4EGXTWJKE4M7783W6F",
        "TRUHXX8K4D5E4665M22FUYZ6F4ZP4SC6UQ",
        "Q8K1J5WIXHVQWV1XHVFF1INTPHWFZP5AZV",
        "KWPEX5CZ437P2JRB2U7WZ37VQFAVZFXXP6"
    ],
    "kovan": [
        "B69GNP1IXCXJUGTWVCZPW4PS6KFDQ9MNJ1",
        "TRUHXX8K4D5E4665M22FUYZ6F4ZP4SC6UQ",
        "373ZPPAM1QZYS55Q5AW24BKW124BGPMPIA",
        "75FE5RHNXQJPRY6A4EGXTWJKE4M7783W6F",
        "TRUHXX8K4D5E4665M22FUYZ6F4ZP4SC6UQ",
        "Q8K1J5WIXHVQWV1XHVFF1INTPHWFZP5AZV",
        "KWPEX5CZ437P2JRB2U7WZ37VQFAVZFXXP6"
    ],
    "bsc": [
        "1GX9SE6TRAUPWY93UCI8VEGYK5PMRFP7E6",
        "XR4VB9FIQRI83BMVZ9HYKJWE58EQ7HCMH1",
        "P54XXZPM8SCQ7WJ46QUZCNZRNQMGTFBAES",
        "YMUWBHKDD1ZXUPWDJI3TXY9EB2T7TP9JR7",
        "YI443WMRI9EEC7NXZRV6SKI2NPZ6ZTM97J",
        "T5NGBCEJ48Y6BVU5CKZZ8STZZ9JM1XVKR3",
        "AYU647AC1FDKWX9BTRIUTTTUZWXSFUZV96"
    ],
    "bsc-testnet": [
        "1GX9SE6TRAUPWY93UCI8VEGYK5PMRFP7E6",
        "XR4VB9FIQRI83BMVZ9HYKJWE58EQ7HCMH1",
        "P54XXZPM8SCQ7WJ46QUZCNZRNQMGTFBAES",
        "YMUWBHKDD1ZXUPWDJI3TXY9EB2T7TP9JR7",
        "YI443WMRI9EEC7NXZRV6SKI2NPZ6ZTM97J",
        "T5NGBCEJ48Y6BVU5CKZZ8STZZ9JM1XVKR3",
        "AYU647AC1FDKWX9BTRIUTTTUZWXSFUZV96"
    ],
    "fantom": [
        "B2DMSKF3CXC6M74B4RA83IXVV1T4BNX25K",
        "HTSU459QXXIXX2YVST9JAG9RKJ7PEEDUKQ",
        "KGKTQQSAP3398UUBUG4ZPUBYEWWUHUI3CW",
        "DDMXPVS7W9J7MEB79I52NS6MEUWXTUJZVD",
        "8MEXS5HP26NSXRQG3URD9KXTPZB25513Y3",
        "RJZ578B8YAY1CHA1ZZED2NQM8SUGJX6KUU"
    ],
    "ftm-testnet": [
        "B2DMSKF3CXC6M74B4RA83IXVV1T4BNX25K",
        "HTSU459QXXIXX2YVST9JAG9RKJ7PEEDUKQ",
        "KGKTQQSAP3398UUBUG4ZPUBYEWWUHUI3CW",
        "DDMXPVS7W9J7MEB79I52NS6MEUWXTUJZVD",
        "8MEXS5HP26NSXRQG3URD9KXTPZB25513Y3",
        "RJZ578B8YAY1CHA1ZZED2NQM8SUGJX6KUU"
    ],
    "poly": [
        "UE3WWC97VU5KZ3NW9XV39ZPRVM5RM8IA1E",
        "GS5AXJY8TVDSCRFSTCJR6YW5T67ZCARYKD",
        "HEFJ8U7QSE56UAJ67K7IRZ831WC4D2796G",
        "QNZR6UNWK41KE3DAVYXNXDWZ93G7J2WC1C",
        "39I4N6AG381FNJX5M2TG19E4YZXMB4EA9A",
        "PUXK78CMRYI6GUDUKZPFZE6XX8IA2QEYCX",
        "JJTJR6QUQZ5VQC65WBGETZIV4UI43BZ9HM",
        "42SIV2ZWIC4DKZ55ABYS2WKTT4AKFVWVA2"
    ],
    "poly-testnet": [
        "UE3WWC97VU5KZ3NW9XV39ZPRVM5RM8IA1E",
        "GS5AXJY8TVDSCRFSTCJR6YW5T67ZCARYKD",
        "HEFJ8U7QSE56UAJ67K7IRZ831WC4D2796G",
        "QNZR6UNWK41KE3DAVYXNXDWZ93G7J2WC1C",
        "39I4N6AG381FNJX5M2TG19E4YZXMB4EA9A",
        "PUXK78CMRYI6GUDUKZPFZE6XX8IA2QEYCX",
        "JJTJR6QUQZ5VQC65WBGETZIV4UI43BZ9HM",
        "42SIV2ZWIC4DKZ55ABYS2WKTT4AKFVWVA2"
    ],
    "avax": [
        "VZRVZISMTHCERDSJ9HCXGNAJIBJAPNYPB8",
        "JI7GW3TZSWUIBTYSYC6PESJEPQ2W9X3BI9",
        "PIGRN8GKHTB72J9HQK83MHVNAHAB7QZ9UT",
        "SDXQ4PTDMAZP84JMRX1CP7MUF5X5DTU3D9",
        "G2XD761SEV475CQQ53UAEIVI1WIZE1JD3R",
        "2MY2JCYF98W8VHU5B55NYY6DDCM1CEBQ5E"
    ],
    "avax-testnet": [
        "VZRVZISMTHCERDSJ9HCXGNAJIBJAPNYPB8",
        "JI7GW3TZSWUIBTYSYC6PESJEPQ2W9X3BI9",
        "PIGRN8GKHTB72J9HQK83MHVNAHAB7QZ9UT",
        "SDXQ4PTDMAZP84JMRX1CP7MUF5X5DTU3D9",
        "G2XD761SEV475CQQ53UAEIVI1WIZE1JD3R",
        "2MY2JCYF98W8VHU5B55NYY6DDCM1CEBQ5E"
    ],
    "arbi": [
        "7JE9ARGTHG6SYCSID23R2B86E2BGJ7S5UE",
        "QCUDSYNPRS9S9JVHT2JRX7F75XPGCIKZIG",
        "GW1WG96PT5FBI71BP9KKKSAN2BJ9FW2HSV",
        "KCB4MA88NH2UW26JQWTRIT2P2AQYSTGI3Y",
        "K84DVIXX16BZEPR4J6NXE9HHVNTSFAQDIC",
        "NNJ96AD95RXNUN7C4QJ34D53CHGMUU1J5H"
    ],
    "arbi-testnet": [
        "7JE9ARGTHG6SYCSID23R2B86E2BGJ7S5UE",
        "QCUDSYNPRS9S9JVHT2JRX7F75XPGCIKZIG",
        "GW1WG96PT5FBI71BP9KKKSAN2BJ9FW2HSV",
        "KCB4MA88NH2UW26JQWTRIT2P2AQYSTGI3Y",
        "K84DVIXX16BZEPR4J6NXE9HHVNTSFAQDIC",
        "NNJ96AD95RXNUN7C4QJ34D53CHGMUU1J5H"
    ],
    "moonriver": ["E9W9NPRB1NCJTEAAA512U8UJYRD55MZSH3", "Y7MNACP4TTIC7FH962FTHQD3QJYJZ7USU4", "IWZMJSBHN17PGCFHXY1EFTGVXZUSIF7FUC"],
    "moonbeam": ["PPGYVB7AR97IDSVKZZJ7TD67WVNDBM74AY", "IV47Y5R8SRKW9KC5DVDYB5RVC3GCV5IHKA", "MQPRQUKMHEFRE7KK6WFXIHZTDMC8RCWX65"],
    "moonbase": ["","",""],
    "boba": ["8KNECUPEU3FW673BA65P5MD13WRHHWVWTX","UMBCJRG9TNMB4UUPF4CC679AAPZYRXRRH6","UYDGY2WRN29IG27YSVJ5NNQ3792VZQAH2A"],
    "boba-testnet": ["","",""],
}

defaultFolder = "contract"

reqUrl = {
    "heco": "https://api.hecoinfo.com/api?module=contract&action=getsourcecode&address=",
    "eth": "https://api.etherscan.io/api?module=contract&action=getsourcecode&address=",
    "bsc": "https://api.bscscan.com/api?module=contract&action=getsourcecode&address=",
    "fantom": "https://api.ftmscan.com/api?module=contract&action=getsourcecode&address=",
    "poly": "https://api.polygonscan.com/api?module=contract&action=getsourcecode&address=",
    "avax": "https://api.snowtrace.io/api?module=contract&action=getsourcecode&address=",
    "arbi": "https://api.arbiscan.io/api?module=contract&action=getsourcecode&address=",
    "goerli": "https://api-goerli.etherscan.io/api?module=contract&action=getsourcecode&address=",
    "cronos": "https://cronos.org/explorer/api?module=contract&action=getsourcecode&address=",
    "kovan": "https://api-kovan.etherscan.io/api?module=contract&action=getsourcecode&address=",
    "rinkeby": "https://api-rinkeby.etherscan.io/api?module=contract&action=getsourcecode&address=",
    "ropsten": "https://api-ropsten.etherscan.io/api?module=contract&action=getsourcecode&address=",
    "bsc-testnet": "https://api-testnet.bscscan.com/api?module=contract&action=getsourcecode&address=",
    "heco-testnet": "https://api-testnet.hecoinfo.com/api?module=contract&action=getsourcecode&address=",
    "ftm-testnet": "https://api-testnet.ftmscan.com/api?module=contract&action=getsourcecode&address=",
    "poly-testnet": "https://api-testnet.polygonscan.com/api?module=contract&action=getsourcecode&address=",
    "avax-testnet": "https://api-testnet.snowtrace.io/api?module=contract&action=getsourcecode&address=",
    "arbi-testnet": "https://api-testnet.arbiscan.io/api?module=contract&action=getsourcecode&address=",
    "moonriver": "https://api-moonriver.moonscan.io/api?module=contract&action=getsourcecode&address=",
    "moonbeam": "https://api-moonbeam.moonscan.io/api?module=contract&action=getsourcecode&address=",
    "moonbase": "https://api-moonbase.moonscan.io/api?module=contract&action=getsourcecode&address=",
    "boba":"https://api.bobascan.com/api?module=contract&action=getsourcecode&address=",
    "boba-testnet":"https://api-testnet.bobascan.com/api?module=contract&action=getsourcecode&address="

}

currentPath = os.getcwd()

proxy = ""

contractIndex = 0


def _argparse():
    parser = argparse.ArgumentParser(
        description="To get contract source code. \n\nSupport network: \nHeco|ETH|BSC|Fantom|Poly|AVAX|ARBI|Tron\nCronos|moonbeam|moonriver|boba|okex\navax-testnet|arbi-testnet|poly-testnet\nbsc-testnet|heco-testnet|ftm-testnet\nGoerli|Kovan|Rinkeby|Ropsten\nmoonbase|boba-testnet",
        formatter_class=RawTextHelpFormatter)
    parser.add_argument('-i', default='', dest='inputFile', help='Input file path including contract addresses.')
    parser.add_argument('-o', default='', dest='outputFolder', help='Choose a folder to export.')
    parser.add_argument('-a', default='', dest='address', help='A string including contract addresses.')
    parser.add_argument('-n', default='', dest='network', help='Which network to get source code.')
    parser.add_argument('-k', action="store_true", dest='key', help='Provide some api keys.')
    parser.add_argument('-p', default='', dest='proxy', help='Use a proxy.')

    return parser.parse_args()


def getKeys(network):
    try:
        if network not in apiKeys.keys():
            return False
        keys = apiKeys[network]
        return keys
    except Exception as e:
        print("--------------------------------------")
        print("error line:", e.__traceback__.tb_lineno)
        print("error type:", e)
        print("--------------------------------------")
        os._exit(0)


def getKey(network):
    try:
        if network not in apiKeys.keys():
            return False
        keys = apiKeys[network]
        if keys == []:
            return "Cronos do not need a api key."
        randomNum = randint(0, len(keys) - 1)
        return keys[randomNum]
    except Exception as e:
        print("--------------------------------------")
        print("error line:", e.__traceback__.tb_lineno)
        print("error type:", e)
        print("--------------------------------------")
        os._exit(0)


def printKey(network):
    try:
        keys = getKeys(network)
        if keys:
            outputKeys = "\n".join(keys)
            print(outputKeys)
        else:
            print("Please choose a right network. For example: getCode -k -n BSC")
    except Exception as e:
        print("--------------------------------------")
        print("error line:", e.__traceback__.tb_lineno)
        print("error type:", e)
        print("--------------------------------------")
        os._exit(0)


def getCode(inputFile, outputFolder, address, network):
    try:
        addresses = []
        if network.lower() == "Tron".lower():
            if inputFile != "":
                addresses = getAddresses(inputFile, True, "")
            elif address != "":
                addresses = getAddresses("", True, address)
            else:
                print("Erorr input")
            sendTron(addresses, outputFolder)
        elif network.lower() == "Okex".lower():
            addresses = []
            if inputFile != "":
                addresses = getAddresses(inputFile, True, "")
            elif address != "":
                addresses = getAddresses("", False, address)
            else:
                print("Erorr input")
            sendOkex(addresses, outputFolder)
        else:
            keys = getKeys(network)
            if not keys and keys != []:
                print("Invalid network")
                os._exit(0)
            if inputFile != "":
                addresses = getAddresses(inputFile, False, "")
            elif address != "":
                addresses = getAddresses("", False, address)
            else:
                print("Erorr input")
                os._exit(0)
            if addresses != []:
                sendRequest(addresses, outputFolder, network)
            else:
                print("Erorr address")
                os._exit(0)
    except Exception as e:
        print("--------------------------------------")
        print("error line:", e.__traceback__.tb_lineno)
        print("error type:", e)
        print("--------------------------------------")
        os._exit(0)


def getAddresses(inputFile, isTron, addString):
    try:
        if inputFile != "":
            filePath = currentPath + "//" + inputFile
            addresses = []
            if os.path.isfile(filePath) and os.path.exists(filePath):
                addStr = ""
                with open(filePath, 'r+', encoding='utf-8') as fr:
                    for line in fr.readlines():
                        addStr = addStr + line.replace('\n', ' ')
                if isTron:
                    addresses = re.findall(r'T[a-zA-Z\d]{33}', addStr)
                else:
                    addresses = re.findall(r'0x[a-zA-Z\d]{40}', addStr)
        elif addString != "":
            if isTron:
                addresses = re.findall(r'T[a-zA-Z\d]{33}', addString)
            else:
                addresses = re.findall(r'0x[a-zA-Z\d]{40}', addString)
        return addresses
    except Exception as e:
        print("--------------------------------------")
        print("error line:", e.__traceback__.tb_lineno)
        print("error type:", e)
        print("--------------------------------------")
        os._exit(0)


def exportResult(result, outputFolder, network):
    global contractIndex
    if "ContractName" not in result.keys():
        return
    try:
        index = 0
        isMultiFile = False
        contractName = result['ContractName']
        sourceCode = result['SourceCode'].replace("\r\n", "\n")
        if sourceCode.find('.sol":{"content":') != -1:
            isMultiFile = True
        if "\"language\":" in sourceCode or isMultiFile:
            contractFolder = contractName
            mkdir(contractFolder)
            if not isMultiFile:
                sourceCode = json.loads(sourceCode[1:-1])['sources']
            else:
                sourceCode = json.loads(sourceCode)
            for key in sourceCode.keys():
                contractName = key.split(".")[0] + ".sol"
                while os.path.exists(contractFolder + "//" + contractName):
                    contractName = key.split(".")[0] + "_{}".format(index) + ".sol"
                    index += 1
                index = 0
                mkdir(os.path.split(contractFolder + "//" + contractName)[0])
                with open(contractFolder + "//" + contractName, "w+", encoding='utf-8') as fw:
                    fw.write(sourceCode[key]["content"].replace('\r\n', '\n'))
                print(f'{contractIndex}: {contractFolder + "/" + contractName}'.replace('//', '/'))
                contractIndex += 1
        else:
            contractFolder = defaultFolder if outputFolder == "" else outputFolder
            mkdir(contractFolder)
            contractName = contractName + ".sol"
            while os.path.exists(contractFolder + "//" + contractName):
                contractName = result['ContractName'] + "_{}".format(index) + ".sol"
                index += 1
            mkdir(os.path.split(contractFolder + "//" + contractName)[0])
            with open(contractFolder + "//" + contractName, "w+", encoding='utf-8') as fw:
                fw.write(sourceCode.replace('\r\n', '\n'))
            print(f'{contractIndex}: {contractFolder + "/" + contractName}'.replace('//', '/'))
            contractIndex += 1
        if network == "cronos":
            if result["IsProxy"] == True:
                addresses = []
                addresses.append(result['ImplementationAddress'])
                sendRequest(addresses, "ImplementationAddress", network)
        elif result['Implementation'] != "":
            addresses = []
            addresses.append(result['Implementation'])
            sendRequest(addresses, "Implementation", network)
    except Exception as e:
        print("--------------------------------------")
        print("error line:", e.__traceback__.tb_lineno)
        print("error type:", e)
        print("--------------------------------------")
        os._exit(0)


def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False


def sendRequest(addresses, outputFolder, network):
    try:
        proxies = {
            "https": "http://" + proxy,
            "http": "http://" + proxy
        }
        header = {
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
        }
        for address in addresses:
            # print(addresses,network)
            realUrl = reqUrl[network] + address + "&apikey=" + getKey(network)
            if proxy != "":
                req = requests.get(realUrl, proxies=proxies, headers=header)
            else:
                req = requests.get(realUrl, headers=header)
            results = json.loads(req.text)['result']

            if type(results) == dict:
                outputData = results
            elif type(results) == list:
                outputData = results[0]
            exportResult(outputData, outputFolder, network)
    except Exception as e:
        print("--------------------------------------")
        print("error line:", e.__traceback__.tb_lineno)
        print("error type:", e)
        print("--------------------------------------")
        os._exit(0)


def sendTron(addresses, outputFolder):
    global contractIndex
    try:
        apiUrl = "https://apiasia.tronscan.io:5566/api/solidity/contract/info"
        for address in addresses:
            data = {
                "contractAddress": address
            }
            req = requests.post(apiUrl, data=data)
            # print(req.text)
            if json.loads(req.text)["code"] == 200:
                contract_code = json.loads(req.text)["data"]["contract_code"]
                contractFolder = defaultFolder if outputFolder == "" else outputFolder
                mkdir(contractFolder)
                for code in contract_code:
                    index = 0
                    contractName = code['name']
                    while os.path.exists(contractFolder + "//" + contractName):
                        contractName = code['name'].split('.')[0] + "_{}".format(index) + ".sol"
                        index += 1
                    mkdir(os.path.split(contractFolder + "//" + contractName)[0])
                    with open(contractFolder + "//" + contractName, "w+", encoding='utf-8') as fw:
                        fw.write(str(base64.b64decode(code['code']), 'utf-8').replace('\r\n', '\n'))
                    print(f'{contractIndex}: {contractFolder + "/" + contractName}'.replace('//', '/'))
                    contractIndex += 1
    except Exception as e:
        print("--------------------------------------")
        print("error line:", e.__traceback__.tb_lineno)
        print("error type:", e)
        print("--------------------------------------")
        os._exit(0)


def sendOkex(addresses, outputFolder):
    global contractIndex
    try:
        for address in addresses:
            apiUrl = f"https://www.oklink.com/api/explorer/v1/okexchain/addresses/{address}/contract"
            req = requests.get(apiUrl)
            # print(req.text)
            if json.loads(req.text)["code"] == 0:
                if 'contractSourceList' in json.loads(req.text)["data"].keys():
                    contract_code_list = json.loads(req.text)["data"]["contractSourceList"]
                else:
                    contract_code_list = [{
                        "name":json.loads(req.text)["data"]["name"],
                        "sourceCode":json.loads(req.text)["data"]["contractSource"],
                    }]
                main_contract = json.loads(req.text)["data"]["name"]
                contractFolder = defaultFolder if outputFolder == "" else outputFolder
                mkdir(contractFolder)
                for code in contract_code_list:
                    index = 0
                    contractName = code['name']
                    while os.path.exists(contractFolder + "//" + contractName):
                        contractName = code['name'].split('.')[0] + "_{}".format(index) + ".sol"
                        index += 1
                    mkdir(os.path.split(contractFolder + "//" + contractName)[0])
                    with open(contractFolder + "//" + contractName, "w+", encoding='utf-8') as fw:
                        fw.write(code['sourceCode'].replace('\r\n', '\n'))
                    print(f'{contractIndex}: {contractFolder + "/" + contractName}'.replace('//', '/'))
                    contractIndex += 1
                impl = ""
                if "implContractAddress" in json.loads(req.text)["data"].keys():
                    impl = json.loads(req.text)["data"]["implContractAddress"]
                if impl != "":
                    addresses = [impl]
                    sendOkex(addresses, "implContract")
    except Exception as e:
        print("--------------------------------------")
        print("error line:", e.__traceback__.tb_lineno)
        print("error type:", e)
        print("--------------------------------------")
        os._exit(0)


def main():
    try:
        parser = _argparse()
        inputFile = parser.inputFile
        outputFolder = parser.outputFolder
        address = parser.address
        network = parser.network.lower()
        # print(parser)
        global proxy
        proxy = parser.proxy
        key = parser.key
        if key:
            printKey(network)
        elif inputFile != "" or address != "":
            if network in reqUrl.keys():
                if "etherscan" in reqUrl[network]:
                    if proxy == "":
                        print("In order to use the ETHSCAN API, you need to provide an proxy.")
                        os._exit(0)
            getCode(inputFile, outputFolder, address, network)
        else:
            print("Invalid command")
            os._exit(0)
        print('\nSuccess.')

    except Exception as e:
        print("--------------------------------------")
        print("error line:", e.__traceback__.tb_lineno)
        print("error type:", e)
        print("--------------------------------------")
        os._exit(0)


if __name__ == '__main__':
    main()
