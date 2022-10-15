import os 

class CarverBase():
    def __init__(self, dir) -> None:
        self.dir = dir
        self.signatures = []

    def _addSignature(self, name, header, footer):
        self.signatures.append((name, bytearray.fromhex(header), bytearray.fromhex(footer)))

    def _setDir(self, dir):
        fullPath = os.path.join(self.dir, dir)
        if(not os.path.isdir(fullPath)):
            os.mkdir(fullPath)
        self.dir = fullPath

    def carve(self, data):
        _start = 0
        _data = bytearray(data)
        count = 0
        
            # Problem is here, that break condition does not hit reliably
            # There is also some problem with the end signature 
            # Apparently the end signature is in some case before the start signature
            # This should be a fragmentation problem of the specific file system
            # We need to enhance the file carver to understand file systems and restore
            # the files from these infos
        for sig in self.signatures:
            
            print("")
            print("--> Carving for: " + sig[0])
            print("")

            while True:

                start = _data.find(sig[1], _start)
                end   = _data.find(sig[2], _start+len(sig[1]))

                if(start == -1 or end < start):
                    break
                elif(start > 0 and end > 0):
                    count += 1
                    print("------> " + sig[0] + " detected! - Start Hex: " + str(hex(start)) + " - End Hex: " + str(hex(end)) + " - Nr: " + str(count))
                    
                    img = bytearray()
                    for i in range(start, end+len(sig[2]), 1):
                        img.append(data[i])

                    file = open(os.path.join(self.dir, str(count) + "-" + str(hex(start)) + sig[0]), "wb")
                    file.write(img)
                    _start = end + len(sig[2])