from cards import *
from art import *
import time
#run the casino 
wallet=50
def blackjack():
    total=0
    tprint("BLACKJACK")
    ready=input("READY?")
    print("dosnt matter we start")
    time.sleep(3)
    card1= cards()
    print_card(card1.suite,card1.number,card1.suite)
    total=total+card1.number
    print("HAHAHAhahhaaaaaaa.......")
    time.sleep(3)
    card2= cards()
    print_card(card2.suite,card2.number,card2.suite)
    total=total+card2.number
    print("HAHAHAhahhaaaaaaa.......")
    if total>21:
        print("YOU LOST")
        print("-10 from wallet")
        return 10
    elif total==21:
        print("YOU won HAHAHA")
        return -20
    else:
        pass
    time.sleep(3)
    card3=cards()
    print_card(card3.suite,card3.number,card3.suite)
    total=total+card3.number
    print("HAHAHAhahhaaaaaaa.......")
    if total>21:
        print("YOU LOST")
        print("-10 from wallet")
        return 10
    elif total==21:
        print("YOU won HAHAHA")
        return -20
    else:
        pass
    time.sleep(3)
    card4=cards()
    print_card(card4.suite,card4.number,card4.suite)
    total=total+card4.number
    print("HAHAHAhahhaaaaaaa.......")
    if total>21:
        print("YOU LOST")
        print("-10 from wallet")
        return 10
    elif total==21:
        print("YOU won HAHAHA")
        return -20
    else:
        pass
    time.sleep(3)
    card5=cards()
    print_card(card5.suite,card5.number,card5.suite)
    total=total+card5.number
    print("HAHAHAhahhaaaaaaa.......")
    if total>21:
        print("YOU LOST")
        print("-10 from wallet")
        return 10
    elif total==21:
        print("YOU won HAHAHA")
        return -20
    else:
        pass
    card6=cards()
    print_card(card6.suite,card6.number,card6.suite)
    total=total+card6.number
    print("HAHAHAhahhaaaaaaa.......")
    if total>21:
        print("YOU LOST")
        print("-10 from wallet")
        return 10
    elif total==21:
        print("YOU won HAHAHA")
        return -20
    else:
        pass
    

games=["TEEN PATTI", "BLACKJACK"]
def available_Games():
    counter=1
    for x in games:
        print(f"{counter}.{x}")
        counter+=1
tprint("Welcome")
while(True):
    print("1.PLAY")
    print("2.EXIT")
    print("3.WALLET")
    play=int(input("? \n"))
    if play==2:
        break
    elif play==3:
        print(wallet)
        continue
    else:
        pass
    print("WHAT WOULD YOU LIKE TO PLAY")
    available_Games()
    game=int(input())
    if game==2:
        wallet=wallet-blackjack()
        
