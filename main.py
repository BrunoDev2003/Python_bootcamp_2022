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



def coffee_choice():
    user_choice = input("What would you like? (espresso/latte/capuccino): " + user_choice)
    
def report():
    print(MENU.espresso)
    print(MENU.latte)
    print(MENU.capuccino)


def coffee_machine(argument):
    match argument:
        case 0:
            return "zero"
        case default:
            exit()


