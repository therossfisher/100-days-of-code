import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10 ,10, 10 ]

play_blackjack = True
dealer_blackjack = False
player_blackjack = False


def get_score(hand):
    return sum(hand["cards"]) 

def get_card_count(hand):
    return len(hand["cards"])

def get_dealer_hand(dealer):
    return dealer["cards"]

def get_player_hand(player):
    return player["cards"]

def blackjack(hand):
    if get_card_count(hand) == 2 and get_score(hand) == 21:
        hand["blackjack"] = True
        return True
    else:
         return False
    
def busted(hand):
    if get_score(hand) > 21:
        print(f"Score is {get_score(hand)} Bust.\n")
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
            print(f"You busted. Dealer wins!!")
            break
        elif draw == 'n':
            break
    return False

def dealer_play(dealer):
    while get_score(dealer) < 16:
        print(f"Dealer has: {dealer['cards']}\n")
        print(f"Dealer is drawing cards... \n")
        while True:
            dealer["cards"].append(random.choice(cards))
            get_score(dealer)
            print(f"Dealer score is now: {get_score(dealer)}\n")
            if busted(dealer):
                print(f"Dealer busts. You win!!")
                break
        return get_score(dealer)


def main_game(play_blackjack):
    while play_blackjack:
        dealing(player, dealer)
        result = drawing(player)
        if result:
            print("Play again?")
            main_game(play_blackjack)
    else:
        dealer_play(dealer)

main_game(play_blackjack)
    

    # def showdown(hand):
    #     dealer_showdown = get_dealer_hand(dealer)
    #     player_showdown = get_player_hand(player)
    #     if hand 
    #     print(f"Dealer has: {dealer_showdown}\nPlayer has: {player_showdown}\n")
        

# print(f"Dealer has: {dealer_showdown}\nPlayer has: {player_showdown}\n")
# player_score = get_score(player)

# dealer_score = get_score(dealer)



########## ########## ########## ########## ########## ########## 


