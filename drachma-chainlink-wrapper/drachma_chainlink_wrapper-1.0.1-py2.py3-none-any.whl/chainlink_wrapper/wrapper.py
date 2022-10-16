# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 19:04:47 2022

@author: godof
"""

from web3 import Web3

class OracleClient:
    def __init__(self, address):
        self.address = address
    
    def price_eth_pair(self):
        web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
        # AggregatorV3Interface ABI
        abi = '[{ "inputs": [ { "internalType": "address", "name": "_ETHConverterAddress", "type": "address" }, { "internalType": "address", "name": "_asset", "type": "address" } ], "stateMutability": "nonpayable", "type": "constructor" }, { "inputs": [], "name": "ETHConverterAddress", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "asset", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getLatestPrice", "outputs": [ { "internalType": "int256", "name": "", "type": "int256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "convertETHPriceToUSD", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "viewAssetAddress", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }]' 
        
        # Set up contract instance
        contract = web3.eth.contract(address=self.address, abi=abi)
        
        current_price = contract.functions.getLatestPrice().call()
        price = (current_price)/10**18
        return price
    
    def price_eth_pair_to_usd(self):
        web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
        # AggregatorV3Interface ABI
        abi = '[{ "inputs": [ { "internalType": "address", "name": "_ETHConverterAddress", "type": "address" }, { "internalType": "address", "name": "_asset", "type": "address" } ], "stateMutability": "nonpayable", "type": "constructor" }, { "inputs": [], "name": "ETHConverterAddress", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "asset", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getLatestPrice", "outputs": [ { "internalType": "int256", "name": "", "type": "int256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "convertETHPriceToUSD", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "viewAssetAddress", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }]' 
        
        # Set up contract instance
        contract = web3.eth.contract(address=self.address, abi=abi)
        
        current_price = contract.functions.convertETHPriceToUSD().call()
        price = (current_price)/10**26
        return price
   
    def price_usd_pair(self):
        web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
        # AggregatorV3Interface ABI
        abi = '[{ "inputs": [ { "internalType": "address", "name": "_ETHConverterAddress", "type": "address" }, { "internalType": "address", "name": "_asset", "type": "address" } ], "stateMutability": "nonpayable", "type": "constructor" }, { "inputs": [], "name": "ETHConverterAddress", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "asset", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getLatestPrice", "outputs": [ { "internalType": "int256", "name": "", "type": "int256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "convertETHPriceToUSD", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "viewAssetAddress", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }]' 
        
        # Set up contract instance
        contract = web3.eth.contract(address=self.address, abi=abi)
        
        current_price = contract.functions.getLatestPrice().call()
        price = (current_price)/10**8
        return price