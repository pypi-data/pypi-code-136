# import utils.utils as utils
# from utils.CustomTx import CustomTxType
import defichainUtils.utils.utils as utils
from defichainUtils.utils.CustomTx import CustomTxType
from dataclasses import asdict


def decodeCustomTx(hex):
    '''
    Hex String without OP_RETURN and DfTx Marker
    ''' 
    functionMarker = utils.hexToString(hex[:2])
    if functionMarker == 'j':
        res = decodeSetGovVariableHeight(hex[2:])
        if res != None:
            res['name'] = 'setgovheight'
    elif functionMarker == 's':
        res = decodePoolSwap(hex[2:])
        if res != None:
            res['name'] = 'poolswap'
    elif functionMarker == 'i':
        res = decodePoolSwapV2(hex[2:])
        if res != None:
            res['name'] = 'compositeswap'
    elif functionMarker == 'l':
        res = decodeAddPoolLiquidity(hex[2:])
        if res != None:
            res['name'] = 'addpoolliquidity'
    elif functionMarker == 'r':
        res = decodeRemovePoolLiquidity(hex[2:])
        if res != None:
            res['name'] = 'removepoolliquidity'
    elif functionMarker == 'p':
        res = decodeCreatePoolPair(hex[2:])
        if res != None:
            res['name'] = 'createpoolpair'
    elif functionMarker == 'B':
        res = decodeAccountToAccount(hex[2:])
        if res != None:
            res['name'] = 'accounttoaccount'
    elif functionMarker == 'X':
        res = decodeTakeLoan(hex[2:])
        if res != None:
            res['name'] = 'takeloan'
    elif functionMarker == 'H':
        res = decodePaybackLoan(hex[2:])
        if res != None:
            res['name'] = 'paybackloan'
    elif functionMarker == 'k':
        res = decodePaybackLoanV2(hex[2:])
        if res != None:
            res['name'] = 'paybackloanv2'
    elif functionMarker == 'a':
        res = decodeAnyAccountsToAccounts(hex[2:])
        if res != None:
            res['name'] = 'anyaccountstoaccounts'
    elif functionMarker == 'e':
        res = decodeCloseVault(hex[2:])
        if res != None:
            res['name'] = 'closevault'
    elif functionMarker == 'V':
        res = decodeVault(hex[2:])
        if res != None:
            res['name'] = 'vault'
    elif functionMarker == 'v':
        res = decodeUpdateVault(hex[2:])
        if res != None:
            res['name'] = 'updatevault'
    elif functionMarker == 'I':
        res = decodeAuctionBid(hex[2:])
        if res != None:
            res['name'] = 'auctionbid'
    elif functionMarker == 'J':
        res = decodeWithdrawFromVault(hex[2:])
        if res != None:
            res['name'] = 'withdrawfromvault'
    elif functionMarker == 'S':
        res = decodeDepositToVault(hex[2:])
        if res != None:
            res['name'] = 'deposittovault'
            
    else:
        c = CustomTxType()
        for key, value in asdict(c).items():
            if value == functionMarker:
                return {
                    'name': str(key).lower(),
                    'hex': hex[2:]
                }
        return None
    return res


def decodeSetGovVariableHeight(hex):
    # Only data part of hex string!
    govVariable = hex[2:2+2*int(hex[:2],16)]
    hex = hex[2+2*int(hex[:2],16):]
    if utils.stringToHex('ATTRIBUTES') == govVariable:
        # if hex[:2] != '01':
        #     return {
        #         'error': 1,
        #         'msg': 'Expected only one value in this function. Please contact package DEV.'
        #     }
        variables = [
            {'key':'attributes', 'type': [
                {'bytesCount': 4, 'key': 'unknown', 'type': int,'endian':None},
                {'bytesCount': 1, 'key': 'type', 'type': str,'endian':None,'abort':['o']},
                {'bytesCount': 1, 'key': 'typeId', 'type': int,'endian':None},
                {'bytesCount': 4, 'key': 'key', 'type': str,'endian':'big'},
                {'bytesCount': 4, 'key': 'keyId', 'type': int,'endian':'little'},
                {'bytesCount': 8, 'key': 'value', 'type': int,'endian':'little'}]
            },
            {'bytesCount': 4, 'key': 'height', 'type': int,'endian':'little'}
        ]
        return searchHex(variables,hex)
    elif utils.stringToHex('ICX_TAKERFEE_PER_BTC') == govVariable:
        # TODO: write Decoding
        pass
    elif utils.stringToHex('LP_LOAN_TOKEN_SPLITS') == govVariable:
        # TODO: write Decoding
        pass
    elif utils.stringToHex('LP_SPLITS') == govVariable:
        # TODO: write Decoding
        pass
    elif utils.stringToHex('ORACLE_DEVIATION') == govVariable:
        # TODO: write Decoding
        pass
    else:
        return None

