from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

def run_machine():
    print("\nOur drinks: " + menu.get_items() + "\n")
    user_request = input("What would you like? ")

    if user_request != "off" and user_request != "report":
        user_drink = menu.find_drink(user_request)
        if coffee_maker.is_resource_sufficient(user_drink) and money_machine.make_payment(user_drink.cost):
            coffee_maker.make_coffee(user_drink)
        run_machine()
    elif user_request == "report":
        coffee_maker.report()
        money_machine.report()
        run_machine()


# Code starts here
run_machine()