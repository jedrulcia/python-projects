from gamedata import gamedata
import random
import os

def get_random_account():
    return random.choice(gamedata)

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return (f"{name}, {description} from {country}")
    
def print_informations(account_a, account_b):
    print(f"A: {format_data(account_a)}")
    print("OR")
    print(f"B: {format_data(account_b)}")
    
def check_answer(account_a, account_b, answer):
    follower_count_a = account_a["follower_count"]
    follower_count_b = account_b["follower_count"]
    if (answer == 'A' and follower_count_a >= follower_count_b):
        return True
    elif (answer == 'B' and follower_count_b >= follower_count_a):
        return True
    else:
        return False
    
def winnter_account(account_a, account_b):
    follower_count_a = account_a["follower_count"]
    follower_count_b = account_b["follower_count"]
    if (follower_count_a > follower_count_b):
        return account_a
    else:
        return account_b
    
def gameplay():
    should_continue = True
    score = 0
    account_b = get_random_account()
    while (should_continue == True):
        account_a = account_b
        account_b = get_random_account()
        while (account_a == account_b):
            account_b = get_random_account()
            
        print_informations(account_a, account_b)
        answer = input("Who has more followers? Type 'A' or 'B': ").upper()
        should_continue = check_answer(account_a, account_b, answer)
        os.system("cls")
        
        if (should_continue == True):
            score += 1
            print(f"You're right! Current score: {score}.")
            account_b = winnter_account(account_a, account_b)
          
    print(f"Sorry, that's wrong. Final score: {score}.")
    
gameplay()
        
    


