class Phrase():
    
    
    
    
    def __init__(self,phrase):
        self.phrase = phrase
        
        
    def display(self, phrase):
        display_phrase = []
        self.phrase = phrase
        self.guess = guess
      
       
        #Can't get this to run
        #while check_complete() == False:
        for letter in self.phrase:
#            if self.guess in self.phrase:
#                display_phrase.append(letter)
            if letter == ' ':
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
        if self.display() == self.phrase:
            return True
        else:
            return False
    
    
    
#go = Phrase()
#go.display("j")
#go.check_letter("j")
