from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
is_on = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_on:
    options = menu.get_items()
    choise = input(f"What would you like? ({options}):")
    if choise == "off":
        is_on = False
    elif choise == "report":
        coffee_maker.report()
        money_machine.report()


