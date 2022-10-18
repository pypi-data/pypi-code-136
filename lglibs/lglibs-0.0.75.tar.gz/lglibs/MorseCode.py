MorseCode = { 
    'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}

def encode(message: str) -> str:
    global MorseCode
    EncryptedPassword = ""
    for text in message.upper():
        if text == " ":
            EncryptedPassword += "\\"
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
        if text == "\\":
            DecryptPassword += " "
            continue
        if text != " ":
            MorseCodeLinker += text
        else:
            if MorseCodeLinker == "": continue
            DecryptPassword += Decoder[MorseCodeLinker]
            MorseCodeLinker = ""
    return DecryptPassword.lower()

