import random
deck = []
suits = ["♠", "♥", "♦", "♣"]
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]

#Combine the suits and values
for suit in suits:
    for value in values:
        deck.append(value + suit)

#Function to deal cards
def deal_cards(num_cards,deck):
    hand = []
    for i in range(num_cards):
        card = random.choice(deck) 
        hand.append(card)
        deck.remove(card)
    return hand

#Calculate the value of a hand
def hand_value(hand):
    value = 0
    for card in hand:
        if card[0] == "A":
            if value + 11<= 21:
                value += 11
            else:
                value += 1
        elif card[0] in ["J", "Q", "K"]:
            value += 10
        else:
            value += int(card[0])
    return value

def is_blackjack(hand):
    return hand_value(hand) == 21

def is_bust(hand):
    return hand_value(hand) > 21

def play_round():
    #Deal 2 cards to the player and 1 card to the dealer
    player_hand = deal_cards(2, deck)
    dealer_hand = deal_cards(1,deck)

    #Print the hands

    print(f"PLayer's hand: {player_hand}")
    print(f"Dealer's hand: {dealer_hand[0]}, ??") #Only show one of the dealer's cards

    #Check if player has blackjack
    if is_blackjack(player_hand):
        print("Blackjack! You win!")
        return
    
    #ask the player if they want to hit or stand
    while True:
        choice = input("Do you want to hit or stand? ").lower()
        if choice == "hit":
            player_hand += deal_cards(1, deck)
            print(f"Player's hand: {player_hand}")
            #Check if the player has bust
            if is_bust(player_hand):
                print("Bust! You lose!")
                return
        elif choice == "stand":
            break

    #Dealer's turn
    while hand_value(dealer_hand) < 17:
        dealer_hand += deal_cards(1, deck)

    #Determine the winner
    player_value = hand_value(player_hand)
    dealer_value = hand_value(dealer_hand)
    if is_bust(dealer_hand):
        print("Dealer busts! You win!")
    elif dealer_value == player_value:
        print("Push.")
    elif dealer_value > player_value:
        print("Dealer wins.")
    else:
        print("You win!")

#play the game
play_round()
