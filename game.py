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
            print(f'\nNumber missed: {self.missed}')
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
            print("You guessed it right! Congratualations!\n")
    
        self.new_game()
        
    def get_guess(self):
            guess = input('Please enter letter: \n')
            
            while guess in self.guesses:
                print("\nYou've already guessed that letter. Try again.\n")
                print(f"Number missed:{self.missed}\n")
                self.active_phrase.display(self.guesses)
                guess = input('Please enter letter: ')
                    
            
            while len(guess) > 1 or guess.isdigit():
                print("\nInvalid input. Only one letter at a time\n")
                print(f"Number missed:{self.missed}\n")
                self.active_phrase.display(self.guesses)
                guess = input('\nPlease enter a letter: ')
                
            
            return guess
                
    def new_game(self):
        restart = input("Would you like to play again?:  ")
        if restart.lower() == "yes":
            game = Game()
            print(game.active_phrase.phrase)
            game.start()
        else:
            print('\nThank you for playing!')
            exit()
