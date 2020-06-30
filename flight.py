import requests
from lxml import html
from bs4 import BeautifulSoup
from selenium import webdriver


origin_code = input("TYPE YOUR AIRPORT CODE HERE:") #origin code
start_date = input("TYPE YOUR DATE HERE (FORMAT:YYYY-MM-DD):") #flight date
end_date = input("TYPE YOUR END DATE HERE OR PRESS ENTER FOR ONE WAY (FORMAT:YYYY-MM-DD):") #end date

 # note that the import package command is `bs4`

driver = webdriver.Chrome("/Users/kellylynch/Downloads/chromedriver")
driver.get(f"https://skiplagged.com/flights/{origin_code}/{start_date}/{end_date}")
soup = BeautifulSoup(driver.page_source, "lxml")

# alllist = soup.find("section", id="trip-list-skipsy-wrapper", class_="skipsy-container").find_all("li")
# price_list = alllist.find_all("div", class_="skipsy-cost")
# price_item = price_list.text

# for flight in alllist:
#   print(flight.text)

alllist = soup.find("section", id="trip-list-skipsy-wrapper", class_="skipsy-container")

destinations = []
destination_list = alllist.find_all("h2")
for destination in destination_list:
    destinations.append(destination.text)

prices = []
prices_formatted_2 =[]
price_list = alllist.find_all("div", class_="skipsy-cost")
for price in price_list:
    prices.append(price.text.split("$"))
    prices_formatted = prices[-1][-1]
    prices_formatted_2.append(prices_formatted)

combined_d_p = list(zip(destinations, prices_formatted_2))[:20]
for elements in combined_d_p:
    print (elements)

driver.quit()

# alllist = soup.find("section", id="trip-list-skipsy-wrapper", class_="skipsy-container")
# destination_list = alllist.find_all("h2")
# price_list = alllist.find_all("div", class_="skipsy-cost")
# for destination in destination_list:
#     destination_text = destination.text
#     print(destination_text)
# for price in price_list:
#     price_text = price.text
#     print(price_text)


