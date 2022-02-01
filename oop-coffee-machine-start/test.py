from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO 1: Print Report
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True
profit = 0

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}):")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_on = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


# TODO 2: Check resources sufficient?

# TODO 3: Process coins.

# TODO 4: Check Transaction successful?

# TODO 5: Make a Coffee.