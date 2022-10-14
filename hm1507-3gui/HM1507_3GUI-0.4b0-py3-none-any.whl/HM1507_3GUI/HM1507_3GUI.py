# HM1507_3GUI starts a GUI to save plots of the data from the HAMEG HM1507-3 oscilloscope. Based on the freely available program by Jean-Claude Feltes.
# 
# Lukas Freudenberg (lfreudenberg@uni-osnabrueck.de)
# Jean-Claude Feltes (jean-claude.feltes@education.lu)
# 
# 14.10.2022, ver0.4a
# 
# Changelog
#   - 14.04.2022: Added displays for the settings of the oscilloscope,
#                 changed port connection to use DSMVLib,
#                 changed plot to resemble scope grid,
#                 changed scaling to always save data in V and s,
#                 fixed a bug that caused the wrong pair of value and unit to be calculated from the oscilloscope data,
#                 updated documentation to match doxygen standard
#   - 04.10.2022: Added functionality to select save path for plots,
#                 changed appearance of saved messages
#                 fixed a bug that caused the dual plot to be saved in two separate files
#   - 30.09.2022: Added functionality to automatically save the plots to user directory,
#                 GUI redesign
#   - unknown:    Initial version by Jean-Claude Feltes
#
# Permission is hereby granted, free of charge, to any person 
# obtaining a copy of this software and associated documentation 
# files (the "Software"), to deal in the Software without 
# restriction, including without limitation the rights to use, copy,
# modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software 
# is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be 
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR 
# OTHER DEALINGS IN THE SOFTWARE.

# Import official modules
import numpy as np
from matplotlib.pyplot import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from tkinter import messagebox

from PIL import Image, ImageTk
import os
import time
# Import custom module
from DSMVLib import DSMVLib as L

""" HM1507 for py3  
Remote viewer for HM1507 oscilloscope
programmed by jean-claude.feltes@education.lu

"""

#----------------------------------------------------------------------

import serial
import time
import matplotlib.pyplot as plt
import os

def hmfoo():
    pass

