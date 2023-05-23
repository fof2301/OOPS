from cards import *
from art import *
from games import blackjack
import json

#run the casino 
wallet=50
games=["TEEN PATTI", "BLACKJACK"]
def available_Games():
    counter=1
    for x in games:
        print(f"{counter}.{x}")
        counter+=1
tprint("Welcome")
while(wallet>0):
    print("1.PLAY")
    print("2.EXIT")
    print("3.WALLET")
    play=(input("? \n"))
    if play=="2":
        break
    elif play=="3":
        print(wallet)
        continue
    else:
        pass
    print("WHAT WOULD YOU LIKE TO PLAY")
    available_Games()
    game=int(input())
    if game==2:
        wallet=wallet-blackjack()
        continue
print("GO AWAY PEASENT")        
        
