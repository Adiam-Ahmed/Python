from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine= MoneyMachine()
menu = Menu()

is_on = True 

while is_on:
    option = input(f"What would you like? ({menu.get_items()})")
    if option == "no":
        is_on= False
    elif option == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(option)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)