## @brief HM1507 Class with methods to connect and disconnect.
class HM1507_3GUI:
    ## @brief Initialize an run the GUI.
    def __init__(self):
        self.ser = L.serPort(command=b" " + b"\x0D" + b"\x0A", question=b"ID?" + b"\x0D" + b"\x0A", answer=b"ID:HM1507-3                 \r\n", 
                             final=b"rm0" + b"\x0D" + b"\x0A", stopbitsV=2, trsctsV=1, timeoutV=10)
        # create window
        self.window=Tk()
        L.window=self.window
        self.window.title("HAMEG HM1507-3 Interface v0.4")
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure((0, 1), weight=1)
        # list with all UI elements
        self.uiElements = []
        # list with the grid parameters of all UI elements
        self.uiGridParams = []
        # create the oscilloscope object
        #oszi=HM1507()
        # create default saving directory
        try:
            os.mkdir(os.path.expanduser("~") + "/HM1507-3/")
        except FileExistsError:
            pass
        ## @brief current save directory
        self.saveDir = os.path.expanduser("~") + "/HM1507-3/"
        path = L.savePath("HM1507-3", self.saveDir)
        ## @brief next filename
        self.filename = path[len(self.saveDir):len(path)]
        # create plot area
        self.fig1 = Figure(figsize=(5, 4), layout='constrained')
        self.ax1 = self.fig1.add_subplot(111)
        self.ax1.set_xlabel("Time (s)")
        self.ax1.set_ylabel("Voltage CH1 (V)")
        self.ax1.yaxis.label.set_color('blue')
        self.ax1.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.ax1.set_yticks([-4, -3, -2, -1, 0, 1, 2, 3, 4])
        self.ax1.ticklabel_format(scilimits=(-3, 3))
        self.ax1.grid(True)
        self.ax1.autoscale(False)
        self.canvas1 = FigureCanvasTkAgg(self.fig1)
        self.canvas1.draw()
        self.uiElements.append(self.canvas1.get_tk_widget())
        self.uiGridParams.append([0, 0, 1, 1, "NESW"])
        self.ax2 = self.ax1.twinx()
        self.ax2.set_ylabel("Voltage CH2 (V)")
        self.ax2.yaxis.label.set_color('red')
        self.ax2.set_yticks([-4, -3, -2, -1, 0, 1, 2, 3, 4])
        self.ax2.grid(True)
        # create frame for controls
        self.controlFrame = Frame(master=self.window, relief=RIDGE, borderwidth=2)
        self.uiElements.append(self.controlFrame)
        self.uiGridParams.append([0, 1, 2, 1, "NESW"])
        self.btnCH1 = Button(master=self.controlFrame, text="CH1", command=self.plot_CH1)
        self.uiElements.append(self.btnCH1)
        self.uiGridParams.append([0, 0, 1, 1, "WE"])
        self.btnCH2 = Button(master=self.controlFrame, text="CH2", command=self.plot_CH2)
        self.uiElements.append(self.btnCH2)
        self.uiGridParams.append([1, 0, 1, 1, "WE"])
        self.btnCH12 = Button(master=self.controlFrame, text="CH1 + CH2", command=self.plot_dual)
        self.uiElements.append(self.btnCH12)
        self.uiGridParams.append([2, 0, 1, 1, "WE"])
        self.btnSaveDir = Button(master=self.controlFrame, text="Select saving directory", command = self.selectDir)
        self.uiElements.append(self.btnSaveDir)
        self.uiGridParams.append([3, 0, 1, 1, "WE"])
        # labels
        self.labelNext = Label(master=self.controlFrame, text="next file", font=("", 8))
        self.uiElements.append(self.labelNext)
        self.uiGridParams.append([4, 0, 1, 2, "WE"])
        self.labelFile = Label(master=self.controlFrame, text=self.filename)
        self.uiElements.append(self.labelFile)
        self.uiGridParams.append([5, 0, 1, 2, "WE"])
        self.labelSep = Label(master=self.controlFrame, text=" ")
        self.uiElements.append(self.labelSep)
        self.uiGridParams.append([6, 0, 1, 2, "WE"])
        self.labelA = Label(master=self.controlFrame, text="A:1s")
        self.uiElements.append(self.labelA)
        self.uiGridParams.append([7, 0, 1, 2, "WE"])
        self.labelY1 = Label(master=self.controlFrame, text="Y1:1V")
        self.uiElements.append(self.labelY1)
        self.uiGridParams.append([8, 0, 1, 2, "WE"])
        self.labelY2 = Label(master=self.controlFrame, text="Y2:1V")
        self.uiElements.append(self.labelY2)
        self.uiGridParams.append([9, 0, 1, 2, "WE"])
        self.labelPath = Label(master=self.window, text="Current save directory: " + self.saveDir)
        self.uiElements.append(self.labelPath)
        self.uiGridParams.append([1, 0, 1, 2, "WE"])
        L.buildUI(self.uiElements, self.uiGridParams)
        self.window.mainloop()
    
    ## @brief Open the serial port.
    def OpenPort(self):
        print ("Opened " + self.ser.portstr)
        if self.ser.isOpen()==False:
            self.ser.open()
    
    ## @brief Close the serial port.
    def ClosePort(self):
        self.ser.close()
        
    ## @brief Send a command to the oscilloscope.
    #  <CR> and <LF> are appended to the command.
    #  @param s command byte
    def SendCommand(self,s):
        self.ser.write(s + b"\x0D" + b"\x0A")
    
    ## @brief Send a command to the oscilloscope and read the returned answer.
    #  <CR> and <LF> are appended to the command.
    #  @param s command byte
    #  @return answer from the oscilloscope
    def SendCommandReadAnswer(self,s):
        self.SendCommand(s)        
        ok=self.ser.readline()
        return ok        
    
    ## @brief Initialize the remote mode for the oscilloscope to read data.
    def Connect(self):
        print ("connect")
        self.OpenPort() 
        ok=self.SendCommandReadAnswer(b" ")
    
    ## @brief Terminate the remote mode for the oscilloscope.
    def Disconnect(self):
        print ("disconnect")
        ok=self.SendCommandReadAnswer(b"rm0")
        print ("close port")
        self.ClosePort()
    
    ## @brief Read the version of the oscilloscope.
    #  
    #  @return version of the oscilloscope
    def Version(self):
        return self.SendCommandReadAnswer(b"VERS?")
    
    ## @brief Read the ID of the oscilloscope.
    #  
    #  @return ID of the oscilloscope (should be "ID:HM1507-3                 \r\n")
    def ID(self):
        return self.SendCommandReadAnswer(b"ID?")
    
    ## @brief Read the ID and version of the oscilloscope and print it.
    def PrintInfo(self):
        print (self.ID())
        print (self.Version())    
       
