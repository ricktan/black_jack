# how many objects are there in the blackjack game?
# card, hands, player, deck, lefts
# the card object has no method to generate, it is the decker who is going to generate the 52 cards.

import random
class card(object):
    count = 0
    rank = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    suit = ['h','s','d','c'] #heart, clubs, dimonds, sleaps
    
    def __init__(self, r, s):
        self.rank = r
        self.card = s + r
        card.count += 1
        self.isFaceUp = True
    
    def __str__(self):
        if self.isFaceUp:
            return self.card
        else:
            return "XX"
        
class hand(object):
    """simulate the hand to withdraw,discard or show cards"""
    def __init__(self):
        self.holdCard = []
    
    def __str__(self):
        # flip the card or not
        allCard = ""
        if self.holdCard:
            for oneCard in self.holdCard:
                allCard += str(oneCard)+"\t"
            return allCard
        else:
            return str(None)
        
    # use print to show the attributes in hand class
    
    def withdraw(self,cards):
        if cards not in self.holdCard:
            self.holdCard.append(cards)
            return True
        else:
            print ("I already have this card" + str(cards)) # shouldnt happen this way
            return False
        
    
    def discard(self,cards):
        if cards in self.holdCard:
            self.holdCard.remove(cards)
            return True
        else:
            print ("I already delete this card" + str(cards)) # shouldnt happen this way
            return False
    
    def flip(self,cards):
        if cards in self.holdCard:
            if cards.isFaceUp:
                return False
            else:
                print (cards)
                return True
            
    def give(self,card,other_hand):
        if card in self.holdCard:
            self.discard(card)
            other_hand.withdraw(card)
            return True
        else:
            return False
            
    def empty(self):
        self.holdCard = []

    
class deck(hand):
    """ a collection of playing cards"""
    def generate(self):
        for oneKind in card.suit:
            for num in card.rank:
                thisCard = card(oneKind,num)
                self.holdCard.append(thisCard)
    
            
    def shuffle(self):
        random.shuffle(self.holdCard)
        
    def deal(self,oneHand,num = 1):
        num = int(num)
        # get top num cards one by one
        if num < len(self.holdCard): #self.holdCard is the piles of cards in the deck hand
            for i in range(num):
                oneHand.withdraw(self.holdCard[i])
                self.holdCard.remove(self.holdCard[i])
                
        else:
            print ("Sorry, there are not enough card in the deck")
        
if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")



