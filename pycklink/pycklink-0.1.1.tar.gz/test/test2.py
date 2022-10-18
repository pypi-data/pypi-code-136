# -*- coding:utf-8 -*-

'''
Created on 2021
@author: tanjiaxi
'''

import os
import cklink
import time
import binascii

addr = 0x22010000  # 570490880
bin_filedir = "eflash_loader_32m.bin"


if __name__ == '__main__':
    link = cklink.CKLink()
    # Show version informations
    link.print_version()
    # Open target
    link.open()  
    if link.connected(): 
        link.reset(2)         
        link.halt()
 
        with open(bin_filedir, 'rb') as f:
            bin_data = f.read()[192:]
        print(bin_data[:100])    
         
        # Write memory to target
        link.write_memory(addr, bin_data)
        # Read memory from target
        res = link.read_memory(addr, 100)
        print(res)
              
        link.write_cpu_reg(32, addr)
        res = link.read_cpu_reg(32)
        print(hex(res))
        
        link.write_cpu_reg(32, addr)
        res = link.read_cpu_reg(32)
        print(hex(res))
        link.resume()
        time.sleep(1)
         
#         print(0x4202BFF0)
#         print(binascii.unhexlify("59445248"))
        link.halt()
        res = link.write_memory(0x4202BFF0, binascii.unhexlify("48524459"))   
        res = link.read_memory(0x4202BFF0, 4)
        print(binascii.hexlify(res))
        link.resume()
        time.sleep(1)
        link.halt()
        res = link.read_memory(0x4202BFF0, 4)
        print(binascii.hexlify(res))
        link.resume()
  
        
        


        

        
        

        
        
        

        


        