#-----------------------------------------------------------------------    
    ## @brief Read DEVICE DATA FIELD.
    #  
    #  @return VoltsPerDIV1 Volts per grid box for channel 1
    #  @return VoltsPerDIV2 Volts per grid box for channel 2
    #  @return Yunit1 unit of the voltage scale for channel 1
    #  @return Yunit2 unit of the voltage scale for channel 2
    #  @return TimePerDIVValue seconds per grid box
    #  @return TimeperDIVUnit unit of the time scale
    def ReadDDF(self):
        self.SendCommand(b"DDF?")
        
        # read response (should be "DDF:" )
        ok=b""
        ok=self.ser.read(4)
        
        # read 14 bytes containing info
        DDF=b'\x00'              #  1 dummy byte   
        for i in range(0,14):    #read 14 bytes to DDF[1...14]
            DDF=DDF + self.ser.read()
        
        # VERMODE in DDF(1)...DDF(3)
        #ch1M, ch2M = scale factors + inverted + probe info
        
        # 10:1 probe CH1 ?
        if (DDF[3] & 64): ch1M = 10 
        else: ch1M = 1
            
        # 10:1 probe CH2 ?
        if (DDF[3] & 4):
            ch2M = 10
        else:
            ch2M = 1
            
        # Channel inverted?
        if DDF[1] & 32:
            ch1M = -ch1M           
        if DDF[2] & 32:
            ch2M = -ch2M
                        
        # CH1/CH2 Volt/DIV
        # array with volt/div  values .  Attention! all must be float otherwise error in calculation! 
        Volts=[0, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0, 200.0, 500.0, 1.0, 2.0, 5.0, 10.0, 20.0]
        
        Counter = DDF[1] & 15
        VoltsPerDIV1 = Volts[Counter + 1] * ch1M
        if Counter < 10: 
            Yunit1= "mV"
        else:
            Yunit1 = "V"
                
        Counter = DDF[2] & 15
        VoltsPerDIV2 = Volts[Counter + 1] * ch2M
        if Counter < 10: 
            Yunit2= "mV"
        else:
            Yunit2 = "V"
            
        # X Time/DIV, value and unit
        # array with time values to select from (must be float!!)
        XVal = [1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0, 200.0, 500.0]
        Counter = DDF[4] & 31
        k = Counter + 5
        k = k % 9         # k mod 9
        TimePerDIVValue = XVal[k]
        
        #Time/DIV unit
        if Counter in range(0,4):
            TimeperDIVUnit = "ns"
        elif  Counter in range(4,13):
            TimeperDIVUnit = "µs"   
        elif  Counter in range(13,22):
            TimeperDIVUnit = "ms"   
        elif  Counter in range(22,29):
            TimeperDIVUnit = "s"   
        else:
            print ("Error reading time/div")
                    
        return VoltsPerDIV1, VoltsPerDIV2, Yunit1, Yunit2, TimePerDIVValue, TimeperDIVUnit
#-----------------------------------------------------------------------
    ## @biref Read Wave Form Preamble.
    #  
    #  @return XresPerDIV resolution per grid box (time scale)
    #  @return YresPerDIV resolution per grid box (voltage scale)
    #  @return Y1Position vertical offset of channel 1
    #  @return Y2Position vertical offset of channel 2
    def ReadWFMPRE(self):
        self.SendCommand(b"WFMPRE?")
        
        # read 14 bytes containing info
        WFMPRE=b' '                 #  1 dummy byte     
        
        for i in range(0,17):       #read 17 bytes to WFMPRE[1...17]
            WFMPRE+=self.ser.read()    
            
        XresPerDIV = WFMPRE[10] + WFMPRE[11] * 256
        YresPerDIV = WFMPRE[12] + WFMPRE[13] * 256
        Y1Position =WFMPRE[14]+WFMPRE[15]*256
        Y2Position =WFMPRE[16]+WFMPRE[17]*256
        
        # correction for negative values:
        if Y1Position & 0x8000: Y1Position = -(65536-Y1Position)
        if Y2Position & 0x8000: Y2Position = -(65536-Y2Position)
                        
        return XresPerDIV, YresPerDIV,Y1Position,Y2Position
