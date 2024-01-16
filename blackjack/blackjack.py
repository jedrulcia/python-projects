import random
import os

def draw_single_card():
    random_number = random.randint(0, len(deck) - 1)
    return deck[random_number]
 
def starting_sequence():
    player_cards.append(draw_single_card())
    player_cards.append(draw_single_card())
    computer_cards.append(draw_single_card())
    computer_cards.append(draw_single_card())
    
def sum_of_cards(x_cards):
    sum = 0
    for card in x_cards:
        sum += card
    return sum

def gameplay():
    starting_sequence()
    should_continue = True
    while (should_continue == True):
        sum = sum_of_cards(player_cards)
        if (sum > 21 and 11 in player_cards):
            index = player_cards.index(11)
            player_cards[index] = 1
            sum = sum_of_cards(player_cards)
        print(f"Your cards: {player_cards} (sum: {sum})")
        print(f"Computer cards: [{computer_cards[0]}, X]")
        if (sum >= 21):
            should_continue = False
            os.system('cls')
            return game_end()
        answer = input("Do you want to draw more cards? Type 'y' to draw or 'n' to end: ")
        if (answer == 'n'):
            should_continue = False
            os.system('cls')
            return game_end()
        elif (answer == 'y'):
            player_cards.append(draw_single_card())
            os.system('cls')

def game_end():
    computer_sum = sum_of_cards(computer_cards)
    while (computer_sum < 17):
        computer_cards.append(draw_single_card())
        computer_sum = sum_of_cards(computer_cards)
    player_sum = sum_of_cards(player_cards)
    computer_sum = sum_of_cards(computer_cards)
    print(f"Your cards: {player_cards} (sum: {player_sum})")
    print(f"Computer cards: {computer_cards} (sum: {computer_sum})")
    if (player_sum > 21 and computer_sum > 21):
        print("Draw")
    elif (player_sum > 21):
        print("You lost")
    elif (computer_sum > 21):
        print("You won")
    elif (player_sum == computer_sum):
        print("Draw")
    elif (player_sum > computer_sum):
        print("You won")
    elif (player_sum < computer_sum):
        print("You lost")
    answer = input("Do you want to start again? Type 'y' if yes or 'n' if not: ")
    if (answer == 'y'):
        player_cards.clear()
        computer_cards.clear()
        os.system('cls')
        return gameplay()
    
        

   
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = [] 

gameplay()

    
    




