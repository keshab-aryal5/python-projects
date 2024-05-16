import random
import os
from logo import stages
from word import sabdha

word = random.choice(sabdha)
list_of_word=[x.upper() for x in word]
blank_list = ['_' for x in word]
guessed_list = []
lives = 6

def clear_screen():
    os.system('cls')

clear_screen() 
print("Welcome to hangman Game".center(100),"\n\n")
print("You will have 6 chances to guess the correct word. All the best.👍".center(100),"\n")

def print_info():
    global lives
    print("Guessed letter: ",end="")
    for x in guessed_list:
        print(x, end=" ")
    
    print("\n\n")
    
   
while lives!=0 and ('_' in blank_list):
    print(stages[lives].center(50))
    print_info()
    for x in blank_list:
        print(x,end="  ")    
    

    #Asking the user to guess a word
    guessed_letter = input("\n\nGuess a letter: ").upper()
    
    #checking if the word was already guessed
    if guessed_letter in guessed_list:
        print(f"You have already guessed this letter {guessed_letter}. You loose a life")
        lives-=1

        
    #checking if the guessed word is correct.
    elif guessed_letter in list_of_word:
        print("Great you guessed it correct.")
        while guessed_letter in list_of_word:
            index = list_of_word.index(guessed_letter)
            blank_list[index]=guessed_letter
            list_of_word[index]="*"
            
        guessed_list.append(guessed_letter)

         
    #handaling the incorrectly guessed letter   
    else:
        print("Sorry you guessed it wrong. You loose a life.")
        guessed_list.append(guessed_letter)
        lives-=1

        
    clear_screen()
    
    
if lives!=0:
    print("\nHurreh You won the game.")
    for x in blank_list:
        print(x,end=" ")   
    
    print(stages[lives])
    
else:   
    print("Oh no, you lost the game. Better try next time. \nThe word was: ")
    for x in word:
        print(x.upper(),end=" ")
    
    print(stages[lives])