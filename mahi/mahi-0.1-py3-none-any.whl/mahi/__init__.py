import random
import math

def guess():
    print("Welcome to Mahi's Number guessing Game")
    l=int(input("Enter the Lower Number: "))
    h=int(input("Enter the Higher Number: "))
    x = random.randint(l,h)
    print("\n\tYou've only ",round(math.log(h-l+1,2)),"chances to guess the number\n")
    count=0
    while count<math.log(h-l+1,2):
        count+=1
        g=int(input("Guess a number: "))
        if x==g:
            print("Congratulations you did it in ",count," number of tries")
            break
        elif x>g:
            print("Your Guess is small, try bigger one")
        elif x<g:
            print("Your Guess is high, try smaller one")
    if count>=math.log(h-l+1,2):
        print("The Number is %d" % x)
        print("Sorry U have reached maximum attempts,Bettre Luck Next Time....!")