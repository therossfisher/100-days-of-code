import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10 ,10, 10 ]

play_blackjack = True
dealer_blackjack = False
player_blackjack = False


def get_score(hand):
    return sum(hand["cards"]) 

def get_card_count(hand):
    return len(hand["cards"])

def blackjack(hand):
    if get_card_count(hand) == 2 and get_score(hand) == 21:
        hand["blackjack"] = True
        return True
    else:
         return False
    
def busted(hand):
    if get_score(hand) > 21:
        print(f"{get_score(player)} Bust. Game over!")
        return True
    else:
        return False

player = {
    "cards": [],
}

dealer = {
    "cards": [],
}


def dealing(player, dealer):
        while get_card_count(player) < 2:
            player["cards"].append(random.choice(cards))
        while get_card_count(dealer) < 2:
            dealer["cards"].append(random.choice(cards))
        print("Finished dealing starting hands")
        print(f"You have: {player['cards']} dealer has: {dealer['cards'][1]}")
        if blackjack(dealer) and blackjack(player):
            print(f"You have: {player['cards']} dealer has: {dealer['cards']}")
            print("Dealer has blackjack, you lose!")
        elif blackjack(dealer):
            print(f"You have: {player['cards']} dealer has: {dealer['cards']}")
            print("Dealer has blackjack, you lose!")
        elif blackjack(player):
            print("You hit blackjack, you win!")
        return player, dealer

def drawing(player):
    while get_score(player) < 21:
        while True:
            draw = input("Would you like another card? Type 'y' to draw or 'n' to stand.\n")
            if draw in ['y', 'n']:
                break
            print("Invalid, try again!")
        if draw == 'y':
            player["cards"].append(random.choice(cards))
            get_score(player)
            print(f"You have: {player['cards']}\n")
            print(f"Your score is: {get_score(player)}\n")
            print(f"Dealer shows: {dealer['cards'][0]}\n")
        if busted(player):
            print(f"{get_score(player)} Bust. Game over!")
            break
        elif draw == 'n':
            break
    return get_score(player)
        
dealing(player, dealer)

drawing(player)

player_score = get_score(player)

dealer_score = get_score(dealer)

print(player_score)

print(dealer_score)

# play_blackjack, dealing, draw, busted_play_again, player_score, player_cards, dealer_cards, dealer_blackjack, player_blackjack, dealer_score = blackjack(play_blackjack, dealing, draw, busted_play_again, player_score, player_cards, dealer_cards, dealer_blackjack, player_blackjack, dealer_score)  



# # Requirements: 

# once user is done and no longer wants more cards:
# let computer play
# computer should keep drawing cards unless score goes over 16

# compare user and computer scores:
# win, loss or draw

# print user and computers final hand and score at end of game

# after game ends, ask user if they want to play again
# clear console for a fresh start

# start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n'.")