
import cards

class card(cards.card):
    """A black jack card"""
    @property 
    # as for the property, there is no need to add () at the end,as it is not callable!
    def amount(self):
        rank = self.rank
        if rank in ['10','J','Q','K']:
            rank = 10
        elif rank == 'A':
            rank = 10
        else:
            rank = card.rank.index(rank) + 1
        return int(rank)

        
class hand(cards.hand):
    """A speicific hand for playing black jack"""
    @property
    def count(self):
        value = 0
        ace = False
        # check if there is A in the card list:
        for each in self.holdCard:
            if each.rank == 'A':
                for bigRank in ['10','J','Q','K']:
                    if bigRank in self.holdCard:
                        ace = True
        
            if ace:
                value += 1
            else:
                value += each.amount
            #print (value)
        return value
            
        
class deck(cards.deck):
    """A deck for black jack game"""
    def generate(self):
        for num in card.rank:
            for kind in card.suit:
                thisCard = card(num,kind)
                self.holdCard.append(thisCard)
                
if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")            
    