#-----------------------------------------------------------------------        
    ## @brief Read raw waveform data.
    #  
    #  @param channel channel to read data for (1 or 2)
    #  @return bytearray with the 2048 data points
    def ReadWaveform(self, channel):
        # command:
        if channel==2: 
            sc=b"RDWFM2:"
        else: 
            sc=b"RDWFM1:"
        sc+=b'\x00\x00\x00\x08'
        self.SendCommand (sc)
             
        # read response (should be "RDWFM..." )
        ok=b""
        ok=self.ser.read(11)
                
        # read 2048 bytes containing waveform data
        w=bytearray ()         #create empty array w for data
        
        for i in range(0,2048):    #read 2048 bytes to w[0...2047]
            w.extend(self.ser.read())
            
        return w    
#-----------------------------------------------------------------------
    ## @brief Calls ReadDDF and ReadWFMPRE to get the basic settings.
    #  
    #  @return VoltsPerDIV1 Volts per grid box for channel 1
    #  @return VoltsPerDIV2 Volts per grid box for channel 2
    #  @return Yunit1 unit of the voltage scale for channel 1
    #  @return Yunit2 unit of the voltage scale for channel 2
    #  @return TimePerDIVValue seconds per grid box
    #  @return TimeperDIVUnit unit of the time scale
    #  @return XresPerDIV resolution per grid box (time scale)
    #  @return YresPerDIV resolution per grid box (voltage scale)
    #  @return Y1Position vertical offset of channel 1
    #  @return Y2Position vertical offset of channel 2
    def ReadSettings(self):
        # read settings from oscilloscope
        (VoltsPerDIV1, VoltsPerDIV2, Yunit1, Yunit2, TimePerDIVValue,TimeperDIVUnit)=self.ReadDDF()
        (XresPerDIV, YresPerDIV,Y1Position,Y2Position)=self.ReadWFMPRE()
        
        # default values for Xres, Yres:
        if XresPerDIV==0: XresPerDIV = 200
        if YresPerDIV==0: YresPerDIV = 25
        
        # Voltage window:
        U1min = (-128 - Y1Position) / YresPerDIV * VoltsPerDIV1
        U1max = (128 - Y1Position) / YresPerDIV * VoltsPerDIV1
        U2min = (-128 - Y2Position) / YresPerDIV * VoltsPerDIV2
        U2max = (128 - Y2Position) / YresPerDIV * VoltsPerDIV2
        
        # print info
        print ("CH1",VoltsPerDIV1,Yunit1+"/DIV")
        print ("CH2",VoltsPerDIV2,Yunit2+"/DIV")
        print ("TIME/DIV: ",TimePerDIVValue,TimeperDIVUnit)
        
        print ("X resolution: ", XresPerDIV)
        print ("Y resolution: ", YresPerDIV)
        print ("Y1 position: ", Y1Position)
        print ("Y2 position: ", Y2Position)

        print ("CH1 : ",U1min, " to ", U1max,"V")
        print ("CH2 : ",U2min, " to ", U2max,"V")
        
        # set self.attributes and return values 
        #(you can use one or the other)
        self.VperDIV1= VoltsPerDIV1
        self.VperDIV2= VoltsPerDIV2
        self.YresPerDIV=YresPerDIV
        self.Yunit1= Yunit1
        self.Yunit2= Yunit2
        self.XresPerDIV=XresPerDIV
        self.Y1Position = Y1Position
        self.Y2Position = Y2Position
        self.Ufactor1=self.UnitfactorV(self.Yunit1)
        self.Ufactor2=self.UnitfactorV(self.Yunit2)
        self.Y1PosReal = Y1Position*self.VperDIV1*self.Ufactor1/self.YresPerDIV
        self.Y2PosReal = Y2Position*self.VperDIV2*self.Ufactor2/self.YresPerDIV
        self.TimePerDIVValue=TimePerDIVValue
        self.Timeunit=TimeperDIVUnit
        self.U1min=-4*self.VperDIV1*self.Ufactor1
        self.U2min=-4*self.VperDIV2*self.Ufactor2
        self.U1max=4*self.VperDIV1*self.Ufactor1
        self.U2max=4*self.VperDIV2*self.Ufactor2
        self.timefactor=self.UnitfactorS(self.Timeunit)
        self.tmax=10*TimePerDIVValue*self.timefactor
        
        # optionnally return values of settings
        return (VoltsPerDIV1, VoltsPerDIV2, Yunit1, Yunit2, TimePerDIVValue,
           TimeperDIVUnit,XresPerDIV,YresPerDIV,Y1Position,Y2Position)
