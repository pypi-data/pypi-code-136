custom_chars = {
    "heart":     [ 0,  0, 10, 31, 31, 14,  4,  0],
    "smile":     [ 0, 10, 10,  0, 17, 14,  0,  0],
    "dog_left":  [ 0,  0, 12, 12,  7,  4,  4,  0],
    "dog_right": [ 0,  0,  0,  6, 24,  8,  8,  0],
    "half_moon": [ 6, 12, 24, 24, 24, 28, 15,  6],
    "bell":      [ 0,  4, 14, 14, 14, 31,  0,  4],
    "note":      [ 0,  2,  3,  2, 14, 30, 12,  0],
    "duck":      [ 0,  0, 12, 29, 15, 15,  6,  0],
}

default_custom_chars = {
    "á":         [2, 4, 0, 14, 1, 15, 17, 15],
    "é":         [2, 4, 0, 14, 17, 31, 16, 14],
    "í":         [2, 4, 0, 4, 12, 4, 4, 14],
    "ó":         [2, 4, 0, 14, 17, 17, 17, 14],
    "ú":         [2, 4, 0, 17, 17, 17, 19, 13],
    "heart":     [ 0,  0, 10, 31, 31, 14,  4,  0],
    "smile":     [ 0, 10, 10,  0, 17, 14,  0,  0],
    "half_moon": [ 6, 12, 24, 24, 24, 28, 15,  6],
}

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

replazable_chars = [
    '¥→←αäβεμσρ√𝑖₵ñöθΩüΣπx̄÷█'
]
