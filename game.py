# Create your Game class logic in here.
from phrase import Phrase
import random



class Game:
    
    def __init__(self):
        self.incorrect = 0
        self.list_of_phrases = [Phrase('Is the juice worth the squeeze'), Phrase('Green Lights'), Phrase('An Arm and a Leg'), Phrase('Dime a Dozen'), Phrase('Down to the Wire')]
        self.active_phrase = self.get_random_phrase
        self.past_guesses = ['a']
       
        
        
    def start_game(self):
        self.welcome()
        self.get_guess()
    
    def get_random_phrase(self):
        sel_phrase = random.choice(self.list_of_phrases)
        return sel_phrase
    
    def welcome(self):
        GREETING = "======> Welcome to Phrase Hunter <====="
        print(GREETING.upper())
        rules = print("\nRules: \n******Try and guesses the phrase! Select a letter on a time, if you can't solve it before your 5 guess up you lose. Good luck!.******\n\n")
    
    def get_guess(self):
        #while Phrase.check_complete == False:
            try:
                guess = input('Please enter a letter:  ')
                
                if len(guess) <2 and len(guess)>0:
                    if guess.isalpha():                         
                        if guess in self.past_guesses:
                            print('Whoops, looks like you guessed that already')
                            #self.guesses = 
                        elif Phrase.check_letter(self.active_phrase) == False:
                            print('boom')
                            self.past_guesses.append(guess)
                            print('Letter not in phrase. Please try again!')
                            self.guesses += 1
                        else:
                            pass
                    else:
                        print('Sorry Letters Only!')
                else:
                    raise ValueError
        
            except ValueError as err:
                print("\nInvalid input. Please enter one letter at a time")
            
         
            
    
    def game_over(self):
        pass
    

