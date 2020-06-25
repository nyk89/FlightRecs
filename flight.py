import requests
import os
from dotenv import load_dotenv

load_dotenv() 

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UK/GBP/en-GB/"

querystring = {"query":"Stockholm"}

headers = {
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    'x-rapidapi-key': "SKYSCANNER_API_KEY"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

api_key = os.environ.get("SKYSCANNER_API_KEY")