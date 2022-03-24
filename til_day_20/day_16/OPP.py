from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()

coffee_maker = CoffeeMaker()

money = MoneyMachine()

machine_on = True

while machine_on:
    choice = input(f"☕ What would you like? {menu.get_items()}:  ").lower()
    if choice == "report":
        coffee_maker.report()
    elif choice == 'off':
        machine_on = False
    else :
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
             coffee_maker.make_coffee(drink)