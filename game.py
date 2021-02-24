# Create your Game class logic in here.
from phrase import Phrase
import random



class Game:
    
    def __init__(self):
        self.incorrect = 0
        self.list_of_phrases = [('Is the juice worth the squeeze'), ('Green Lights'), ('An Arm and a Leg'), ('Dime a Dozen'), ('Down to the Wire')]
        self.active_phrase = random.choice(self.list_of_phrases)
        self.past_guesses = []
        
    
    def welcome(self):
        GREETING = "======> Welcome to Phrase Hunter <====="
        print(GREETING.upper())
        rules = print("\nRules: \n******Try and guesses the phrase! Select a letter on a time, if you can't solve it before your 5 guess up you lose. Good luck!.******\n\n")
        
    
    def get_random_phrase(self):
        print(Phrase.display(self,self.active_phrase))
    
    def get_guess(self):
        
        
        while self.incorrect < 5:
            guess = input('Please enter a letter:  ')
            
            try:

                if len(guess) <2 and len(guess)>0:
                    if guess.isalpha():                         
                        if guess in self.past_guesses:
                            print('Whoops, looks like you guessed that already')
                        
                        elif Phrase.check_letter(self,guess) == False:
                            self.past_guesses.append(guess)
                            print('Sorry, that letter is not in phrase. Please try again!')
                            self.incorrect += 1
                            print(self.past_guesses)
                            
                        else:
                            if guess in self.active_phrase:
                                pass
                                
                            
                    else:
                        print('Sorry Letters Only!')
                else:
                    raise ValueError
        
            except ValueError as err:
                print("\nInvalid input. Please enter one letter at a time")
    
    
    def start_game(self):
        self.welcome()
        self.get_random_phrase()
        
        self.get_guess()
    
    
        
    
        
    
   
    
    
            
         
            
    
    def game_over(self):
        pass
    


    

