from random import choice

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

safe = 0

machine_on = True


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Pease insert coins.")
    total = int(input("how many quartesrs?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def its_pay_ok(money, drink_cost):
    """Return True if have sufficient money, else False"""
    if money >= drink_cost:
        change = round(money - drink_cost, 2)
        print(f"Here is your change : ${change}")
        global safe
        safe += drink_cost
        return True
    else:
        print("Sorry you lack money.")    
        return False


def is_enought(order_ingredients):
    """Returns True when have enougth resoruces, False if dont have them"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f'Sorry is not enougth {item}' )
            return False
    return True    


def make_coffe(drink_name, order_ingredients):
    """Take a ingredient and subtract from the resoruces"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
        print(f"Yor {drink_name} its ready! ☕️")


while machine_on:
    
    coffee_choice = input("☕ What would you like? (espresso/latte/cappuccino):  ").lower()
    if coffee_choice == 'off':
        machine_on = False
    elif coffee_choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}ml")
        print(f"money: ${safe}")
    else:
         drink = MENU[coffee_choice]  
         if is_enought(drink["ingredients"]):
            payment = process_coins()
            if its_pay_ok(payment , drink['cost']):
                make_coffe(choice , drink["ingredients"])
