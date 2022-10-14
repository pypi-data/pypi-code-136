from multicall import Call, Multicall
from web3 import Web3
import requests
def from_baseUnit(decimal):
    '''
    :param value:
    :param decimal: 1e8,1e18,....
    :return:
    '''
    def from_wei(value):
        return value / decimal
    return from_wei
def to_baseUnit(value):
    '''
    :param value:
    :param decimal: 1e8,1e18,....
    :return:
    '''
    return int(value)

class EMultilCall(Multicall):
    def __init__(self,muticall_addresses):
        '''
        para: 'https://raw.githubusercontent.com/Nevquit/configW/main/MULTICALL_ADDRESSES.json'
        '''
        super(EMultilCall, self).__init__(muticall_addresses)
        self.muticall_addresses = muticall_addresses

    def __call__(self):
        aggregate = Call(
            self.muticall_addresses['MULTICALL_ADDRESSES'][str(self.w3.eth.chainId)],
            'aggregate((address,bytes)[])(uint256,bytes[])',
            returns=None,
            _w3=self.w3,
            block_id=self.block_id
        )
        args = [[[call.target, call.data] for call in self.calls]]
        block, outputs = aggregate(args)
        result = {}
        for call, output in zip(self.calls, outputs):
            result.update(call.decode_output(output))
        return result

class eCall(Call):
    pass



if __name__ == '__main__':
    calls = [Call('0x07FDb4e8f8E420d021B9abEB2B1f6DcE150Ef77c','totalSupply()(uint256)',[['ToTallSupply', to_baseUnit]]),Call('0xc8F5b26589392fDE84eE0482e2b5a77DFbE943Fc','totalSupply()(uint256)',[['ToTall2Supply', to_baseUnit]])]
    multi = EMultilCall(calls,_w3=Web3(Web3.HTTPProvider('https://gwan-ssl.wandevs.org:46891')))
    print(multi())