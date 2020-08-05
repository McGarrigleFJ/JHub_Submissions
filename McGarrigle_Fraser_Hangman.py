words=open('word_list.txt')
wordlist=words.read().split('\n')
wordlist.pop() #The final item in the list is just a 'return', so I'll pop this off to leave just words.
from random import randint
def rand(): #Generates a random number between 0 and the length of the list
    
    return randint(0,len(wordlist))  

def new_word(): #Picks a random word from the list
    
    word=wordlist[rand()].lower() 
    return word

def return_stars(letters): #displays a series of stars of same length as word
    return '*'*len(letters)

import string
alphabet=string.ascii_lowercase #Imports object of all lower case letters for validity checking of user input

from IPython.display import clear_output #Helps keep the screen clean

def take_a_guess(): #Function that actually runs the game 
    
    solved=False  

    clear_output #Set up initial values, generate word and displays stars to the user
    word=new_word()
    letters=list(word)
    print(return_stars(letters))
    curr_list=list(return_stars(letters))
    lives=7    
    already_guessed=[]   
    choice_valid=False    
    
    while choice_valid==False and lives!=0: #The first loop checks if the users guess is valid; i.e if they're taking legitimate guesses or typing nonsense
        
        choice=input('Please enter your next guess: ').lower()
        
        if len(choice)>1: 
            clear_output()
            print('Pick only one letter')
            print(return_stars(letters))
            choice_valid=False
        
        elif choice not in alphabet:
            clear_output()
            print('Please pick a letter')
            print(return_stars(letters))
            choice_valid=False
        
        elif len(choice)==1 and choice.lower() in alphabet:
            choice_valid=True
        
        while choice_valid==True and solved==False: #If user choice is actually a letter
            if choice in letters and choice not in already_guessed: #If their guess is correct
            
                clear_output()       
                already_guessed.append(choice)                      #Adds guess to list of already guessed letters
                counter=-1                                          #Set up counter 
                correct=[]
            
                print(f'Yes! {choice} is a letter. You have {lives} lives remaining.\n\nLetters youve guessed are: {already_guessed}\n')
                for let in letters:                                 #For each letter in the word
                    counter+=1
                    if let==choice:                                 #If the letter matches the guess
                        correct.append(counter)                     #Generates a list of indexes of the correct letters (correct). Eg, for 'a' in 'alphabet', correct = [0,4]
                
                for index in correct:
                    curr_list[index]=choice                         #replaces star with correct guess in correct location. Again for 'alphabet' this leads to [a,*,*,*,a,*,*,*]
                soln=''                                             #Empty string to work with
                for let in curr_list:                               #Each character in NEW current list (i.e with correct guess)
                    soln+=let                                       #Add character to empty string and print. Because only exists in this nested loop, it's re-generated each time
                print(soln)                
        
                if '*' in curr_list:                                #Checks if word has been solved
                    solved=False
                else:                                               #Checks if word has been solved
                    solved=True
                choice_valid=False
        
            elif choice in already_guessed:                         #Makes sure the user doesn't waste a life on something they've already guessed
                clear_output()
                print(f'Sorry youve already guessed {choice}. Pick again.\n\nLetters youve guessed are: {already_guessed}\n')
                soln=''
                for let in curr_list:                               #Same function as line 70-73 
                    soln+=let
                print(soln)
                choice_valid=False
            
            elif choice not in letters and lives>=1:                #Loop for an incorrect choice
                lives-=1
                clear_output()
                already_guessed.append(choice)
                print(f'Unlucky, "{choice}" isnt in the word, you have {lives} lives remaining.\n\nLetters youve guessed are: {already_guessed}\n')
                soln=''                                             #Same function as line 70-73 
                for let in curr_list:
                    soln+=let
                print(soln)
                choice_valid=False
            
        if solved==False and lives==0:                              #When user looses the game 
            print(f"\nYou're out of lives! Unlucky. The word was {word}.\n You lose")    
            break
    
        if solved==True:                                            #When user wins the game 
            print(f'\nWell done! The word was "{word}" and you had {lives} lives remaining.\nCongratulations you win')  
            break
take_a_guess()                                                      #Actually run the game 
