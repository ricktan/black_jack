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
        self.again = True  #check there are player left at the beggining of each round
        self.round = 0
    
    def __str__(self):
        rep = ""
        for player in self.userList:
            rep += str(player.name) + "\t" + str(player.score) + "\n"
        return rep
        
    def ask_number(self,ques,low,high):
        question = str(ques) + "(" + str(low) + "-" + str(high) + "):"
        num = input(question)
        num = int(num)
        low = int(low)
        high = int(high)
        
        while num not in range(low,high):
            question = "type a number in between" + "(" + str(low) + "-" + str(high) + "):"
            num = input(question)
            num = int(num)
            
        return num
            
    def add(self,onePlayer):
        if onePlayer not in self.userList:
            self.userList.append(onePlayer)
    
    def remove (self):
        for player in self.userList:
            if player.isBusted or player.isSurrender:
                self.userList.remove(player)

        
    def start(self):
        # deal cards to players and dealer
        count = 0
        while count < 2:
            self.theDeck.deal(self.theDealer)
            if count == 0:
                self.theDealer.flip_down()
            print (self.theDealer)
            for user in self.userList:
                self.theDeck.deal(user)
                print (user)
            count += 1

    def isRunning(self):
        for user in self.userList:
            
            user.isStand = False
            
            if self.round == 0:
                user.is_busted()
                
            if user.is21:
                    print (user.name + ",you are blackjack!")
                    print ("Your bet $" + self.bet)
                    user.win()
                    
            else:    
                while not user.isBusted and not user.is21 and not user.isGreedy and not user.isStand:
                    ques = "what to do," + str(user.name) + "? (stand/hit/surrender):"
                    ans = user.answer(ques)
                    
                    while ans not in ["stand","hit","surrend"]:
                        print ("I dont understand your command")
                        ques = "what to do," + str(user.name) + "? (stand/hit/surrender):"
                        ans = user.answer(ques)
                        
                    if ans == "stand":
                        user.isStand = True
                        
                    elif ans == "hit":
                        if not user.max_card():
                            self.theDeck.deal(user)
                        print (user)
                        user.is_busted()
                
                        if user.is21:
                            print (user.name + ",you are blackjack!")
                            print ("Your bet $" + self.bet)
                            user.win()
                        
                    elif ans == "surrender":
                        user.surrender()
                        
        self.remove()
        
        # if all the player chooses to stand
        check_winner = 0
        for user in self.userList:
            if user.isStand:
                check_winner += 1
                
        if check_winner == len(self.userList):
            # its dealer's time to play
            self.dealer_time()
            self.whoIsWinner()
            
        else:    
            self.round += 1
    def dealer_time(self):
        self.theDealer.max_card()
        self.theDealer.is_busted()
        self.theDealer.flip(self.theDealer.holdCard[0])
        
        while not self.theDealer.isGreedy and not self.theDealer.isBusted and not self.theDealer.is21 and self.theDealer.count <= 17:
            self.theDeck.deal(self.theDealer)
            print (self.theDealer)
            self.theDealer.max_card()
            self.theDealer.is_busted()
        
    def whoIsWinner(self):
        winner = self.theDealer  
        max = self.theDealer.count
        
        if len(self.userList):
            for user in self.userList:
                if user.count > max:
                    max = user.count
                    winner = user
                    
        if max > self.theDealer.count: 
            winner.win()
            
        else:
            print (self.theDealer)
            self.theDealer.win()
            for user in self.userList:
                user.lose()
            
        self.again = False
            
        
                
if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")               
            
            
            
                
