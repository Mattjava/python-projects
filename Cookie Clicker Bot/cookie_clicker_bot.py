import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Sets the timeout time to be 30 minutes from now.
timeout = time.time() + 60*30

# Sets up the driver and gets the website.
cookie_driver = webdriver.Firefox()
cookie_driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Stores the cookie element and the store element into separate variables
cookie = cookie_driver.find_element(By.ID, value="cookie")
store = cookie_driver.find_element(By.ID, value="store")

# Extracts the items in the store and sets up the dictionary
items_list = store.text.split("\n")[::2]
item_dictionary = {}

# Seperates the item's name and price and use them to create a key and value in item_dictionary
for item in items_list:
    item = item.split(" - ")
    number = item[len(item) - 1].replace(",", "")
    item_dictionary[item[0]] = int(number)


# Sets up Cookie per seconds, or what will be printed when the for loop ends
cps = ""

# Calculates the time 5 seconds from now.
future_time = time.time() + 5.00

# Determines which item is the most expensive with the current amount of money.
# After choosing, it automatically buys it.
def buy_upgrade(money):
    max = "Cursor"
    for item in item_dictionary:
        if (money >= item_dictionary[item]) and item_dictionary[item] > item_dictionary[max]:
            max = item
    chosen_item = cookie_driver.find_element(By.ID, value=f"buy{max}")
    chosen_item.click()

# The main for loop that will run the game.
while True:
    # Determines if the set amount of time has passed.
    # If so, it will grab the cps, assign it to the cps variable, and break the loop
    if time.time() >= timeout:
        cps = cookie_driver.find_element(By.ID, "cps").text
        break

    # Scrapes the current amount of money right now.
    current_money = int(cookie_driver.find_element(By.ID, value="money").text.replace(",", ""))

    # Checks if 5 seconds has passed.
    # If so, it will run buy_upgrade with current_money.
    # It will also set future_time to the next time 5 seconds from now.
    if time.time() >= future_time:
        buy_upgrade(current_money)
        future_time = time.time() + 5.00

    # Automatically clicks the cookie.
    cookie.click()

# Shuts down the driver.
cookie_driver.close()

# Prints the cps when the loop breaks.
print(cps)



