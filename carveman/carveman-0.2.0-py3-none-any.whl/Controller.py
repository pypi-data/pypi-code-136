import os
import time

from datetime import datetime

class Controller():
    def __init__(self) -> None:
        self.startTime = time.time()

    def printHeader(self, path, outdir, hash):
        print("###########################################################################################")
        print("")
        print("Carveman by 5f0")
        print("File carving for pictures, documents and other files based on it's file signatures")
        print("")
        print("Current working directory: " + os.getcwd())
        print("        Investigated file: " + path)
        print("")
        print("                      MD5: " + hash.md5)
        print("                   SHA256: " + hash.sha256)
        print("")
        print("     Path to carved files: " + outdir)
        print("")
        print(" Datetime: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print("")
        print("###########################################################################################")

    def printExecutionTime(self):
        end = time.time()
        print("")
        print("###########################################################################################")
        print("")
        print("Execution Time: " + str(end-self.startTime)[0:8] + " sec")
        print("")