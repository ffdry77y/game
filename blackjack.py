# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 15:34:48 2022

@author: MyPc
"""
logo="""
                                                                                   
88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"                                 
"""


def BlackJack():
    
    import random
   
    def one():
        if 11 in user_card and sum(user_card)>21:
            user_card.remove(11)
            user_card.append(1)
    def add(x):
        one()
        summ=0
        for i in range(0,len(x)):
            summ+=x[i]
    
            return summ

    def loseruser(x):
        if add(x)>21:
            print(f"Dealer Wins{cp_card}")
        
    def losercp(x):
        if add(x)>21:
            print("You Win")


#--------------------------------
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    user_card=[]
    cp_card=[]
    ending=False
    for i in range(0,2):
        user_card.append(cards[random.randint(0,12)])
        cp_card.append(cards[random.randint(0,12)])
    if add(user_card)==21:
        print("BlackJack")
        ending==True
    
    print(f"your carts are: {user_card}\n the dealer first cart is: {cp_card[0]}" )
    
    cp_add= cp_card[0]+cp_card[1]
#------------------------
    while cp_add<17:
        cp_add+=cards[random.randint(0,12)]

    loseruser(user_card)


#-------------------
    while  ending==False:
        hit=input("do you wish to hit? type 'y' or 'n'")
        if hit=="y":
            user_card.append(cards[random.randint(0,12)])
            print(user_card)
            if add(user_card)>21:
                print(f"Dealer Wins {cp_card}")
                ending=True
            
        else:
            if add(user_card)>21 or add(cp_card)>21:
                    losercp(cp_card)
                    loseruser(user_card)
                    ending=True
            elif add(user_card)>add(cp_card):
                    ending=True
                    print("You Win")
            elif add(cp_card)>add(user_card):
                    print(f"Dealer Wins {cp_card}")
                    ending=True
            else:
                    print("equal")
                    ending=True
#------------------------
#------------------------
while input("Do you want to play BlackJack?(type'y' or'n')")=="y":
    print("\x1B[2J")
    print(logo)
    BlackJack()
