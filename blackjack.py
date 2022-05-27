############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random


logo = """
                                      .------.
                   .------.           |A .   |
                   |A_  _ |    .------; / \  |
                   |( \/ )|-----. _   |(_,_) |
                   | \  / | /\  |( )  |  I  A|
                   |  \/ A|/  \ |_x_) |------'
                   `-----+'\  / | Y  A|
                         |  \/ A|-----'    
                         `------'"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
dealer_hand = []


def deal_first_cards():
    # Dealing the first hands to both player and computer.
    player_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))
    player_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))
    print(f"dealer's card is {dealer_hand[0]}")
    print('your cards are', str(player_hand).lstrip('[').rstrip(']'))
    return player_hand, dealer_hand


def deal_card(hand_who):
    # Deals the consequential hands, if needed.
    hand_who.append(random.choice(cards))
    if hand_who == dealer_hand:
        print("dealer's cards are", str(dealer_hand).lstrip('[').rstrip(']'))
    elif hand_who == player_hand:
        print('your cards are', str(player_hand).lstrip('[').rstrip(']'))
    return player_hand, dealer_hand


def summer(check_who):
    # Counts the scores for the hand in the argument.
    if (11 in check_who) and (sum(check_who) > 21):
        for index, item in enumerate(check_who):
            if item == 11:
                check_who[index] = 1
    return sum(check_who)


def checker(player_check, dealer_check):
    # Checks the winner based on the scores.
    if player_check == dealer_check:
        print("it's a draw")
    elif player_check > 21:
        print('you lose')
    elif dealer_check > 21:
        print('you win')
    elif player_check == 21:
        print('you win')
    elif dealer_check == 21:
        print('you lose')
    elif (21 - player_check) > (21 - dealer_check):
        print('you lose')
    elif (21 - player_check) < (21 - dealer_check):
        print('you win')


def repeater():
    # Offers to play another game.
    repeat = input('Do you wish to play a game of blackjack? type y or n \n')
    if repeat == 'y':
        play_game()


def play_game():
    # The actual game process.
    print(logo)
    deal_first_cards()

    flag_another = True
    while flag_another:
        another = input('would you like to draw another card? y or n ')
        if another == 'y':
            deal_card(player_hand)
        elif another == 'n':
            flag_another = False

    player_sum = summer(player_hand)
    dealer_sum = summer(dealer_hand)
    while dealer_sum < 16:
        deal_card(dealer_hand)
        dealer_sum = summer(dealer_hand)
        if dealer_sum > 16:
            break

    checker(player_sum, dealer_sum)
    repeater()