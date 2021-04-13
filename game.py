# Create your Game class logic in here.
from phrase import Phrase
import random



class Game:
    
    def __init__(self):
        self.missed = 0
        self.phrases = [Phrase('Is the juice worth the squeeze'), Phrase('Green Lights'), Phrase('An Arm and a Leg'), Phrase('Dime a Dozen'), Phrase('Down to the Wire')]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]
        
    def welcome(self):
        GREETING = "==========================\n Welcome to Phrase Hunter\n=========================="
        print(GREETING.upper())
        rules = print("\nRules: \n******Try and guesses the phrase! Select a letter on a time, if you can't solve it before your 5 guess up you lose. Good luck!.******\n\n")    
    
    def get_random_phrase(self):
        sel_phrase = random.choice(self.phrases)
        return sel_phrase
    
    def start(self):
        self.welcome()
        while self.missed < 5 and self.active_phrase.check_complete(self.guesses) == False:
          print(f'Number missed: {self.missed}')
          self.active_phrase.display(self.guesses)
          user_guess = self.get_guess()
          self.guesses.append(user_guess)
          if not self.active_phrase.check_guess(user_guess):
            self.missed += 1
          self.active_phrase.check_complete(self.guesses)
        self.game_over()
        
    def game_over(self):
      if self.missed == 5:
        print("Sorry, Game Over...")
      else:
        print("You guessed it right! Congratualations!")
        
        
    def get_guess(self):
        try:
          self.guess = input('Please enter letter: ')
          
      
          
          if len(self.guess) > 1:
            print('1')
          
          else:
            raise ValueError
          
          #else:
          #return self.guess
        
        except ValueError as err:
          print('\nInvalid input. One letter at a time.')
        
    
