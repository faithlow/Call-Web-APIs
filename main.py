base_currency = "USD" #base currency must be USD because it is included in the URL
target_currency = input("What currency do you want to exchange it to? Please write 3 letter abbreviation for desired currency you want to exchange USD into.").upper()

import requests 

def get_exchange_rate(base_currency, target_currency):
  api_key = b737cf750c85f10fd181f880 #personal api key
  URL = f"https://v6.exchangerate-api.com/v6/b737cf750c85f10fd181f880/latest/USD" #api key within the URL
  response = requests.get(URL)
  
  data = response.json()
  if response.status_code == 200:
      if target_currency in data["conversion_rates"]:
        exchange_rate = data["conversion_rate"]["target_currency"]
        return exchange_rate
      else:
        return None
  else:
      return None

exchange_rate = get_exchange_rate(base_currency, target_currency)
if exchange_rate is not None:
  print(f"1 {base_currency} = {exchange_rate} {target_currency}")
else: 
  print ("Failed to fetch exchance rate.")
      
