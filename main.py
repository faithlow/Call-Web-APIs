import requests 

def get_exchange_rate(base_currency, target_currency):
  api_key = "b737cf750c85f10fd181f880" #personal api key
  URL = "https://v6.exchangerate-api.com/v6/" + api_key + "/latest/" + base_currency #api key within the URL
  response = requests.get(URL)
  
  data = response.json()
  if response.status_code == 200:
      if target_currency in data["conversion_rates"]:
        exchange_rate = data["conversion_rates"][target_currency]
        return exchange_rate
      else:
        return None
  else:
      return None
    

if __name__ == '__main__': #start of program execution
  user_base_currency = input("What currency do you want to convert from: ").upper() #base currency must be USD because it is included in the URL
  user_target_currency = input("What currency do you want to exchange it to? Please write 3 letter abbreviation for desired currency you want to exchange USD into: ").upper()
  user_amount = input("How much " + user_base_currency + " do you want to exchange to " + user_target_currency + ": ")
  exchange_rate = get_exchange_rate(user_base_currency, user_target_currency)
  if exchange_rate is not None:
    print(f"1 {user_base_currency} = {exchange_rate} {user_target_currency}")
    exchange_amount = float(user_amount) * exchange_rate
    exchange_amount_2_decimal = "{:.2f}".format(exchange_amount)
    print(f"For {user_amount} {user_base_currency} , you can exchange to {exchange_amount_2_decimal} {user_target_currency}")
  else: 
    print ("Failed to fetch exchance rate between " + user_base_currency + " to " + user_target_currency +".")
      
