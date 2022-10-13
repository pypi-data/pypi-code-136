# import libraries
import csv  
import pathlib

def program():
    # check if file exists
    try:
        print("EasyVcf 1.0 by DoguMer")
        filename = input("Enter csv file name(with .csv extension): ")
        fileextension = pathlib.Path(filename).suffix
        file = open(filename, 'r')
    except:
        if fileextension != ".csv":
            print("Invalid file type (Use .csv files)!")
            quit()
        else:
            print("Error: File not found")
            quit()

    data = list(csv.reader(file, delimiter=","))
    file.close()

    # user inputs for column numbers
    namecol = int(input("Enter name column: ")) - 1
    telcol = int(input("Enter tel number column: ")) - 1
    emailcol = int(input("Enter E-Mail column: ")) - 1
    eventname = input("Enter event name(starting word): ")
    vcffilename = input("Enter .vcf file name(without .csv at the end): ") + ".vcf"

    # write from csv to vcf in vcf format
    try:
        for row in data:
            if row[0] != "isim":
                start = "BEGIN:VCARD" + '\n'
                fn = "FN:" + eventname + " " + row[namecol] + '\n'
                if row[telcol][0] != "0":
                    row[telcol] = "0" + row[telcol] # corrects numbers which not starting with 0
                tel = "TEL;TYPE#WORK,VOICE:" + row[telcol] + '\n'
                email = "EMAIL:" + row[emailcol] + '\n'
                end = "END:VCARD" + '\n' + '\n'

                vcffile = open(vcffilename, "a")
                vcffile.write(start+fn+tel+email+end)
                vcffile.close()
    except:
        print("Error: Invalid column number!")
        quit()

    # final message
    print("Contacts exported to " + vcffilename + " !")