def decodePoolSwap(hex):
    variables = [
        {'key': 'from', 'type': 'address','endian':None},
        {'bytesCount':1, 'key': 'fromTokenId', 'type': int,'endian':None},
        {'bytesCount': 8, 'key': 'fromAmount', 'type': int,'endian':'little'},
        {'key': 'to', 'type': 'address','endian':None},
        {'bytesCount':1, 'key': 'toTokenId', 'type': int,'endian':None},
        {'bytesCount': 8, 'key': 'maxPriceCounter', 'type': int,'endian':'little'},
        {'bytesCount': 8, 'key': 'maxPriceDenominator', 'type': int,'endian':'little'}
    ]
    return searchHex(variables,hex)
def decodePoolSwapV2(hex):
    variables = [
        {'key': 'from', 'type': 'address','endian':None},
        {'bytesCount':1, 'key': 'fromTokenId', 'type': int,'endian':None},
        {'bytesCount': 8, 'key': 'fromAmount', 'type': int,'endian':'little'},
        {'key': 'to', 'type': 'address','endian':None},
        {'bytesCount':1, 'key': 'toTokenId', 'type': int,'endian':None},
        {'bytesCount': 8, 'key': 'maxPriceCounter', 'type': int,'endian':'little'},
        {'bytesCount': 8, 'key': 'maxPriceDenominator', 'type': int,'endian':'little'},
        {'key':'pools', 'type':
            [{'bytesCount': 1, 'type': int,'endian':None}]
        }
    ]
    return searchHex(variables,hex)
def decodeAddPoolLiquidity(hex):
    variables = [
        {'key':'addresses', 'type': [
            {'key': 'from', 'type': 'address','endian':None},
            {'key': 'amounts', 'type': [
                {'bytesCount': 4,'key': 'tokenId', 'type': int,'endian':'little'},
                {'bytesCount': 8, 'key': 'amount', 'type': int,'endian':'little'}
                ]}
        ]},
        {'key': 'shareAddress', 'type': 'address','endian':None}
    ]
    return searchHex(variables,hex)
def decodeRemovePoolLiquidity(hex):
    variables = [
        {'key': 'from', 'type': 'address','endian':None},
        {'bytesCount':1, 'key': 'tokenId', 'type': int,'endian':None},
        {'bytesCount': 8, 'key': 'amount', 'type': int,'endian':'little'}
    ]
    return searchHex(variables,hex)
def decodeCreatePoolPair(hex):
    variables = [
        {'bytesCount':1, 'key': 'tokenIdA', 'type': int,'endian':None},
        {'bytesCount':1, 'key': 'tokenIdB', 'type': int,'endian':None},
        {'bytesCount': 8, 'key': 'commission', 'type': int,'endian':'little'},
        {'key': 'from', 'type': 'address','endian':None},
        {'bytesCount':1, 'key': 'status', 'type': int,'endian':None},
        {'key': 'customRewards', 'type': 'rest' ,'endian':None}
    ]
    return searchHex(variables,hex)
def decodeAccountToAccount(hex):
    variables = [
        {'key': 'from', 'type': 'address','endian':None},
        {'key':'addresses', 'type': [
            {'key': 'to', 'type': 'address','endian':None},
            {'key': 'amounts', 'type': [
                {'bytesCount': 4,'key': 'tokenId', 'type': int,'endian':'little'},
                {'bytesCount': 8, 'key': 'amount', 'type': int,'endian':'little'}
                ]}
        ]}
    ]
    return searchHex(variables,hex)
