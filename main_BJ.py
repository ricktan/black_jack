import sys
# import the sys paths if there isnt any
module_path = 'C:\\Users\\Tan\\Dropbox\\guess_song'

if module_path not in sys.path:
    sys.path.append(module_path)
    
import BJ_card, BJ_player, BJ_game

# main program herec  
# ask how many players in the game create a list for all players
print ("$o$ welcome to the game that could make you the richest man in the world!")
system = BJ_player.player("System")
player_num = system.ask_number("How many players",2,5)
thisGame = BJ_game.BJ_game()

for num in range(player_num):
    name = system.answer("Player Name:")
    curplayer = BJ_player.player(name)
    if num == 0:
        player1 = curplayer
    elif num == 1:
        player2 = curplayer
    elif num == 2:
        player3 = curplayer
    elif num == 3:
        player4 = curplayer
    elif num == 4:
        player5 = curplayer
    thisGame.add(curplayer)
    
print (thisGame)

thisGame.start()

# a hand for each player a deck 52 cards deal two cards for each player,
# the first card face up and another one face down count the amount for
# each player while in the round:
#     for one player in the player list:
#         while card in hand are smaller than 21 and not stand and not
#         surrender:
# 			ask which action does player want to do
#             hit or stand or surrender if hit
#                   deal 1 more cards from the deck to the current hand
#             else if stand:
#                   break to the other player
#             else if surrender:
#                   end the turn and remove the name from the list discard
#                   all the cards in the hand
#          if the current player is busted:
#             break the loop
# clip all the cards
# decide who wins            
# jump out of the current round







# theDeck = cards.deck()
# theDeck.generate()
# print ("All kinds of cards are listed: " + str(theDeck))
# theDeck.shuffle()
# print ("All kinds of cards are listed: " + str(theDeck))
# 
# myHand = cards.hand()
# yourHand = cards.hand()
# 
# theDeck.deal(myHand,2)
# theDeck.deal(yourHand,2)
# print("Cards that I have are like: " + str(myHand))
# print("Cards that You have are like: " + str(yourHand))