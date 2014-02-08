import BJ_card,BJ_player

class BJ_game(object):
    """A plantform for blackjack game"""
    def __init__(self):
        self.theDeck = BJ_card.deck() #the deck
        self.theLeft = BJ_card.deck() #put all used card here
        self.theDeck.generate()       
        self.theDeck.shuffle()
        self.theDealer = BJ_player.dealer("dealer")
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
 
        self.theDeck.deal(self.theDealer,2)
        self.theDealer.flip_down()
        print (self.theDealer) # give two cards to deck itself 
        self.theDealer.flip_the_card()
        print (self.theDealer)  #hide the first card
        
        
        for user in self.userList:
            ques = "what to do," + str(user.name) + "? (stand/hit/surrender):"
            ans = user.answer(ques)
            
            while ans and not user.isBusted and not user.isStand and not user.is21 and not user.isGreedy:
                if ans == "stand":
                    user.stand()
                    
                elif ans == "hit":
                    user.hit()

                    if not user.max_card():
                        self.theDeck.deal(user)
                    
                    print (user)
                    user.is_busted()
                    
                    if user.isBusted:
                        pass
                        
                    elif user.is21:
                        user.lucky()
                        
                    else:
                        ques = "what to do," + str(user.name) + "? (stand/hit/surrender):"
                        ans = user.answer(ques)
                    
                elif ans == "surrender":
                    user.surrender()
                    
                else:
                    print ("I dont understand your command")
                

        # if there is no user in the user list, flip the card of dealer
        # else count the point and the one with value wins the game
        
        winner = None  
        max = 0
        
        if len(self.userList):
            for user in self.userList:
                if user.count > max and not user.isBusted and not user.isSurrender:
                    max = user.count
                    winner = user
                    
        if max > 0 and winner: # find the maximum one
            winner.win()
            
        else:
            self.theDealer.flip(self.theDealer.holdCard[1])
            print (self.theDealer)
            self.theDealer.win()
            
        
                
if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")               
            
            
            
                
