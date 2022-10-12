# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 2021

(C) 2021, Rohde&Schwarz, ramian
"""

import struct
import re


def ConvertWv2BinStream( FileName):
    '''
    Convert large wv files to bin (KS file format), i.e. do not read full iq vector
    '''
    SampleSize = 4 # 2 x 2 bytes
    BlockSize = 50000

    try:
        file = open(FileName, "rb")
        data = file.read( 6000)     # for the header, 62 kB should be sufficient
    except:
        print( "File open error ("+ FileName+")!")

    binaryStart = 0
    tags = ""
    Counter = 0
    ConverterSize = 20
    while (binaryStart == 0) & (Counter < len(data)):
        tags += data[Counter:Counter+ConverterSize].decode("ASCII","ignore")
        Counter += ConverterSize
        #{WAVEFORM-20001: #
        res = re.search("WAVEFORM.{0,20}:.{0,3}#",tags)
        if res != None:
            binaryStart = res.span()[1]

    if (Counter > len(data)) & (binaryStart == 0):
        print( "Required tags not found, potentially incompatible file format!")

    res = re.search("SAMPLES[ ]*:[ ]*(?P<NumberOfSamples>[0-9]*)[ ]*}",tags)
    if res:
        NumberOfSamples = int( res.group("NumberOfSamples"))
    else:
        NumberOfSamples = -1
    
    outFileName = FileName.lower().replace( '.wv', '.bin')
    outfile = open( outFileName, "wb")

    data = data[binaryStart:]
    data = data + file.read( SampleSize-(len(data) % SampleSize))
    NumberOfInt16s = len(data)//2
    SampleCount = NumberOfInt16s // 2
    data = list(struct.unpack("h"*NumberOfInt16s, data))
    for nIdx in range(NumberOfInt16s):
        outfile.write( struct.pack(">h",data[nIdx]))

    
    while SampleCount < NumberOfSamples:
        SamplesToRead = NumberOfSamples-SampleCount
        if SamplesToRead > BlockSize:
            SamplesToRead = BlockSize
        data = file.read( SamplesToRead * SampleSize)
        NumberOfInt16s = len(data)//2
        data = list(struct.unpack("h"*NumberOfInt16s, data))
        for nIdx in range(NumberOfInt16s):
            outfile.write( struct.pack(">h",data[nIdx]))
        SampleCount = SampleCount + SamplesToRead

    file.close()
    outfile.close()



if __name__ == "__main__":
    pass
    # Testcode
    # ConvertWv2BinStream(r'C:\Users\ramian\Documents\gitlab\demo files\DirectDPD.wv')
    # import rskfd
    # iq,fs = rskfd.ReadWv(r'C:\Users\ramian\Documents\gitlab\demo files\DirectDPD.wv')
    # rskfd.WriteBin( iq,fs, r'C:\Users\ramian\Documents\gitlab\demo files\DirectDPD.bin.test')