#-----------------------------------------------------------------------
    ## @brief Calculates the multiplier for the voltage based on the unit string.
    def UnitfactorV(self, unit):
        if unit == "V":
            return 1
        elif unit == "mV":
            return 1e-3
        elif unit == "uV":
            return 1e-6
#-----------------------------------------------------------------------
    ## @brief Calculates the multiplier for the time based on the unit string.
    def UnitfactorS(self, unit):
        if unit == "s":
            return 1
        elif unit == "ms":
            return 1e-3
        elif unit == "µs":
            return 1e-6
        elif unit == "ns":
            return 1e-9
#-----------------------------------------------------------------------
    ## @brief Converts raw Y1 values to a voltage.
    #  
    #  @param w raw values to be converted
    #  @return list with the voltage values
    def ConvertY1(self, w):
        Scalefactor=self.VperDIV1*self.Ufactor1/self.YresPerDIV
        v = [float(w_element-128-self.Y1Position)*Scalefactor for w_element in w ]
        return v
#-----------------------------------------------------------------------
    ## @brief Converts raw Y2 values to a voltage.
    #  
    #  @param w raw values to be converted
    #  @return list with the voltage values
    def ConvertY2(self, w):
        Scalefactor=self.VperDIV2*self.Ufactor2/self.YresPerDIV
        v = [float(w_element-128-self.Y2Position)*Scalefactor for w_element in w ]
        return v
#-----------------------------------------------------------------------
    ## @brief Converts raw time values to seconds.
    #  
    #  @return list with the time values
    def get_timevector(self):
        xi=range(0,2048)       
        Scalefactor=self.TimePerDIVValue*self.timefactor/self.XresPerDIV
        t = [float(x_element)*Scalefactor for x_element in xi ]
        return t
#-----------------------------------------------------------------------
#***********************************************************************    
    ## @brief Get the data from channel 1.
    #  
    #  @return t list with the time values
    #  @return v list with the voltage values
    def get_CH1(self):
        print("Acquiring channel 1")
        
        # connect  
        self.Connect()
        self.PrintInfo()
        
        # read settings + waveform
        self.ReadSettings()
        w=self.ReadWaveform(1)
        
        # disconnect
        self.Disconnect()
        
        # generate plot values out of waveform + settings
        v=self.ConvertY1(w)
        t=self.get_timevector()
        return (t,v)
#-----------------------------------------------------------------------
    ## @brief Get the data from channel 2.
    #  
    #  @return t list with the time values
    #  @return v list with the voltage values
    def get_CH2(self):
        print("Acquiring channel 2")
        
        # connect  
        self.Connect()
        self.PrintInfo()
        
        # read settings + waveform
        self.ReadSettings()
        w=self.ReadWaveform(2)
        
        # disconnect
        self.Disconnect()
        
        # generate plot values out of waveform + settings
        v=self.ConvertY2(w)
        t=self.get_timevector()
        return (t,v)
#-----------------------------------------------------------------------
    ## @brief Saves the data of the plot.
    def save(self):
        path = L.savePath("HM1507-3", self.saveDir)
        # save the image
        self.fig1.savefig(path + ".svg")
        # save the data as csv file
        L.saveFigCSV(self.fig1, path)
        # update the file label
        path = L.savePath("HM1507-3", self.saveDir)
        self.filename = path[len(self.saveDir):len(path)]
        self.labelFile.configure(text=self.filename)
#-----------------------------------------------------------------------
    ## @brief Saves the data of the plot and displays the message for CH1
    def save1(self):
        self.save()
        # display the saved message
        self.btnCH1.configure(text="Saved!")
        # schedule message removal
        self.window.after(2000, lambda: self.btnCH1.configure(text="CH1"))
#-----------------------------------------------------------------------
    ## @brief Saves the data of the plot and displays the message for CH2
    def save2(self):
        self.save()
        # display the saved message
        self.btnCH2.configure(text="Saved!")
        # schedule message removal
        self.window.after(2000, lambda: self.btnCH2.configure(text="CH2"))
