import time

def play():
    print("Let's have some fun...\n")
    print('We will be going to see some alphabetical pattern here.\n')
    time.sleep(1.5)
    b = True
    t = 0
    while b:
        if t==0:
            in_msg = 'Choose any letter between a and z: '
        else:
            in_msg = "That's not an alphabet. Choose again: "

        try:
            t+=1
            ch = input(in_msg)
            asc_no = ord(ch)
            if asc_no in range(97,97+27) or asc_no in range(65,65+27):
                if asc_no>=97:
                    if ch=='a':
                        ch='b'
                else:
                    if ch=='A':
                        ch='B'

                print('\nPattern is loading. Please wait.',end='')

                for t in range(5):
                    time.sleep(0.6)
                    print('.', end='', flush=True)
                print('\n\n')

                alpha_pattern(ch,' ')

                uc = input("\n\nIf you want to play it again, press any numeric ky, else press any other key: ")
                if uc in [str(k) for k in range(10)]:
                    b = True
                    t = 0
                    print('\nOnce again,', end=' ')
                else:
                    b = False
                    print('\nEnd of the game. Good bye!!\n')

            else:
                raise ValueError('')
        except ValueError as ex:
            b = True
            pass
        except:
            b = True
           
def alpha_pattern(ch,smb):
    asc_no = ord(ch)
    if asc_no>=97:
        n = asc_no - 97+1
        alph_dict = {c: chr(97+c) for c in range(26)}
    else:
        n = asc_no - 65+1
        alph_dict = {c: chr(65+c) for c in range(26)}

    mid = (n-1)*2
    rlen = mid*2+1       
    pattern=[]

    for r in range(1,n+1):
        rpatt = []
        for ci in range(1,r+1):
            rpatt.append(alph_dict.get(n-ci))
        rpatt.extend(list(reversed(rpatt[:-1])))
        pattern.append(smb.join(rpatt).center(rlen,' '))

    pattern.extend(list(reversed(pattern[:-1])))

    for p in pattern:
        time.sleep(0.5)
        print(p)
    time.sleep(0.75)    

    return None  


