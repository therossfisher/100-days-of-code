# Rules:
# deck is unlimited size
# no jokers
# J/Q/K all count as 10
# A counts as 11 or 1
# all cards have equal probablity of being drawn
# cards not removed from deck as they are drawn
# computer is the dealer


import random

# deal both user and computer a starting hand of 2 random card values

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []

dealer_cards = []

player_score = sum(player_cards)

dealer_score = sum(dealer_cards)

play_blackjack = True

while play_blackjack:
        while len(player_cards) < 2:
            player_cards.append(random.choice(cards))
            print(player_cards)
        while len(dealer_cards) < 2:
            dealer_cards.append(random.choice(cards))
            print(dealer_cards)
        if len(dealer_cards) ==2 and len(player_cards) == 2:
             print(f"You have: {player_cards[0]}, {player_cards[1]} dealer has: {dealer_cards[1]}")
             print(player_score)
             print(dealer_score)
             break

print(player_cards)
print(dealer_cards)



# Requirements: 

# detect when computer or user has blackjack (A + 10 value cards)



# if computer gets blackjack, then user loses, (even if user also has blackjack)
# if user gets blackjack they win unless computer also has blackjack

# calculate users and computers scores based on their card values

# if A drawn count it as 11
# but if total goes over 21 count as 1

# reveal computers first card to user

# game ends immediately when user score goes over 21
# or if user or computer get blackjack

# ask the user if they want to get another card

# once user is done and no longer wants more cards:
# let computer play
# computer should keep drawing cards unless score goes over 16

# compare user and computer scores:
# win, loss or draw

# print user and computers final hand and score at end of game

# after game ends, ask user if they want to play again
# clear console for a fresh start

# start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n'.")


