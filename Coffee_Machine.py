#DEFINING THE MENU
#ingredients are measured in grams
MENU = {
    "espresso": {
        "ingredients":{
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 18
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

#Define the resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

#Define the starting profit
profit = 0

#Function to get the user choice
def get_user_choice():
    return input("What would you like to have? (espresso/latte/cappuccino) ")

#Function to check if there's enough resources
def check_resources(choice):
    for item in MENU[choice]["ingredients"]:
        if resources[item] < MENU[choice]["ingredients"][item]:
            print(f"Sorry, there's not enough {item}")
            return False
    return True

#Function to process the coins
def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles: ")) *0.05
    total += int(input("How many pennies: ")) *0.01
    return total

#Function to make the drink
def make_drink(choice):
    for item in MENU[choice]["ingredients"]:
        resources[item] -= MENU[choice]["ingredients"][item]
    print(f"Here is your {choice} . Enjoy!")
    global profit
    profit += MENU[choice]["cost"]

#Function to run the coffee machine
def run_coffee_machine():
    while True:
        choice = get_user_choice()
        if choice == "off":
            break
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}ml")
            print(f"Money: ${profit}")
        else:
            if check_resources(choice):
                payment = process_coins()
                if payment >= MENU[choice]["cost"]:
                    make_drink(choice)
                    change = round(payment - MENU[choice]["cost"], 2)
                    print(f"Here is ${change} dollars in change.")
                else:
                    print("Sorry, that's not enough money.")

run_coffee_machine()