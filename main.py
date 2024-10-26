from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_menu = menu.get_items()

making_coffee = CoffeeMaker()

cha_ching = MoneyMachine()

machine_on = True

while machine_on:
    choice = input(f"What would you like? ({coffee_menu[:-1]}): ").lower().strip()
    coffee_choice = menu.find_drink(choice)

    if choice == "off":
        print("POWERING DOWN!!")
        machine_on = False
    elif choice == "report": 
        making_coffee.report()
        cha_ching.report()
    elif coffee_choice:
        check_resources = making_coffee.is_resource_sufficient(coffee_choice)
        if check_resources:
            money_input = cha_ching.make_payment(coffee_choice.cost)
            if money_input:
                making_coffee.make_coffee(coffee_choice)


