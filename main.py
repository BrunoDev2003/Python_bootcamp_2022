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


user_choice = input("What would you like? (espresso/latte/capuccino): " + user_choice)
coins_inserted = 0
    
    
def report():
    print(MENU.espresso)
    print(MENU.latte)
    print(MENU.capuccino)

def sufficient_resources():
    if user_choice == "espresso":
        if "water" <= 0:
            print("Sorry there is not enough water.")
        elif "coffe" <= 0:
            print("Sorry there is not enough coffee.")
    if user_choice == "latte":
        if "water" <= 0:
            print("Sorry there is not enough water.")
        elif "milk" <= 0:
            print("Sorry there is not enough milk.")
        elif "coffe" <= 0:
            print("Sorry there is not enough coffee.")
    if user_choice == "capuccino":
        if "water" <= 0:
            print("Sorry there is not enough water.")
        elif "milk" <= 0:
            print("Sorry there is not enough milk.")
        elif "coffe" <= 0:
            print("Sorry there is not enough coffee.")


def process_coins():

#TODO: IMPLEMENTAR A FUNÇÃO PROCESS_COINS, E O CHECK TRANSACTION,E POR FIM O MAKE_COFFE


def coffee_machine(argument):
    match argument:
        case 0:
            return "zero"
        case default:
            exit()


