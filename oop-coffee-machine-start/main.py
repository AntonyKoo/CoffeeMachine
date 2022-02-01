from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO 1 : Print Report.
# resources & money
coffee_maker = CoffeeMaker()  # Initialize the Class
money_machine = MoneyMachine()  # Initialize the Class
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like?( {options}): ")
    if choice == "off":
        is_on = False
    elif choice =="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)  # drink == MenuItem(), it means name/cost/ingredients
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

            # This method returns T/F value.
            # if the method above is True, this line works.


# TODO 2 : Check resources sufficient?

# TODO 3 : Process coins.

# TODO 4 : Check Transaction successful?

# TODO 5 : Make a Coffee.

