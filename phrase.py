# Create your Phrase class logic here.



class Phrase:
    
    def __init__(self, phrase):
        self.phrase = phrase.lower()
    
    def display(self, guesses):
        display = []
        
        for letter in self.phrase:
            if letter in guesses:
                display.append(letter)
            elif letter == ' ':
                display.append(' ')       
            else:
                display.append('_')
        print(' '.join(display))       
      
    def check_guess(self, guess):
        if str(guess) in self.phrase:
            return True

        else:
            return False
    
    def check_complete(self, guesses):
        for letter in self.phrase:
            if str(letter) not in guesses:
                return False
            
        return True
        
      
