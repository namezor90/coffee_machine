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

c_coins = {
    "quarter": 10,
    "dimes": 10,
    "nickel": 10,
    "pennies": 10,
}


def check_resources(resources, MENU, choice):
    r_water = resources["water"]
    r_milk = resources["milk"]
    r_coffee = resources["coffee"]
    water = MENU[choice]["ingredients"]["water"]
    milk = MENU[choice]["ingredients"].get("milk", 0)
    coffee = MENU[choice]["ingredients"]["coffee"]

    if r_water > water and r_milk > milk and r_coffee > coffee:
        succes = True
    else:
        succes = False
    return succes


def report_resources(resources):
    r_water = resources["water"]
    r_milk = resources["milk"]
    r_coffee = resources["coffee"]
    return f"Water: {r_water} \nMilk: {r_milk} \nCoffee: {r_coffee}"


def report_coins(c_coins):
    quarter = c_coins["quarter"]
    dimes = c_coins["dimes"]
    nickel = c_coins["nickel"]
    pennies = c_coins["pennies"]

    return (f"Quarter: {quarter} pieces in total: ${quarter*0.25} \n"
            f"Dimes: {dimes} pieces in total: ${dimes*0.10} \n"
            f"Nickel: {nickel} pieces in total: ${nickel*0.05} \n"
            f"Pennies: {pennies} pieces in total: ${pennies*0.01}")


def making_coffee(succes, MENU, choice):
    r_water = resources["water"]
    r_milk = resources["milk"]
    r_coffee = resources["coffee"]
    water = MENU[choice]["ingredients"]["water"]
    milk = MENU[choice]["ingredients"].get("milk", 0)
    coffee = MENU[choice]["ingredients"]["coffee"]

    if succes is True:
        resources["water"] = r_water - water
        resources["milk"] = r_milk - milk
        resources["coffee"] = r_coffee - coffee
        succes = True
    elif succes is False:
        print("Sorry, the coffee was not made.")
        succes = False
    return succes


def making_coins(succes, MENU, choice, c_coins):
    print("Coins!")
    quarter = float(input("Quarter:"))
    dimes = float(input("Dimes:"))
    nickel = float(input("Nickel:"))
    pennies = float(input("Pennies:"))

    full_coins = (quarter*0.25) + (dimes*0.10) + (nickel*0.05) + (pennies*0.01)
    cost = MENU[choice]["cost"]

    if cost < full_coins:
        c_coins["quarter"] = quarter
        c_coins["dimes"] = dimes
        c_coins["nickel"] = nickel
        c_coins["pennies"] = pennies
        full_coins -= cost
        print("Coffee made!")
    elif cost > full_coins:
        print("Sorry, the coffee was not made.")

    return full_coins

def recurring(making_coins):
    amount = making_coins

    quarters = amount // 0.25
    amount = round(amount % 0.25, 2)  # maradékot kerekítjük a következő lépéshez

    dimes = amount // 0.10
    amount = round(amount % 0.10, 2)

    nickels = amount // 0.05
    amount = round(amount % 0.05, 2)

    pennies = amount // 0.01
    amount = round(amount % 0.01, 2)
    return f"Quarters: {quarters}, Dimes: {dimes}, Nickels: {nickels}, Pennies: {pennies}"


def progress(resources, MENU, choice, c_coins):
    succes = check_resources(resources, MENU, choice)
    if succes:
        succes = making_coffee(succes, MENU, choice)
        if succes:
            full_coins = making_coins(succes, MENU, choice, c_coins)
            print(recurring(full_coins))
        else:
            print("Sorry, the coffee was not made.")
    else:
        print("Sorry, the coffee was not made.")

def menu():
    on = True
    while on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "report1":
            print(report_resources(resources))
        elif choice == "report2":
            print(report_coins(c_coins))
        elif choice == "latte" or choice == "espresso" or choice == "cappuccino":
            progress(resources=resources, MENU=MENU, choice=choice, c_coins=c_coins)
        elif choice == "off":
            print("Thank you!")
            on = False


if __name__ == '__main__':
    menu()
