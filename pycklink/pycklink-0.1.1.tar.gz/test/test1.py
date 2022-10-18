# -*- coding:utf-8 -*-

'''
Created on 2021
@author: tanjiaxi
'''

import os
import cklink

#root_path = os.path.dirname(__file__)
addr = 0x42020000
bin_filedir = "test.bin"
#bin_filedir = os.path.join(root_path, bin_filename)


if __name__ == '__main__':
    link = cklink.CKLink()
    # Show version informations
    link.print_version()
    # Open target
    link.open()  
    if link.connected():         
        ''' memory access test '''
        # Enable downloading memory with DDC
        #link.enable_ddc()     
        with open(bin_filedir, 'rb') as f:
            bin_data = f.read()
        print(bin_data[:100])        
        # Write memory to target
        link.write_memory(addr, bin_data)
        # Disable downloading memory with DDC
        #link.disable_ddc()
        # Read memory from target
        res = link.read_memory(addr, 100)
        print(res)
                
        ''' register access test '''
        for i in range(15):
            link.write_cpu_reg(i, 0x12345678)
            res = link.read_cpu_reg(i)
            print(i, res)
            
        ''' breakpoint test '''   
        res = link.add_soft_breakpoint(0x0, 2)  
        print(res)
        res = link.add_hard_breakpoint(0x100, 2)  
        print(res) 
        res = link.clear_breakpoint()
        print(res)       
        link.resume()
        
        #link.close()
        












