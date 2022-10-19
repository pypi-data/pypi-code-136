from typing import Union

class CustomChar():
    def __init__(self, char: list[int], aliases: Union[list[str], str]) -> None:
        self.char = char
        if isinstance(aliases, str):
            self.aliases = [aliases]
        else:
            self.aliases = aliases

other_custom_chars = {
    CustomChar([ 0,  0, 10, 31, 31, 14,  4,  0], "heart"),
    CustomChar([ 0, 10, 10,  0, 17, 14,  0,  0], "smile"),
    CustomChar([ 0,  0, 12, 12,  7,  4,  4,  0], "dog_left"),
    CustomChar([ 0,  0,  0,  6, 24,  8,  8,  0], "dog_right"),
    CustomChar([ 6, 12, 24, 24, 24, 28, 15,  6], "half_moon"),
    CustomChar([ 0,  4, 14, 14, 14, 31,  0,  4], "bell"),
    CustomChar([ 0,  2,  3,  2, 14, 30, 12,  0], "note"),
    CustomChar([ 0,  0, 12, 29, 15, 15,  6,  0], "duck"),
}

default_custom_chars: list[CustomChar] = [
    CustomChar([2, 4, 0, 14, 1, 15, 17, 15], "á"),
    CustomChar([2, 4, 0, 14, 17, 31, 16, 14], "é"),
    CustomChar([2, 4, 0, 4, 12, 4, 4, 14], "í"),
    CustomChar([2, 4, 0, 14, 17, 17, 17, 14], "ó"),
    CustomChar([2, 4, 0, 17, 17, 17, 19, 13], "ú"),
    CustomChar([ 0,  0, 10, 31, 31, 14,  4,  0], ["heart", "♥️", "❤️"]),
    CustomChar([ 0, 10, 10,  0, 17, 14,  0,  0], ["smile", "😀", "😁","😄","😃","☺️","🙂","🤗", "😊"]),
    CustomChar([ 6, 12, 24, 24, 24, 28, 15,  6], ["half_moon", "🌙", "🌜", "🌛", "🌘", "🌖"]),
]

available_chars_ROM_A00 = [
    '                ',  # 00. Custom chars loaded to rom, displayed twice in a row
    '                ',  # 01. empty
    ' !"#$%&\'()*+,-./', # 02. 
    '0123456789:;<>=?',  # 03. 
    '@ABCDEFGHIJKLMNO',  # 04. 
    'PQRSTUVWXYZ[¥]^_',  # 05. 
    '`abcdefghijklmno',  # 06. 
    'pqrstuvwxyz{|}→←',  # 07. 
    '                ',  # 08. empty
    '                ',  # 09. empty
    '????????????????',  # 10. non latin characters
    '????????????????',  # 11. non latin characters
    '????????????????',  # 12. non latin characters
    '????????????????',  # 13. non latin characters
    'αäβεμσρ?√?𝑖?₵?ñö',  # 14. 
    'pqθ?ΩüΣπx̄????÷ █',  # 15. 
]

available_chars_ROM_A00: str = ''.join(available_chars_ROM_A00)

replaceable_chars = '¥→←αäβεμσρ√𝑖₵ñöθΩüΣπx̄÷█'
