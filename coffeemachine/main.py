from coffeemachine_menu import menu

def print_report(resources):
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Total_balance: ${(resources["cost"]) * -1}")

def is_resource_sufficient(order_ingredients, resources):
    water = resources["water"] - order_ingredients["water"]
    milk = resources["milk"] - order_ingredients["milk"]
    coffee = resources["coffee"] - order_ingredients["coffee"]
    if (water < 0):
        print("Not enough water.")
        return False
    elif (milk < 0):
        print("Not enough milk.")
        return False
    elif (coffee < 0):
        print("Not enough coffee.")
        return False
    else:
        return True

def process_payment(drink):
    print("Please insert coins.")
    total = 0
    total += int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    if (total >= drink["cost"]):
        print(f"Here is ${round(total - drink["cost"], 2)} change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink, choice):
    for item in drink:
        resources[item] -= drink[item]
    print(f"here is your {choice}. Enjoy!")

def coffee_machine(resources):
    is_on = True
    while (is_on == True):
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if (choice == "off"):
            is_on = False
        elif (choice == "report"):
            print_report(resources)
        else:
            drink = menu[choice]
            if (is_resource_sufficient(drink, resources)):
                payment = process_payment(drink)
                if (payment == True):
                    make_coffee(drink, choice)

resources = {
    "water": 1000,
    "milk": 1000,
    "coffee": 200,
    "cost": 0
}
coffee_machine(resources)