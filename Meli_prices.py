import requests

# Define the exchange rate for "dolar cripto"
exchange_rate = 0.011

# Argentina API URLs
samsung_arg_url = "https://api.mercadolibre.com/sites/MLA/search?q=Samsung%20Galaxy%20S23"
xiaomi_arg_url = "https://api.mercadolibre.com/sites/MLA/search?q=Xiaomi%20Note%2012"

# Mexico API URLs
samsung_mex_url = "https://api.mercadolibre.com/sites/MLM/search?q=Samsung%20Galaxy%20S23"
xiaomi_mex_url = "https://api.mercadolibre.com/sites/MLM/search?q=Xiaomi%20Note%2012"

# Send requests to the Argentina API URLs
samsung_arg_response = requests.get(samsung_arg_url)
xiaomi_arg_response = requests.get(xiaomi_arg_url)

# Send requests to the Mexico API URLs
samsung_mex_response = requests.get(samsung_mex_url)
xiaomi_mex_response = requests.get(xiaomi_mex_url)

# Check if the response status code is 200
if (samsung_arg_response.status_code == 200 and xiaomi_arg_response.status_code == 200 and
    samsung_mex_response.status_code == 200 and xiaomi_mex_response.status_code == 200):
    
    # Parse the JSON response to get the prices for the Samsung and Xiaomi phones in Argentina
    samsung_arg_data = samsung_arg_response.json()
    xiaomi_arg_data = xiaomi_arg_response.json()
    samsung_arg_prices = [result['price'] for result in samsung_arg_data['results']]
    xiaomi_arg_prices = [result['price'] for result in xiaomi_arg_data['results']]
    
    # Convert the prices from Argentine pesos to USD using the exchange rate
    samsung_arg_prices_usd = [price * exchange_rate for price in samsung_arg_prices]
    xiaomi_arg_prices_usd = [price * exchange_rate for price in xiaomi_arg_prices]
    
    # Parse the JSON response to get the prices for the Samsung and Xiaomi phones in Mexico
    samsung_mex_data = samsung_mex_response.json()
    xiaomi_mex_data = xiaomi_mex_response.json()
    samsung_mex_prices = [result['price'] for result in samsung_mex_data['results']]
    xiaomi_mex_prices = [result['price'] for result in xiaomi_mex_data['results']]
    
    # Convert the prices from Mexican pesos to USD using the exchange rate
    samsung_mex_prices_usd = [price * exchange_rate for price in samsung_mex_prices]
    xiaomi_mex_prices_usd = [price * exchange_rate for price in xiaomi_mex_prices]
    
    # Print the converted prices for the Samsung and Xiaomi phones in Argentina
    print("Samsung Galaxy S23 (Argentina):")
    print("Precio más alto:", max(samsung_arg_prices_usd), "USD")
    print("Precio más bajo:", min(samsung_arg_prices_usd), "USD")
    
    print("\nXiaomi Note 12 (Argentina):")
    print("Precio más alto:", max(xiaomi_arg_prices_usd), "USD")
    print("Precio más bajo:", min(xiaomi_arg_prices_usd), "USD")
    
    # Print the converted prices for the Samsung and Xiaomi phones in Mexico
    print("\nSamsung Galaxy S23 (Mexico):")
    print("Precio más alto:", max(samsung_mex_prices_usd), "USD")
    print("Precio más bajo:", min(samsung_mex_prices_usd), "USD")
    
    print("\nXiaomi Note 12 (Mexico):")
    print("Precio más alto:", max(xiaomi_mex_prices_usd), "USD")
    print("Precio más bajo:", min(xiaomi_mex_prices_usd), "USD")
    
    # Compare the prices of the Samsung and Xiaomi phones in Argentina and Mexico
    if max(samsung_arg_prices_usd) > max(samsung_mex_prices_usd):
        print("\nEl Samsung Galaxy S23 es más caro en Argentina que en México.")
        print("Diferencia de precio más alto:", max(samsung_arg_prices_usd) - max(samsung_mex_prices_usd), "USD")
    elif max(samsung_arg_prices_usd) < max(samsung_mex_prices_usd):
        print("\nEl Samsung Galaxy S23 es más caro en México que en Argentina.")
        print("Diferencia de precio más alto:", max(samsung_mex_prices_usd) - max(samsung_arg_prices_usd), "USD")
    else:
        print("\nEl Samsung Galaxy S23 tiene el mismo precio más alto en Argentina y México.")
        
    if min(xiaomi_arg_prices_usd) > min(xiaomi_mex_prices_usd):
        print("El Xiaomi Note 12 es más barato en México que en Argentina.")
        print("Diferencia de precio más bajo:", min(xiaomi_mex_prices_usd) - min(xiaomi_arg_prices_usd), "USD")
    elif min(xiaomi_arg_prices_usd) < min(xiaomi_mex_prices_usd):
        print("El Xiaomi Note 12 es más barato en Argentina que en México.")
        print("Diferencia de precio más bajo:", min(xiaomi_arg_prices_usd) - min(xiaomi_arg_prices_usd), "USD")
    else:
        print("El Xiaomi Note 12 tiene el mismo precio más bajo en Argentina y México.")
else:
    print("Error al obtener datos.")

