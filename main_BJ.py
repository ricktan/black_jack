import sys
# import the sys paths if there isnt any
module_path = 'C:\\Users\\Tan\\Dropbox\\black_jack'
module_path1 = 'C:\\Users\\Rick L Tan\\black_jack'

if '' in sys.path:
    sys.path.remove('')

for path in [module_path,module_path1]:
    if path not in sys.path:
        sys.path.append(path)

import BJ_card, BJ_player, BJ_game

# main program here  
print ("$o$ welcome to the game that could make you the richest man in the world!")
thisGame = BJ_game.BJ_game()
system = BJ_player.player("System")
player_num = thisGame.ask_number("How many players",2,5)

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

thisGame.start()

while thisGame.again:
    print ("hello")
    thisGame.isRunning()


# a hand for each player a deck 52 cards deal one card at time
# show dealer's card all the time
#     for one player in the player list:
#         show all the card with how much does player have
#         check if user is 21
#         while and not stand and not surrender and not busted and not 21:
# 			ask which action does player want to do
#             hit or stand or surrender 
#             if hit
#                   if check how many cards in hand
#                       ask how much (on the base of 10)
#                       do the match (self.money)
#                       deal 1 more cards from the deck to the current hand
#                       check if busted
#                       if it is, he will be exluded from the list later on
#             else if stand:
#                   break to the other player
#             else if surrender:
#                   end the turn and remove the name from the list discard
#                   all the cards in the hand
# check anyone if is busted or not
# eliminate the busted player
#
# clip all the cards
# decide who wins            
# jump out of the current round





