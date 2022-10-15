import sys
import fish_collector
import re

CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext

def main(species_name):
    if species_name:
        #Print information about selected species
        sel_fish_param = ""
        for fish in fish_collector.getSpeciesList():
            if fish["name"] == species_name[0]:
                sel_fish_param = fish["path"]

    
        if sel_fish_param == "":
            print("Species Not found")
            sys.exit()
        
        inform = fish_collector.getInformSelectSpecies(sel_fish_param)
        print(len(inform[0]))
        for elem in inform[0]:
            if elem != "Image Gallery":
                print(elem+"="+str(cleanhtml(str(inform[0][elem]))))
    else:
        #Print species list
        for fish in fish_collector.getSpeciesList():
            print(fish["name"])


if __name__ == "__main__":
    main(sys.argv[1:])