def decodeTakeLoan(hex):
    variables = [
        {'bytesCount': 32,'key': 'vault', 'type': 'hex','endian':'little'},
        {'key': 'to', 'type': 'address','endian':None},
        {'key': 'amounts', 'type': [
            {'bytesCount': 4,'key': 'tokenId', 'type': int,'endian':'little'},
            {'bytesCount': 8, 'key': 'amount', 'type': int,'endian':'little'}
        ]}
    ]
    return searchHex(variables,hex)
def decodePaybackLoan(hex):
    variables = [
        {'bytesCount': 32,'key': 'vault', 'type': 'hex','endian':'little'},
        {'key': 'from', 'type': 'address','endian':None},
        {'key': 'amounts', 'type': [
            {'bytesCount': 4,'key': 'tokenId', 'type': int,'endian':'little'},
            {'bytesCount': 8, 'key': 'amount', 'type': int,'endian':'little'}
        ]}
    ]
    return searchHex(variables,hex)
def decodePaybackLoanV2(hex):
    variables = [
        {'bytesCount': 32,'key': 'vaultId', 'type': 'hex','endian':'little'},
        {'key': 'from', 'type': 'address','endian':None},
        {'key': 'tokens', 'type': [
            {'bytesCount': 1,'key': 'tokenId', 'type': int,'endian':None},
            {'key': 'amounts', 'type': [
                {'bytesCount': 4,'key': 'tokenId', 'type': int,'endian':'little'},
                {'bytesCount': 8, 'key': 'amount', 'type': int,'endian':'little'}
            ]}
        ]}
    ]
    return searchHex(variables,hex)
def decodeAnyAccountsToAccounts(hex):
    variables = [
        {'key':'fromAddresses', 'type': [
            {'key': 'from', 'type': 'address','endian':None},
            {'key': 'amounts', 'type': [
                {'bytesCount': 4,'key': 'tokenId', 'type': int,'endian':'little'},
                {'bytesCount': 8, 'key': 'amount', 'type': int,'endian':'little'}
                ]}
        ]},
        {'key':'toAddresses', 'type': [
            {'key': 'to', 'type': 'address','endian':None},
            {'key': 'amounts', 'type': [
                {'bytesCount': 4,'key': 'tokenId', 'type': int,'endian':'little'},
                {'bytesCount': 8, 'key': 'amount', 'type': int,'endian':'little'}
                ]}
        ]}
    ]
    return searchHex(variables,hex)
def decodeCloseVault(hex):
    variables = [
        {'bytesCount': 32, 'key': 'vaultId', 'type': 'hex', 'endian':'little'},
        {'key': 'shareAddress', 'type': 'address','endian':None}
    ]
    return searchHex(variables,hex)
def decodeUpdateVault(hex):
    variables = [
        {'bytesCount': 32, 'key': 'vaultId', 'type': 'hex', 'endian':'little'},
        {'key': 'ownerAddress', 'type': 'address','endian':None},
        {'bytesCount': 1,'key': 'lengthLoanSchemeName', 'type': int,'endian':'little'},
        {'bytesCount': 'rest', 'key': 'loanScheme', 'type': str,'endian':None}
    ]
    return searchHex(variables,hex)
def decodeVault(hex):
    variables = [
        {'key': 'address', 'type': 'address','endian':None},
        {'bytesCount': 1,'key': 'lengthLoanSchemeName', 'type': int,'endian':'little'},
        {'bytesCount': 'rest', 'key': 'loanScheme', 'type': str,'endian':None}
    ]
    return searchHex(variables,hex)
def decodeAuctionBid(hex):
    variables = [
        {'bytesCount': 32, 'key': 'vaultId', 'type': 'hex', 'endian':'little'},
        {'bytesCount': 4,'key': 'index', 'type': int,'endian':'little'},
        {'key': 'address', 'type': 'address','endian':None},
        {'bytesCount': 1, 'key': 'tokenId', 'type': int,'endian':'little'},
        {'bytesCount': 8,'key': 'amount', 'type': int,'endian':'little'}
    ]
    return searchHex(variables,hex)
def decodeWithdrawFromVault(hex):
    variables = [
        {'bytesCount': 32, 'key': 'vaultId', 'type': 'hex', 'endian':'little'},
        {'key': 'to', 'type': 'address','endian':None},
        {'bytesCount': 1, 'key': 'tokenId', 'type': int,'endian':'little'},
        {'bytesCount': 8,'key': 'amount', 'type': int,'endian':'little'}
    ]
    return searchHex(variables,hex)
