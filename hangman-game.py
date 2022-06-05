# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 16:28:57 2022

@author: sepideiu
"""

# 
"""
Created on Sun Jun  5 16:23:32 2022

@author: sepideiu
"""

import random
logo='''
_                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       '''
hangman= ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


print(logo)
print("Welcome to tha hangman game of animals")

word_list=['ant', 'baboon' ,'badger', 'bat', 'bear' ,'beaver' ,'camel' ,'cat' ,'clam' ,'cobra', 'cougar'
       'coyote', 'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat', 'goose', 'hawk',
       'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose', 'mouse', 'mule', 'newt', 'otter', 'owl', 'panda',
       'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat', 'raven', 'rhino', 'salmon', 'seal', 'shark', 'sheep',
       'skunk', 'sloth', 'snake', 'spider', 'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle',
       'weasel', 'whale', 'wolf', 'wombat', 'zebra', 'goldfish', 'ardvark', 'elephant']
chosen_word= random.choice(word_list)
display=[]
for i in range(len(chosen_word)):
    display+="_"
print(f"{' '.join(display)}")
end_of_game = False
lives=7
han=0

while not end_of_game:
    guess= input("guess a letter ").lower()
    for i in range(0,len(chosen_word)):
        if chosen_word[i] == guess:
            display[i]= guess
    print(f"{' '.join(display)}")
    if guess not in display:
        lives=lives-1
        print(hangman[han])
        han+=1
       
    
    if "_" not in display:
        end_of_game=True
        print("you win")
    if lives==0:
        end_of_game = True
        print("you lose")
        print(f"the answer was {chosen_word}")
