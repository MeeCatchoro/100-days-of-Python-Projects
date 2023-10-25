from data import MENU, resources

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0.0


def report():
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


def make_beverage(beverage):
    global water, milk, coffee, money
    required_water = MENU[beverage]["ingredients"]["water"]
    required_milk = MENU[beverage]["ingredients"]["milk"]
    required_coffee = MENU[beverage]["ingredients"]["coffee"]
    cost = MENU[beverage]["cost"]

    if water < required_water:
        print("Sorry, not enough water.")
    elif coffee < required_coffee:
        print("Sorry, not enough coffee.")
    elif milk < required_milk:
        print("Sorry, not enough milk.")
    else:
        if pay(cost):
            water -= required_water
            milk -= required_milk
            coffee -= required_coffee
            money += cost
            print(f"Here is your {beverage}. Enjoy!")


def pay(cost):
    print(f"Total: ${cost}. Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies?"))
    coins = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if coins < cost:
        print("Sorry, that\'s not enough money. Money refunded")
        return False
    elif coins > cost:
        change = round(coins - cost, 2)
        print(f"Here is ${change} in change.")
    return True


is_on = True
while is_on:
    request = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if request == "report":
        report()
    elif request == "off":
        is_on = False
    else:
        make_beverage(request)



