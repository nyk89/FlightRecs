import requests
from bs4 import BeautifulSoup


origin_code = input("TYPE YOUR AIRPORT CODE HERE:") #origin code
start_date = input("TYPE YOUR DATE HERE (FORMAT:YYYY-MM-DD):") #flight date
end_date = input("TYPE YOUR END DATE HERE (FORMAT:YYYY-MM-DD):")

 # note that the import package command is `bs4`

response = requests.get(f"https://skiplagged.com/flights/{origin_code}/{start_date}/{end_date}")
response_html = response.text

# soup = BeautifulSoup(response_html)

# titles = soup.find_all("span", "title")

# print(type(titles)) #> <class 'bs4.element.ResultSet'> (like a list)
# print(titles[5]) #> <span class="title">Macbeth</span>
# print(titles[5].text) #> Macbeth

# booklinks = soup.find_all("li", "booklink")

# books = []
# for list_item in booklinks:
#     title = list_item.find("span", "title").text #> "Shakespeare's Sonnets"
#     author = list_item.find("span", "subtitle").text #> "William Shakespeare"
#     downloads = list_item.find("span", "extra").text #> '830 downloads'
#     downloads_count = int(downloads.replace(" downloads", "")) #> 830
#     book = {"title": title, "author": author, "downloads": downloads_count}
#     print(book)
#     books.append(book)

# print(books[2]["title"]) #> Macbeth
