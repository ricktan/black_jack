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
        self.is21 = False
        self.isGreedy = False
        
    def __str__(self):
        rep = super(player, self).__str__() 
        rep = str(self.name) + ":" + rep
        return rep
    
    def answer(self,ques):
        ans = input(ques)
        return ans
        
    def ask_number(self,ques,low,high):
        question = str(ques) + "(" + str(low) + "-" + str(high) + "):"
        num = input(question)
        low = int(low)
        high = int(high)
        
        while num not in range(low,high):
            question = str(ques) + "(" + str(low) + "-" + str(high) + "):"
            num = input(question)
        
        return num
        
    def win(self):
        print (str(self.name) + " wins") 
        
    def lose(self):
        self.surrender()
        print (str(self.name) + " loses") 
        
    def stand(self):
        self.isStand = True
    
    def hit(self):
        self.isHit = True
        
    def surrender(self):
        for each in self.holdCard:
            if not each.isFaceUp:
                self.flip(each)
                self.discard(each)
        self.isSurrender = True
    
    def is_busted(self):
        if self.count > 21:
            self.isBusted = True
            print (self.name + ",you are busted")
            
        elif self.count == 21:
            self.is21 = True
    
    def lucky(self):
        self.is21 = True
        
    def max_card(self):
        if len(self.holdCard) >= 5:
            print ("Sorry, you can have 5 cards at most")
            return True
            self.isGreedy = True
        else:
            return False
    
class dealer(player):
    """ the dealer of the game"""
    def flip_down(self):
        if self.holdCard:
            for card in self.holdCard:
                card.isFaceUp = False
        
    def flip_the_card(self):
        self.flip(self.holdCard[0])
        
if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")            
    
        
        