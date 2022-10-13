import os as _os
import pickle as _pickle

file = open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "MorseCode.bytes") , "rb")
MorseCode = _pickle.load(file)
file.close()

def encode(message: str) -> str:
    global MorseCode
    EncryptedPassword = ""
    for text in message:
        if text == " ":
            EncryptedPassword += "/"
            continue
        EncryptedPassword += MorseCode[text]
        EncryptedPassword += " "
    return EncryptedPassword
def decode(message: str) -> str:
    global MorseCode
    DecryptPassword = ""
    MorseCodeLinker = ""
    Decoder = dict((v,k) for k,v in MorseCode.items())
    for text in message:
        if text == "/":
            DecryptPassword += " "
            continue
        if text != " ":
            MorseCodeLinker += text
        else:
            if MorseCodeLinker == "": continue
            DecryptPassword += Decoder[MorseCodeLinker]
            MorseCodeLinker = ""
    return DecryptPassword