def decodeDepositToVault(hex):
    variables = [
        {'bytesCount': 32, 'key': 'vaultId', 'type': 'hex', 'endian':'little'},
        {'key': 'from', 'type': 'address','endian':None},
        {'bytesCount': 1, 'key': 'tokenId', 'type': int,'endian':'little'},
        {'bytesCount': 8,'key': 'amount', 'type': int,'endian':'little'}
    ]
    return searchHex(variables,hex)
def recursiveSearchHex(variable,hex):
    abort = False
    if type(variable['type']) == list:
        cnt = int(hex[:2],16)
        hex = hex[2:]
        arr = []
        for i in range(0,cnt):
            res = {}
            for idx,listVariable in enumerate(variable['type']):
                (key,value,hex,abort) = recursiveSearchHex(listVariable,hex)
                if 'abort' in variable['type'][idx] and value in variable['type'][idx]['abort']:
                    abort = True
                    break
                if key is None and idx == len(variable['type']) - 1:
                    res = value
                else:
                    res[key] = value
            arr.append(res)
        return variable['key'],arr,hex,abort
    else:
        (key,value,hex) = getValue(variable,hex)
        return key,value,hex,abort

def searchHex(variables:list,hex:str):
    res = {}
    for variable in variables:
        (key,value,hex,abort) = recursiveSearchHex(variable,hex)
        res[key] = value
        if abort:
            break
    
    if len(hex) == 0:
        res['hex'] = None
    else:
        res['hex'] = hex
    return res

def getValue(variable,hex):
    # Select subString from hex depending on length info in hex String or length info from variable input
    if variable['type'] == 'address':
        if 'key' in variable and variable['key'] == 'to' and hex[:2] == '00':
            return variable['key'],None,hex[2:]
        # START - Remove leading zeros
        while True:
            if len(hex) >= 2 and hex[:2] == '00':
                hex = hex[2:]
            else:
                break
        if len(hex) < 2:
            return None,None,None
        # END - Remove leading zeros
        hexLength = int(hex[:2],16)
        if hex[2:6] == '76a9' and hexLength == 25:
            addressType = 'base58'
            addressVersion = 18
            addressLength = int(hex[6:8],16)
            hexOfInterest = hex[8:8+2*addressLength]
            hex = hex[2+2*hexLength:]
        elif hex[2:4] == 'a9' and hexLength == 23: 
            addressType = 'base58'
            addressVersion = 90
            addressLength = int(hex[4:6],16)
            hexOfInterest = hex[6:6+2*addressLength]
            hex = hex[2+2*hexLength:]
        else:
            addressType = 'bech32'
            addressVersion = hex[2:4]
            addressLength = int(hex[4:6],16)
            hexOfInterest = hex[6:6+2*addressLength]
            hex = hex[2+2*hexLength:]
    elif variable['type'] == 'rest':
        hexOfInterest = hex
        hex = ''
    else:
        if variable['bytesCount'] == 'rest':
            hexOfInterest = hex
            hex = ''
        else:
            hexOfInterest = hex[:2*variable['bytesCount']]
            hex = hex[2*variable['bytesCount']:]

    # Handle Endian Transformation
    if variable['endian'] == 'big':
        hexOfInterest = utils.convert_hex(hexOfInterest,'big','little')
    elif variable['endian'] == 'little':
        hexOfInterest = utils.convert_hex(hexOfInterest,'little','big')

    # Extract Value
    if variable['type'] == int:
        if hexOfInterest == '':
            valueOfInterest = 0
        else:
            valueOfInterest = int(hexOfInterest,16)
    elif variable['type'] == str:
        if hexOfInterest == '':
            valueOfInterest = hexOfInterest
        else:
            valueOfInterest = utils.hexToString(hexOfInterest)
    elif variable['type'] == 'address':
        valueOfInterest = utils.decodeHexToAddress(hexOfInterest,addressType,addressVersion)
    elif variable['type'] == 'hex':
        valueOfInterest = hexOfInterest
    else:
        valueOfInterest = None
    
    if 'key' not in variable:
        return None,valueOfInterest,hex
    if variable['key'] != None:
        return variable['key'],valueOfInterest,hex
    return None,None,hex