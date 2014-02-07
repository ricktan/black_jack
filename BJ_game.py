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
    
    def remove(self,loser):
        if loser in self.userList:
            self.userList.remove(loser)
            
        
    def start(self):
        for user in self.userList:
            self.theDeck.deal(user,2)
            print (user)
 
        self.theDeck.deal(self.theDealer,2) # give two cards to deck itself 
        self.theDealer.flip_the_card() #hide the first card
        
        for user in self.userList:
            ques = "what to do," + str(user.name) + "? (stand/hit/surrender):"
            ans = user.answer(ques)
            while ans and not user.isBusted and not user.isStand and not user.is21 :
                if ans == "stand":
                    user.stand()
                    
                elif ans == "hit":
                    user.hit()
                    self.theDeck.deal(user)
                    print (user)
                    
                    if user.is_busted():
                        user.lose()
                        
                    elif user.count == 21:
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
        
        if not self.userList:
            self.theDealer.win()
        elif len(self.userList) == 1:
            if self.userList[0].isBusted:
                self.theDealer.win()
            else:
                self.theDealer.flip(self.theDealer.holdCard[1])
                print(self.theDealer.count)
                
        elif len(self.userList) > 1:
            max = 0
            winner = None
            for user in self.userList:
                if user.count > max and not user.isBusted:
                    max = user.count
                    winner = user
            if max > 0: # find the maximum one
                winner.win()
            else:
                self.theDealer.win()
                
if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")               
            
            
            
                
