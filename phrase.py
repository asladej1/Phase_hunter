# Create your Phrase class logic here.



class Phrase():
    
    
    
    
    def __init__(self,phrase):
        self.phrase = phrase
        
        
    def display(self, guess):
        display_phrase = []
        for letter in self.phrase:
            if letter in guess:
                display_phrase.append(letter)
            elif letter == ' ':
                display_phrase.append(' ')       
            else:
                display_phrase.append('_')
        print(' '.join(display_phrase))
        
         
    def check_letter(self,guess):
        if guess in self.phrase:
            return True
        else:
            return False
        
        
    def check_complete(self):
        if display_phrase == self.phrase:
            return True
        else:
            return False
    
    
#go = Phrase()
#go.display("j")
#go.check_letter("j")
          