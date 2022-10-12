# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 2021

(C) 2021, Rohde&Schwarz, ramian
"""

import struct
import re
import rskfd

def ConvertIiQq2Wv():
    '''
    Test
    '''
    fs = 320e6
    data = rskfd.ReadIqw( r'\\Rsint.net\data\MU\SATURN\GROUP\GR_1E\TRANSFER\Reichert\signal\higher_qams.iiqq', iqiq=False)
    rskfd.WriteWv( data, fs, r'\\Rsint.net\data\MU\SATURN\GROUP\GR_1E\TRANSFER\Reichert\signal\higher_qams_DEC.wv')
    # rskfd.WriteBin( data, fs, r'C:\Users\ramian\Documents\waveforms\Keysight PXI Waveforms\WLAN_11be_320MHz_MCS13_dec.bin')
    rskfd.WriteIqTar( data, fs, r'\\Rsint.net\data\MU\SATURN\GROUP\GR_1E\TRANSFER\Reichert\signal\higher_qams_DEC.iq.tar')



def ReadFile( filename):
    '''
    Test
    '''
    data,fs = rskfd.ReadWv( filename)
    print( f'RMS power in file: {rskfd.MeanPower( data)} dBm, peak power: {rskfd.MeanPower( data)} dBm.\n')
    rskfd.WriteWv( data, fs, 'myfilename.wv')



def ReadWvTest():
    '''
    Test the wv reading routine (tags!!)
    '''
    iq, fs = rskfd.ReadWv(r'C:\Users\ramian\Documents\gitlab\demo files\DirectDPD.wv')
    iq, fs = rskfd.ReadWv(r'C:\Users\ramian\Documents\gitlab\demo files\IQ_d.wv')


if __name__ == "__main__":
	pass
    # ReadWvTest()
    