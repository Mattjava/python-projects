from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

# Access the website and grabs it. It then converts the text into a soup.
website_text = requests.get(url="https://appbrewery.github.io/Zillow-Clone/").text

website_soup = BeautifulSoup(website_text, "html.parser")

# Obtains links from each of the listings.
links = website_soup.find_all(class_="property-card-link")
links = [link["href"] for link in links]

# Obtains prices for each of the listings.
prices = website_soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
prices = [price.text[:6] for price in prices]

# Obtains the addresses for each of the listings.
addresses = website_soup.find_all("address")
addresses = [address.text.strip("\n                                  ") for address in addresses]

# Creates a for-loop to create a form entry for each of the listings.


for i in range(len(links)):
    # Activates the webdriver
    form_driver = webdriver.Firefox()
    form_driver.get(url="https://docs.google.com/forms/d/e/1FAIpQLSd5Yvgi0BGP3HfQYkXKB_ma7K_Ua2nGA3-FZ0XuPs1iUUGT4A/viewform?usp=sf_link")

    # Stops the program for 7 seconds.
    # Allows the website to fully load before the driver inspects it.
    time.sleep(7)

    # Retrieves the address input and inserts the address (in which the variable i of the for loop indicates) into it.
    address_input = form_driver.find_element(By.CSS_SELECTOR, "div.Qr7Oae:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
    address_input.send_keys(addresses[i])

    # Retrieves the price input and inserts the price (in which the variable i of the for loop indicates) into it.
    price_input = form_driver.find_element(By.CSS_SELECTOR, "div.Qr7Oae:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
    price_input.send_keys(prices[i])

    # Retrieves the link input and inserts the link (in which the variable i of the for loop indicates) into it.
    link_input = form_driver.find_element(By.CSS_SELECTOR, "div.Qr7Oae:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
    link_input.send_keys(links[i])

    # Clicks on the submit button to submit the form.
    submit_button = form_driver.find_element(By.CSS_SELECTOR, ".Y5sE8d > span:nth-child(3)")
    submit_button.click()

    # Close the driver
    form_driver.close()

