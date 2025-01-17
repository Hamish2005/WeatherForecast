import requests
import os


API_KEY = "ce07f4e781a5b8f7a2b0ce65cf08caf5"

# Function to get weather data
def get_weather_data(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric" # Uses openweathermap
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch weather data (Status Code: {response.status_code})")
        return None

# Main program
if __name__ == "__main__":
    city_name = input("Enter the city name: ")
    weather_data = get_weather_data(city_name, API_KEY)

    if weather_data:
        print(f"Weather forecast for {city_name};")
        for forecast in weather_data["list"][:5]:  # Show the first 5 forecasts
            date = forecast["dt_txt"]
            temp = forecast["main"]["temp"]
            description = forecast["weather"][0]["description"]
            print(f"Date: {date}, Average temperature during the day: {temp}°C, Type of weather: {description}")
    else:
        print("Failed to fetch weather data.")
