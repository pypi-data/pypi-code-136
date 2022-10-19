#!/usr/bin/python

"""Split a large CSV file into chunks, 
each with their own copy of the header."""

import csv
import sys

def splitCSV( filename , rowcount=100000 ):

    # Header data must be retained for the whole script.
    header = []

    with open(filename , "r" , newline='') as headerfile:
        headerReader = csv.reader(headerfile)
        header = next(headerReader)
        #print(header)

    with open(filename , "r" , newline='') as bigFile:
        looper = csv.reader(bigFile)

        count = 0
        filenamecount = 1
        tmprows = []
        for row in looper:
            if row != header:
                tmprows.append(row)
                count = count + 1
                if count == rowcount:
                    #print(count)
                    tmpfilename = filename[:-4] + str(filenamecount) + ".csv"
                    with open(tmpfilename, 'w', newline='') as tmpcsv:
                        wrtr = csv.writer(tmpcsv)
                        wrtr.writerow(header)
                        wrtr.writerows(tmprows)
                    tmprows = []
                    count = 0
                    filenamecount = filenamecount + 1
        # Clean up remaining rows into a final file.
        tmpfilename = filename[:-4] + str(filenamecount) + ".csv"
        with open(tmpfilename , "w", newline='') as tmpcsv:
            wrtr = csv.writer(tmpcsv)
            wrtr.writerow(header)
            wrtr.writerows(tmprows)

if __name__ == "__main__":
    if sys.argv[1]:
        if sys.argv[2]:
            splitCSV(sys.argv[1], int(sys.argv[2]))
        else:
            print("Usage: python3 splitCSV.py filename 'numberOfRowsPerFile'")
    else:
        print("Usage: python3 splitCSV.py filename 'numberOfRowsPerFile'")