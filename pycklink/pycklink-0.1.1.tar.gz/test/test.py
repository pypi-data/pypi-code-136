# -*- coding:utf-8 -*-

'''
Created on 2021
@author: tanji
'''

import os
import ctypes
import pycklink

root_path = os.path.dirname(__file__)
addr = ctypes.c_uint64(0x42020000)
bin_filename = "test.bin"
bin_filedir = os.path.join(root_path, bin_filename)


if __name__ == '__main__':
    link = pycklink.CKLink()
    # Show version informations
    link.target_print_version()
    # Initialize target interfaces
    link.target_init()
    # Check whether target is connected or not
    res = link.target_is_connected()
    print(res)
    # Open target
    tgt = link.target_open()
    print(tgt)  
    link.cfg.target = tgt
    if res and tgt:        
        ''' memory access test '''
        # Enable downloading memory with DDC
        link.target_enable_ddc(tgt)       
        with open(bin_filedir, 'rb') as f:
            bin_data = bytearray(f.read())          
        size = len(bin_data)
        print(size)
        wbuff = (ctypes.c_char*size)(*(bin_data))
        rbuff = (ctypes.c_char*size)()
        print(wbuff[0:10])
        # Write memory from target
        link.target_write_memory(tgt, addr, wbuff, size)
        # Disable downloading memory with DDC
        link.target_disable_ddc(tgt)
        # Read memory from target
        link.target_read_memory(tgt, addr, rbuff, size)
        print(rbuff[0:10])
        # link.target_resume(tgt)            
        
        ''' register access test '''
        rn = pycklink.Register()
        for i in range(15):
            rn.num = i
            rn.value.val32 = 0x12345678
            res = link.target_write_cpu_reg(tgt, rn)
            ctypes.memset(ctypes.byref(rn.value), 0, ctypes.sizeof(rn.value))
            print(i, rn.value.val32)
            res = link.target_read_cpu_reg(tgt, rn)
            print(i, rn.value.val32)
        
        ''' breakpoint test '''   
        res = link.soft_breakpoint_add(tgt, 0x0, 2)  
        print(res)
        res = link.hard_breakpoint_add(tgt, 0x100, 2)  
        print(res)  
        
        link.target_close(tgt)
        












