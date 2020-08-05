words=open('word_list.txt')
wordlist=words.read().split('\n')
wordlist.pop() #The final item in the list is just a 'return', so I'll pop this off to leave just words.
from random import randint
def rand():
    
    return randint(0,len(wordlist))

def new_word():
    
    word=wordlist[rand()].lower()
    return word

def return_stars(letters):
    return '*'*len(letters)

import string
alphabet=string.ascii_lowercase

from IPython.display import clear_output

def take_a_guess():
    
    solved=False  

    clear_output
    word=new_word()
    letters=list(word)
    print(return_stars(letters))
    curr_list=list(return_stars(letters))
    lives=7    
    already_guessed=[]   
    choice_valid=False    
    
    while choice_valid==False and lives!=0:
        
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
        
        while choice_valid==True and solved==False:
            if choice in letters and choice not in already_guessed:
            
                clear_output()       
                already_guessed.append(choice)
                counter=-1
                correct=[]
            
                print(f'Yes! {choice} is a letter. You have {lives} lives remaining.\n\nLetters youve guessed are: {already_guessed}\n')
                for let in letters:
                    counter+=1
                    if let==choice:
                        correct.append(counter)      
                
                for index in correct:
                    curr_list[index]=choice
                soln=''
                for let in curr_list:
                    soln+=let
                print(soln)                
        
                if '*' in curr_list:
                    solved=False
                else:
                    solved=True
                choice_valid=False
        
            elif choice in already_guessed:
                clear_output()
                print(f'Sorry youve already guessed {choice}. Pick again.\n\nLetters youve guessed are: {already_guessed}\n')
                soln=''
                for let in curr_list:
                    soln+=let
                print(soln)
                choice_valid=False
            
            elif choice not in letters and lives>=1:
                lives-=1
                clear_output()
                already_guessed.append(choice)
                print(f'Unlucky, "{choice}" isnt in the word, you have {lives} lives remaining.\n\nLetters youve guessed are: {already_guessed}\n')
                soln=''
                for let in curr_list:
                    soln+=let
                print(soln)
                choice_valid=False
            
        if solved==False and lives==0:
            print(f"\nYou're out of lives! Unlucky. The word was {word}.\n You lose")    
            break
    
        if solved==True:
            print(f'\nWell done! The word was "{word}" and you had {lives} lives remaining.\nCongratulations you win')  
            break
take_a_guess()
