from cnvrtr.Converter import Converter

class ByteInterpreter():
    def __init__(self, bytes, config) -> None:
        self._bytes = bytes
        self._config = config
        self._cnvrtr = Converter()

    def interpret(self):
        result = []
        for c in self._config:
            b = bytearray()
            amount = c["end"] - c["start"] + 1
            subBytes = [self._bytes[i:i + amount] for i in range(c["start"], c["end"]+1, amount)][0]
            b.extend(subBytes)
            if(c.get("action") != None):
                actionResult = self.__getActionResult(c["action"], b)
                result.append((c["name"], c["description"], c["action"]["type"], b, actionResult))
            else:
                actionResult = ""
                result.append((c["name"], c["description"], "None", b, actionResult)) 
        return result

    def __getActionResult(self, action, b):
        result = ""
        type_ = action["type"]
        if(type_ == "amount"):
            endianess = action["endianess"]
            if(endianess == "big"):
                result = self._cnvrtr.hexToDec(b.hex())
            elif(endianess == "little"):
                result = self.__hexToLittleEndianToDec(b)
        elif(type_ == "ascii"):
            result = self._cnvrtr.hexToAsciiString(b.hex())
        elif(type_ == "equals"):
            result = action["noMatch"]
            for i in range(0, len(action["cmp"])):
                if(b.hex() == action["cmp"][i]["value"].lower()):
                    result = action["cmp"][i]["description"]
        return result

    def __hexToLittleEndianToDec(self, byteArr):
        le = self._cnvrtr.toLittleEndian(byteArr.hex(" "))
        return str(self._cnvrtr.hexToDec(le))