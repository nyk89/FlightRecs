import requests
from lxml import html
from bs4 import BeautifulSoup
from selenium import webdriver

# def to_usd(my_price):
#     return f"${my_price:,.2f}" #> $12,000.71

print("Welcome to Flight Recs for the cheapest deals from your city. Enter the airport code you want to travel from and the dates.")

#airport_codes = ["ATL", "LAX"] ORD, DFW, DEN, JFK, SFO, SEA, LAS, MCO, EWR, CLT, PHX, IAH, MIA, BOS, MSP, FLL, DTW, PHL, LGA, BWI, SLC, SAN, IAD, DCA, MDW, TPA, PDX]

# try:
origin_code = input("TYPE YOUR AIRPORT CODE HERE:") #origin code
    # if origin_code not in airport_codes:
    #     print("Hmmm, I don't think that's a valid code")
    # else:
    #     if origin_code.isdigit() and origin_code in airport_codes:
    #         origin_codes.append(origin_code)
    # break

start_date = input("TYPE YOUR DATE HERE (FORMAT:YYYY-MM-DD):") #flight date
end_date = input("TYPE YOUR END DATE HERE OR PRESS ENTER FOR ONE WAY (FORMAT:YYYY-MM-DD):") #end date

 # note that the import package command is `bs4`

driver = webdriver.Chrome("/Users/kellylynch/Downloads/chromedriver")
driver.get(f"https://skiplagged.com/flights/{origin_code}/{start_date}/{end_date}")
#driver.get("https://skiplagged.com/flights/JFK/2020-07-23/2020-07-30")
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

# prices_formatted_4 = []
# for price_2 in prices_formatted_2:
#     prices_formatted_3 = to_usd(float(prices_formatted_2)) 
#     prices_formatted_4.append(prices_formatted_3)
  
combined_d_p = list(zip(destinations, prices_formatted_2))[:20]
for elements in combined_d_p:
    print(elements)

print("Bon Voyage!")
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


