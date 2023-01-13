MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 1.Print report of coffe machine recoursces

is_on = True
coins_inserted = 0

def sufficient_resources(order_ingredient):
    """Returns true if order can be made, or false if not."""
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

    
    
def report():
    print(MENU.espresso)
    print(MENU.latte)
    print(MENU.capuccino)




def process_coins():
    """Returns the total amount of coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.1
    total += int(input("How many nickels?")) * 0.05
    total += int(input("How many pennies?")) * 0.01

    return total

def check_transaction_successful(money_received,drink_cost):
    """Return true if payment is accepted, or false if not."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Your amonunt of change is {change}.")
        global coins_inserted
        coins_inserted += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, all_ingredients):
    """deduct the required ingredients resources."""
    for item in all_ingredients:
        resources[item] -= all_ingredients[item]
        print(f"Here is your {drink_name}")

while is_on:

    user_choice = input("What would you like? (espresso/latte/capuccino): " + user_choice)
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffe: {resources['coffee']}g")
        print(f"Money: {coins_inserted}")
    else:
        drink = MENU[user_choice]
        if sufficient_resources(drink["ingredients"]):
            payment = process_coins()
            check_transaction_successful(payment, drink["cost"])
            make_coffee(user_choice, drink["ingredients"])


#TODO: IMPLEMENTAR A FUNÇÃO PROCESS_COINS, E O CHECK TRANSACTION,E POR FIM O MAKE_COFFE


def coffee_machine(argument):
    match argument:
        case 0:
            return "zero"
        case default:
            exit()

