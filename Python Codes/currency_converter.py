# Currency Converter

# This script allows users to convert an amount from one currency to another using real-time exchange rates.
# It fetches the exchange rates from the ExchangeRate-API.
# 
# Usage:
# 1. Make sure you have Python installed on your system.
# 2. Install the 'requests' library by running the following command in your terminal:
#    pip install requests
# 3. Run the script and follow the on-screen instructions to perform currency conversions.
#
# Note: Replace the 'api_key' variable with your own API key from ExchangeRate-API.

import requests

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"  
    response = requests.get(url)
    if response.status_code != 200:  
        print("Error fetching data from the API.")  
        return None  
    
    data = response.json()  
    if target_currency in data['conversion_rates']:  
        return data['conversion_rates'][target_currency]  
    else:  
        print(f"Currency '{target_currency}' is not available.")  
        return None  

def currency_converter():  
    api_key = "40d18e4782ece74b4d5ae9ee"  
    print("Welcome to the Currency Converter!")  
    
    while True:
        base_currency = input("Enter the base currency (e.g., USD, EUR): ").upper()  
        target_currency = input("Enter the target currency (e.g., USD, EUR): ").upper()  
        exchange_rate = get_exchange_rate(api_key, base_currency, target_currency)  
        
        if exchange_rate:  
            amount = float(input("Enter the amount you want to convert: "))  
            converted_amount = amount * exchange_rate  
            print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")  
            
        again = input("Do you want to convert another currency? (y/n): ").strip().lower()
        if again == "y":  
            continue
        else:  
            print("Thank you for using the Currency Converter!")
            break

if __name__ == "__main__":  
    currency_converter()