#-----------------------------------------------------------------------
    ## @brief Saves the data of the plot and displays the message for CH1 and CH2
    def save12(self):
        self.save()
        # display the saved message
        self.btnCH12.configure(text="Saved!")
        # schedule message removal
        self.window.after(2000, lambda: self.btnCH12.configure(text="CH1 + CH2"))
#-----------------------------------------------------------------------
    ## @brief Reads the data for channel 1, plots and saves it.
    #  
    #  @param save specifies whether to save the plot directly
    def plot_CH1(self, save=True):
        if save:
            self.ax1.clear()
            self.ax2.clear()
            self.ax1.get_yaxis().set_visible(True)
            self.ax2.get_yaxis().set_visible(False)
        t,v=self.get_CH1()
        self.ax1.set_xticks(np.multiply([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], self.TimePerDIVValue*self.timefactor))
        self.ax1.set_yticks(np.multiply([-4, -3, -2, -1, 0, 1, 2, 3, 4], self.VperDIV1*self.Ufactor1))
        self.ax1.ticklabel_format(scilimits=(-3, 3))
        self.ax1.grid(True)
        line1dot, = self.ax1.plot(t, np.add(np.multiply(v, 0), self.Y1PosReal), color="blue", linestyle="dotted", linewidth=1)
        line1, = self.ax1.plot(t, np.add(v, self.Y1PosReal), "b")
        self.ax1.set_xlim([0, self.tmax])
        self.ax1.set_ylim([self.U1min, self.U1max])
        self.ax1.set_xlabel("Time (s)")
        self.ax1.set_ylabel("Voltage CH1 (V)")
        self.labelA.configure(text="A:" + L.fstr(self.TimePerDIVValue) + self.Timeunit)
        self.labelY1.configure(text="Y1:" + L.fstr(self.VperDIV1) + self.Yunit1)
        self.canvas1.draw()
        if save:
            self.save1()
#-----------------------------------------------------------------------
    ## @brief Reads the data for channel 2, plots and saves it.
    #  
    #  @param save specifies whether to save the plot directly
    def plot_CH2(self, save=True):
        if save:
            self.ax1.clear()
            self.ax2.clear()
            self.ax1.get_yaxis().set_visible(False)
            self.ax2.get_yaxis().set_visible(True)
        t,v=self.get_CH2()
        self.ax2.set_yticks(np.multiply([-4, -3, -2, -1, 0, 1, 2, 3, 4], self.VperDIV2*self.Ufactor2))
        self.ax1.set_xticks(np.multiply([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], self.TimePerDIVValue*self.timefactor))
        self.ax1.ticklabel_format(scilimits=(-3, 3))
        self.ax1.grid(True)
        self.ax2.grid(True)
        line2dot, = self.ax2.plot(t, np.add(np.multiply(v, 0), self.Y2PosReal), color="red", linestyle="dotted", linewidth=1)
        line2, = self.ax2.plot(t, np.add(v, self.Y2PosReal), "r")
        self.ax2.set_xlim([0, self.tmax])
        self.ax2.set_ylim([self.U2min, self.U2max])
        self.ax2.set_xlabel("Time (s)")
        self.ax2.set_ylabel("Voltage CH2 (V)")
        self.labelA.configure(text="A:" + L.fstr(self.TimePerDIVValue) + self.Timeunit)
        self.labelY2.configure(text="Y2:" + L.fstr(self.VperDIV2) + self.Yunit2)
        self.canvas1.draw()
        if save:
            self.save2()
#-----------------------------------------------------------------------
    ## @brief Reads the data for channel 1 and 2, plots and saves it.
    def plot_dual(self):
        self.ax1.clear()
        self.ax2.clear()
        self.ax1.get_yaxis().set_visible(True)
        self.ax2.get_yaxis().set_visible(True)
        self.plot_CH1(save=False)
        self.plot_CH2(save=False)
        self.save12()
#-----------------------------------------------------------------------
    ## @brief Selects the directory to save the plots and data to.
    def selectDir(self):
        newDir = filedialog.askdirectory(initialdir=self.saveDir, title="Select a directory")
        if newDir == "":
            return
        self.saveDir = newDir + "/"
        self.labelPath.configure(text="Current save directory: " + self.saveDir)
#***********************************************************************

## @brief Main function to execute the program
if __name__ == "__main__":
    gui = HM1507_3GUI()