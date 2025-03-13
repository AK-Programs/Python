# Weather Program

# This script fetches and displays the current weather information for a specified city.
# Usage:
# 1. Run the script.
# 2. Enter the city name when prompted.
# 3. The script will display the temperature, weather description, humidity, and wind speed.
# 4. You can choose to check the weather for another city or exit the program.
# 5. Don't forget to replace 'your_api_key_here' with your OpenWeatherMap API key.

import requests  
import time


def get_weather(city_name, api_key):  
    while True:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"  
        
        response = requests.get(url)  

        if response.status_code == 200:  
            data = response.json()  

            temperature = data['main']['temp']  
            weather_description = data['weather'][0]['description']  
            humidity = data['main']['humidity']  
            wind_speed = data['wind']['speed']  

            print(f"Gathering weather information for {city_name}...")
            time.sleep(2)
            print(f"Weather in {city_name}:")  
            time.sleep(1)
            print(f"Temperature: {temperature} °C")  
            time.sleep(1)
            print(f"Description: {weather_description}")  
            time.sleep(1)
            print(f"Humidity: {humidity}%")  
            time.sleep(1)
            print(f"Wind Speed: {wind_speed} m/s")  
        else:  
            print("City not found or API request unsuccessful.")  
            
        time.sleep(1)
        next = input("Would you like to try again? (yes/no): ")
        if next == "yes":
            city_name = input("Enter the city name: ")
        else:
            print("Exiting the program...")
            time.sleep(1)
            break

if __name__ == "__main__":  
    city_name = input("Enter the city name: ")  
    api_key = "your_api_key_here"
    get_weather(city_name, api_key)