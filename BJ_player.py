import cards
import BJ_card

class player(BJ_card.hand):
    """ A player for the game"""
    # attributes
    def __init__(self,name,score = 100,bet = 10):
        super(player, self).__init__()
        self.name = str(name)
        self.score = score
        self.bet = bet # the bet you have 
        self.isBusted = False
        self.isStand = False
        self.isSurrender = False
        self.is21 = False
        self.isGreedy = False #wants to get more than 5 cards

        
    def __str__(self):
        rep = super(player, self).__str__() 
        rep = str(self.name) + ":" + rep + " " + str(self.score)
        return rep
    
    def answer(self,ques):
        ans = input(ques)
        return ans
        
    def win(self):
        win = self.bet * 2
        self.score += win
        print (str(self.name) + " gets $" + str(win) + "! Good job :)") 
        
    def lose(self):
        lose = self.bet
        self.score -= lose
        print (str(self.name) + " loses $" + str(lose) + "!:(") 
        
        
    def surrender(self):
        for each in self.holdCard:
            if not each.isFaceUp:
                self.flip(each)
                self.discard(each)
        self.isSurrender = True
        self.lose()
    
    def is_busted(self):
        if self.count > 21:
            self.isBusted = True
            print (self.name + ",you are busted")
            self.lose()
            
        elif self.count == 21:
            self.is21 = True

        
    def max_card(self):
        if len(self.holdCard) >= 5:
            print ("Sorry, you can have 5 cards at most")
            return True
            self.isGreedy = True
        else:
            return False
            
    def bet(self,amount):
        if amount <= self.score:
            self.score -= amount
        else:
            print ("All in!")
            self.score = 0
    
class dealer(player):
    """ the dealer of the game"""
    def flip_down(self):
        if self.holdCard:
            for card in self.holdCard:
                card.isFaceUp = False
        
    def flip_the_card(self):
        self.flip(self.holdCard[0])
        
    def win(self):
        print ("Dealer wins :D")
        
    def lose(self):
        self.score = 0
        
        
        
if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")            
    
        
        