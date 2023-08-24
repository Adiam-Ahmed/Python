from dic import*

coffee_machine  = True
earnings = 0


def processor():
    global coffee_machine
    global earnings
    if user_request == "Off":
        coffee_machine = False
    if user_request == "report":
        for key, value in goods.items():
         if key == "Milk" or key =="Water":
            print(f"{key}:{value}ml")
         if key == "Coffee":
            print(f"{key}:{value}g")
         if key == "Money":
            print(f"{key}:${value}")
    if user_request == "espresso" or user_request == "latte" or user_request == "cappuccino":
        if "milk" in MENU[user_request]["ingredients"]:
            if MENU[user_request]["ingredients"]["milk"] > goods["Milk"]:
                print("Sorry there is not enough milk")
        if MENU[user_request]["ingredients"]["water"]>goods["Water"]:
            print("Sorry there is not enough water")
        elif MENU[user_request]["ingredients"]["coffee"]>goods["Coffee"]:
            print("Sorry there is not enough coffee")
        else:
            print("Please insert coins.")
            quarters = (int(input("how many quarters?: "))*0.25)
            dimes = (int(input("how many dimes?: "))*0.10)
            nickles = (int(input("how many nickles?: "))*0.05)
            pennies = (int(input("how many pennies?: "))*0.01)
            total = quarters+dimes+nickles+pennies
            if total >=  MENU[user_request]["cost"]:
                change = round((total - MENU[user_request]["cost"]),2)
                earnings +=round((total-change), 2)
                goods["Money"] = earnings
                if "milk" in MENU[user_request]["ingredients"]:
                    goods["Milk"] -= MENU[user_request]["ingredients"]["milk"]
                goods["Water"] -=MENU[user_request]["ingredients"]["water"]
                goods["Coffee"] -=MENU[user_request]["ingredients"]["coffee"]
                print(f"Here is ${change}  in change")
                print(f"Here is your {user_request}. Enjoy!")

            else:
                    print("Sorry that's not enough money. Money refunded.")


while coffee_machine :
    user_request = input("What would you like? (espresso/latte/cappuccino):")
    processor()
