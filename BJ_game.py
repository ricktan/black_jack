import BJ_card,BJ_player

class BJ_game(object):
    """A plantform for blackjack game"""
    def __init__(self):
        self.theDeck = BJ_card.deck() #the deck
        self.theLeft = BJ_card.deck() #put all used card here
        self.theDeck.generate()       
        self.theDeck.shuffle()
        self.theDealer = BJ_player.dealer()
        self.userList = []
    
    def __str__(self):
        rep = ""
        for player in self.userList:
            rep += str(player.name) + "\t" + str(player.score) + "\n"
        return rep
        
            
    def add(self,onePlayer):
        if onePlayer not in self.userList:
            self.userList.append(onePlayer)
        
    def start(self):
        for user in self.userList:
            self.theDeck.deal(user,2)
            print (user)
 
        self.theDeck.deal(self.theDealer,2) # give two cards to deck itself 
        self.theDealer.flip_the_card() #hide the first card
        
        for user in self.userList:
            ques = "what to do," + str(user.name) + "? (stand/hit/surrender):"
            ans = user.answer(ques)
            while ans and not user.isBusted :
                if ans == "stand":
                    user.stand()
                    break
                                      
                elif ans == "hit":
                    user.hit()
                    print (str(user.count))
                    self.theDeck.deal(user)
                    print (user)
                    if user.is_busted():
                        user.lose()
                        break
                    
                elif ans == "surrender":
                    user.surrender()
                    
                ques = "what to do," + str(user.name) + "? (stand/hit/surrender):"
                ans = user.answer(ques)
            
            
            
            
            
                
