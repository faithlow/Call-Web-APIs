

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
      
