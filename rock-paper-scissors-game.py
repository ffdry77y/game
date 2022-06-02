# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 21:44:05 2022

@author: sepideiu
"""

Rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
import random
print("welcome to the Rock, Paper, Scissors land")
game=[Rock,Scissors,Paper]
user=input("choose your move, rock, scissors or paper? \n")
if user=="rock":
    print(Rock)
elif user=="paper":
    print(Paper)
else:
    print(Scissors)
cp=random.randint(0,2)
print(f"computer choice {game[cp]}")
if user=="rock":
    if game[cp]== Scissors:
        print("you win")
    else:
        print("you lost")
elif user=="scissors":
    if game[cp]==Paper:
        print("you win")
    else:
        print("you lost")
else:
    if game[cp]==Rock:
        print("you win")
    else:
        print("you lost")
