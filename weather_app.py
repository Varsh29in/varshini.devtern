import requests

# Replace with your actual API key
API_KEY = '9651cb04b9497c195585d055e1a513ba'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

def get_weather(city):
    """Fetch the weather for a given city."""
    # Construct the final URL
    url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
    
    # Make a GET request to fetch the raw HTML content
    response = requests.get(url)
    
    # If the response was successful, no Exception will be raised
    response.raise_for_status()
    
    # Parse the JSON data
    data = response.json()
    
    if data["cod"] != "404":
        main = data["main"]
        weather_desc = data["weather"][0]["description"]
        temperature = main["temp"]
        humidity = main["humidity"]
        wind_speed = data["wind"]["speed"]
        
        weather_info = (
            f"City: {city}\n"
            f"Temperature: {temperature}°C\n"
            f"Weather Description: {weather_desc}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s\n"
        )
        return weather_info
    else:
        return "City not found."

def main():
    while True:
        city = input("Enter city name (or type 'exit' to quit): ")
        if city.lower() == 'exit':
            print("Goodbye!")
            break
        try:
            weather_info = get_weather(city)
            print(weather_info)
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            print("Please check your network connection and try again.")

if __name__ == "__main__":
    main()
