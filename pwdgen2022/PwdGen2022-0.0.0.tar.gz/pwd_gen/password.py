import random

chars = 'abcdefghijklmn0pqrstuvwxyz'
upper_chars = chars.upper()
special_chars ='#@'


def createPwd(char_length, include_special = False, include_upper = False):
    password = []
    for i in range(char_length):
        
        if include_special:
            password.append(random.choice(special_chars))
            include_special = False
        elif include_upper:
            password.append(random.choice(upper_chars))
            include_upper = False
        else:
            password.append(random.choice(chars))
            
    print(f"your password is: {''.join(password)}")

  

  