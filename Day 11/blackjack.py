import random

from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10 ,10, 10 ]

play_blackjack = True

def get_score(hand):
    score = sum(hand["cards"]) 
    ace_count = hand["cards"].count(11)
    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1
    return score

def get_card_count(hand):
    return len(hand["cards"])

def get_dealer_hand(dealer):
    return dealer["cards"]

def get_player_hand(player):
    return player["cards"]

def blackjack(hand):
    return get_card_count(hand) == 2 and get_score(hand) == 21


def busted(hand):
    return get_score(hand) > 21


def end_game_score(player, dealer):
    print(f"Dealer score is: {get_score(dealer)}\n")
    print(f"Your score is: {get_score(player)}\n")
    if get_score(player) > get_score(dealer):
        print("You win!")
    elif get_score(player) < get_score(dealer):
        print(f"Dealer score is: {get_score(dealer)}\n")
        print(f"Your score is: {get_score(player)}\n")
        print("Dealer wins!")
    else:
        print("Push!")



player = {
    "cards": [],
}

dealer = {
    "cards": [],
}


def start_new_game(play_blackjack):
        while play_blackjack:
            play_again = input("Would you like to play again? Type 'y' for yes, or 'q' to quit.\n")
            if play_again in ['y', 'q']:
                break
            print("Invalid, try again!")
        if play_again == 'y':
            return True
        if play_again == 'q':
            print("Thanks for playing!")
            quit()
  
        
def dealing(player, dealer):
        print("Welcome to blackjack!")
        while get_card_count(player) < 2 and get_card_count(dealer) < 2:
            player["cards"].append(random.choice(cards))
            dealer["cards"].append(random.choice(cards))
        if get_card_count(player) == 2 and get_card_count(dealer) == 2:
            print("Finished dealing starting hands")
            print(f"You have: {player['cards']} dealer shows: {dealer['cards'][1]}")
            print(f"Your score is: {get_score(player)}\n")
            return True


def drawing(player):
    while get_score(player) < 21:
        while True:
            draw = input("Would you like another card? Type 'y' to draw or 'n' to stand.\n")
            if draw in ['y', 'n']:
                break
            print("Invalid, try again!")
        if draw == 'y':
            player["cards"].append(random.choice(cards))
            print(f"You have: {player['cards']}\n")
            print(f"Your score is: {get_score(player)}\n")
            print(f"Dealer shows: {dealer['cards'][1]}\n")
        if busted(player):
            print(f"You busted. Dealer wins!!")
            return False
        if draw == 'n':
            return True
    
def dealer_play(dealer):
    while get_score(dealer) < 16:
        print(f"Dealer has: {dealer['cards']}\n")
        print(f"Dealer is drawing cards... \n")
        dealer["cards"].append(random.choice(cards))
        print(f"Dealer score is now: {get_score(dealer)}\n")
        if busted(dealer):
            print(f"Dealer busts. You win!!")
            break
    return get_score(dealer)


def main_game(play_blackjack):
        while True:
            play_game = input("Would you like to play Black Jack? Type 'y' to play or 'n' to quit.\n")
            if play_game in ['y', 'n']:
                break
            print("Invalid, try again!")
        if play_game == 'n':
            print("Have a nice day!")
            play_blackjack = False
            quit()
        while play_blackjack:
            print("\n" * 100)
            print(logo)
            player["cards"].clear()
            dealer["cards"].clear()
            dealing_result = dealing(player, dealer)
            if blackjack(player) and blackjack(dealer):
                print("Both have blackjack! Push!")
                start_new_game(play_blackjack)
                continue
            elif blackjack(player):
                print("You made blackjack! You win!")
                start_new_game(play_blackjack)
                continue
            elif blackjack(dealer):
                print("Dealer has blackjack! Dealer wins!")
                start_new_game(play_blackjack)
                continue
            if dealing_result:
                drawing_result = drawing(player)
            if busted(player):
                start_new_game(play_blackjack)
                continue
            if drawing_result:
                dealer_play(dealer)
            if busted(dealer):
                start_new_game(play_blackjack)
                continue
            end_game_score(player, dealer)
            start_new_game(play_blackjack)

main_game(play_blackjack)
