from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine





coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


is_on = True

while is_on:
    order = input(f"What coffee would you like? ({menu.get_items()}) ").lower()
    if order == "off":
        break
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)





