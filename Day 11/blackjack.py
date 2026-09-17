# Rules:
# deck is unlimited size
# no jokers
# J/Q/K all count as 10
# A counts as 11 or 1
# all cards have equal probablity of being drawn
# cards not removed from deck as they are drawn
# computer is the dealer


import random

## deal both user and computer a starting hand of 2 random card values
## detect when computer or user has blackjack (A + 10 value cards)# if computer gets blackjack, then user loses, (even if user also has blackjack)
## if user gets blackjack they win unless computer also has blackjack

## calculate users and computers scores based on their card values
# reveal computers first card to user
# game ends immediately when user score goes over 21
# or if user or computer get blackjack


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10 ,10, 10 ]


play_blackjack = True
dealing = True
draw = True

def start_dealing(player_cards, dealer_cards, player_score, dealer_score):
        while len(player_cards) < 2:
            player_cards.append(random.choice(cards))
            player_score = sum(player_cards)
        while len(dealer_cards) < 2:
            dealer_cards.append(random.choice(cards))
            dealer_score = sum(dealer_cards)
        return player_cards, dealer_cards, player_score, dealer_score

        
def starting_hands(player_cards, dealer_cards, player_score, dealer_score):
        player_cards, dealer_cards, player_score, dealer_score = start_dealing(player_cards, dealer_cards, player_score, dealer_score)
        dealer_blackjack = dealer_cards == [10,11] or dealer_cards == [11,10]
        player_blackjack = player_cards == [10,11] or player_cards == [11,10]
        print(player_cards, dealer_cards, player_score, dealer_score)
        if len(dealer_cards) == 2 and len(player_cards) == 2:
            print("Finished dealing starting hands")
            print(f"You have: {player_cards[0]}, {player_cards[1]} dealer has: {dealer_cards[1]}")
        if dealer_blackjack:
            print("Dealer has blackjack, you lose!")
        elif player_blackjack:
            print("You hit blackjack, you win!")
        return dealer_blackjack, player_blackjack, player_cards, dealer_cards, player_score, dealer_score

def player_drawing(draw, player_score, player_cards, dealer_cards):
    while player_score < 21:
            while True:
                draw = input("Would you like another card? Type 'y' to draw or 'n' to stand.\n")
                if draw in ['y', 'n']:
                    break
                print("Invalid, try again!")
            if draw == 'y':
                player_cards.append(random.choice(cards))
                player_score = sum(player_cards)
                print(f"You have: {player_score}")
                print(f"Dealer shows: {dealer_cards[0]}")
            elif draw == 'n':
                break
    return draw, player_score, player_cards, dealer_cards
    
while play_blackjack:
    player_cards = []
    dealer_cards = []
    player_score = 0
    dealer_score = 0
    dealer_blackjack, player_blackjack, player_cards, dealer_cards, player_score, dealer_score = starting_hands(player_cards, dealer_cards, player_score, dealer_score)
    if dealer_blackjack or player_blackjack:
         play_blackjack = False
    draw, player_score, player_cards, dealer_cards = player_drawing(draw, player_score, player_cards, dealer_cards)
    break # TEMP REMOVE ONCE PLAYER DRAWING IS BUILT IT     
    
# while player_score > 21 and 11 in player_cards:
#     player_score -= 10
# while dealer_score > 21 and 11 in dealer_cards:
#     dealer_score -= 10

# draw, player_score, player_cards, dealer_cards = player_drawing(draw, player_score, player_cards, dealer_cards)

# while dealing:
#         player_cards, dealer_cards, player_score, dealer_score = start_dealing(player_cards, dealer_cards, player_score, dealer_score)
            
        
# ask the user if they want to get another card


# Requirements: 








# once user is done and no longer wants more cards:
# let computer play
# computer should keep drawing cards unless score goes over 16

# compare user and computer scores:
# win, loss or draw

# print user and computers final hand and score at end of game

# after game ends, ask user if they want to play again
# clear console for a fresh start

# start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n'.")


