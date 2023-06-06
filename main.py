base_currency = "USD" #base currency must be USD because it is included in the URL
target_currency = input("What currency do you want to exchange it to? ").upper()

import requests 

def get_exchange_rate(base_currency, target_currency):
  api_key = b737cf750c85f10fd181f880 #personal api key
  URL = "https://v6.exchangerate-api.com/v6/b737cf750c85f10fd181f880/latest/USD" #api key within the URL
  response = requests.get(URL)
  data = response.json()