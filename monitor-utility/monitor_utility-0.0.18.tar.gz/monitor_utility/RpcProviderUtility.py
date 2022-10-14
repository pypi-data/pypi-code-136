import json
import requests
import time
from websocket import create_connection
from substrateinterface import SubstrateInterface  # for DOT RPC

class PROVIDER_SELECTOR:
    def __init__(self,print_flag=False):
        '''
        :param rpcs:
                [
                    "https://nodes.wandevs.org/eth",
                    "https://eth-mainnet.public.blastapi.io",
                    "https://main-rpc.linkpool.io",
                    "https://rpc.ankr.com/eth"
                ]
        '''
        self.print_flag = print_flag
    def pprint(self,*args,**kwargs):
        if self.print_flag :
            print(*args,**kwargs)

    def getEvmBlkNum(self,rpc,timer=5):
        '''
        :param url:
        :return: str
        '''
        headers = {"Content-Type": "application/json"}
        method = json.dumps({
                            "jsonrpc": "2.0",
                            "method": "eth_blockNumber",
                            "params": [],
                            "id": 1
                 })
        try:
            eth_block = requests.post(url= rpc, headers=headers, data=method,timeout=timer).json()
            BlockNum = int(eth_block['result'], 16)
        except:
            BlockNum = 0
        return BlockNum

    def getXrpBlkNum(self,rpc,timer=15):
        '''
        https://xrpl.org/ledger_data.html
        :param url:
        :return: str
        '''
        method = json.dumps({"method": "server_state", "params": [{}]})
        try:
            ws = create_connection(url=rpc, timeout=timer)
            ws.send(method)
            wanchain_raw = json.loads(ws.recv())
            state = wanchain_raw['result']['state']
            status = wanchain_raw['status']
            ws.close()
            complete_ledgers = state['complete_ledgers']
            BlockNum = complete_ledgers.split(',')[-1].split('-')[-1]
            if status != 'success':  # First check the server state status
                err = 'Server state is {} '.format(status)
            elif len(complete_ledgers.split(',')) > 1:  # Then check the length of complete_ledgers
                err = 'Length of complete_ledgers is {}'.format(len(complete_ledgers.split(',')))
            else:
                err = None
        except Exception as e:
            BlockNum = 0
            err = str(e)
        self.pprint(err)
        return BlockNum

    def getDotBlkNum(self,rpc):
        '''
        :param url:
        :return:
        {"jsonrpc": "2.0", "result": {"currentBlock": 6874227, "highestBlock": 6874227, "startingBlock": 6376299}, "id": 3}
        '''
        try:
            substrate = SubstrateInterface(url=rpc)
            BlockNum = int(substrate.rpc_request('chain_getBlock', [])['result']['block']['header']['number'], 16)
            err = None
        except Exception as e:
            BlockNum = 0
            err = str(e)
        self.pprint('get dot blocknumber faild for {}, due to {}'.format(rpc,err))
        return BlockNum

    def select_best_provider(self,rpcs,getBlockNum):
        '''
        :param : getBlockNum> : function
        :return: return best RPC
        '''
        time_cost_pool = []
        blockNum_pool = []
        rpc_status = {}
        #get the latest block number
        for rpc in rpcs:
            start_time = time.time()
            blockNum = getBlockNum(rpc)
            stop_time = time.time()
            time_cost = stop_time - start_time
            rpc_status[rpc] = {'blockNum':blockNum,'time_cost':time_cost}

        #select the best RPC
        for rpc_node in rpc_status.keys():
            time_cost_pool.append(rpc_status[rpc_node]['time_cost'])
            blockNum_pool.append(int(rpc_status[rpc_node]['blockNum']))

        fastest_rpc = time_cost_pool.index(min(time_cost_pool))
        latestBlock = max(blockNum_pool)
        #to ensure the fastest RPC block number is normal
        if latestBlock - blockNum_pool[fastest_rpc] < 2 and latestBlock!=0:
            return list(rpc_status.keys())[fastest_rpc]
        else:
            return 'All RPCs are unavailable: {} '.format(rpcs)

if __name__ == '__main__':
    selector = PROVIDER_SELECTOR()

    evmrpcs =                 [
                    "https://nodes.wandevs.org/eth",
                    "https://eth-mainnet.public.blastapi.io",
                    "https://main-rpc.linkpool.io",
                    "https://rpc.ankr.com/eth"
                ]
    # rpc = selector.select_best_provider(evmrpcs,selector.getEvmBlkNum)

    xrprpcs = [
			"wss://s1.ripple.com/",
			"wss://nodes.wandevs.org/xrp:443",
			"wss://s2.ripple.com/",
			"wss://xrplcluster.com/"
		]
    # rpc = selector.select_best_provider(xrprpcs,selector.getXrpBlkNum)

    dotrpcs = [
			"wss://nodes.wandevs.org/polkadot",
			"wss://rpc.polkadot.io",
			"wss://polkadot.api.onfinality.io/public-ws"
		]
    rpc = selector.select_best_provider(dotrpcs, selector.getDotBlkNum)
    print(rpc)







