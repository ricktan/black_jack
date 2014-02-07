import cards
import BJ_card

class player(BJ_card.hand):
    """ A player for the game"""
    # attributes
    def __init__(self,name,score = 0):
        super(player, self).__init__()
        self.name = str(name)
        self.score = score
        self.isStand = False
        self.isBusted = False
        self.isHit = False
        self.isSurrender = False
        
    def __str__(self):
        rep = super(player, self).__str__() 
        rep = str(self.name) + ":" + rep
        return rep
    
    def answer(self,ques):
        ans = str(input(ques))
        return str(ans)
        
    def ask_number(self,ques,low,high):
        question = str(ques) + "(" + str(low) + "-" + str(high) + "):"
        num = input(question)
        low = int(low)
        high = int(high)
        
        while num not in range(low,high):
            question = str(ques) + "(" + str(low) + "-" + str(high) + "):"
            num = input(question)
        
        return num
        
    def win(self,theGame):
        print (str(self.name) + "wins") 
        
    def lose(self,theGame):
        self.surrender()
        print (str(self.name) + "loses") 
        
    def stand(self):
        self.isStand = True
    
    def hit(self):
        self.isHit = True
        
    def surrender(self):
        for each in self.holdCard:
            if not each.isFaceUp:
                self.flip(each)
                self.discard(each)
        print (self)
        self.isSurrender = True
    
    def is_busted(self):
        if self.count > 21:
            self.isBusted = True
    
class dealer(BJ_card.hand):
    """ the dealer of the game"""
    def flip_the_card(self):
        self.flip(self.holdCard[0])
        
if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")            
    
        
        