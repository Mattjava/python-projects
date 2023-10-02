import menu

# Goals

# 3 Hot Flavors [1. Espresso, 2. Latte, 3. Cappuccino]

# Espresso - 50ml Water, 18g Coffee, $1.50
# Latte - 200ml Water, 24g Coffee, 150ml Milk, $2.50
# Cappuccino - 250ml Water, 24g Coffee, 100ml Milk $3.00

# Sets up the current resources of the machine.
current_resources = menu.resources
current_resources["money"] = 0.0

# The main function to be run.
def run_machine():
    total = 0
    user_coins = []
    user_request = input("What would you like? An espresso, a latte, or a cappuccino?\n")

    if user_request != "off" and user_request != "report":
        cost = menu.MENU[user_request]["cost"]
        ingredients = menu.MENU[user_request]

        print("Enter your coins.")
        user_coins.append(int(input("How many  quarters?: ")))
        user_coins.append(int(input("How many dimes?: ")))
        user_coins.append(int(input("How many nickels?: ")))
        user_coins.append(int(input("How many pennies?: ")))

        total = calculate_coins(user_coins)

        if total < cost:
            print("\nInsufficient coins. Your coins have been refunded. Please try again.\n")
            run_machine()
        else:
            if user_request != "espresso":
                used_milk = menu.MENU[user_request]["ingredients"]["milk"]
            used_water = menu.MENU[user_request]["ingredients"]["water"]
            used_coffee = menu.MENU[user_request]["ingredients"]["coffee"]

            if user_request == "latte":
                if check_resources(user_request):
                    print("Dispensing latte. Enjoy :)")
                    use_resources(used_water, used_milk, used_coffee, cost)
                    run_machine()
                else:
                    run_machine()
            elif user_request == "espresso":
                if check_resources(user_request):
                    print("Dispensing espresso. Enjoy! :)")
                    use_resources(used_water, 0, used_coffee, cost)
                    run_machine()
                else:
                    run_machine()
            elif user_request == "cappuccino":
                if check_resources(user_request):
                    print("Dispensing cappuccino. Enjoy! :)")
                    use_resources(used_water, used_milk, used_coffee, cost)
                    run_machine()
                else:
                    run_machine()

    elif user_request == "report":
        print_report(current_resources)
        run_machine()

# Calculate the total of the coins
def calculate_coins(coins):
    total = 0.0
    for i in range(coins[0]):
        total += 0.25
    for i in range(coins[1]):
        total += 0.1
    for i in range(coins[2]):
        total += 0.05
    for i in range(coins[3]):
        total += 0.01
    return total


# Prints the report
def print_report(current_report):
    print(current_report)


# Uses the current resources to make the drink.
def use_resources(water, milk, coffee, money):
    global current_resources
    current_resources["water"] += -water
    current_resources["milk"] += -milk
    current_resources["coffee"] += -coffee
    current_resources["money"] += money


# Checks if the machine has enough resources for the drink. Returns false if the requirements are not met along with printing an error about it.
def check_resources(drink):
    if current_resources["water"] < menu.MENU[drink]["ingredients"]["water"]:
        print("Not enough water. Please pick another drink.")
        print("Your money has been refunded")
        return False
    elif drink != "espresso" and current_resources["milk"] < menu.MENU[drink]["ingredients"]["milk"]:
        print("Not enough milk. Please pick another drink.")
        print("Your money has been refunded")
        return False
    elif current_resources["coffee"] < menu.MENU[drink]["ingredients"]["coffee"]:
        print("Not enough coffee. Please pick another drink.")
        print("Your money has been refunded")
        return False
    return True


# Code starts here


run_machine()
