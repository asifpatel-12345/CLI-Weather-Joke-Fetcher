import requests
import sys

def get_random_joke():
    print("\nfetching a random joke for you... 🤖")
    # Public Joke API
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"\n😂 {data['setup']}")
            print(f"👉 {data['punchline']}\n")
        else:
            print("❌ Failed to fetch joke. Try again later.")
    except requests.exceptions.RequestException:
        print("❌ Network Error! Please check your internet connection.")

def get_weather():
    city = input("\nEnter city name for weather: ").strip()
    if not city:
        print("❌ City name cannot be empty!")
        return

    print(f"\nFetching live weather for {city}... 🌤️")
    
    # Using wttr.in (Free open-source weather API which doesn't require an API key)
    url = f"https://wttr.in/{city}?format=j1"
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            current = data['current_condition'][0]
            temp_c = current['temp_C']
            desc = current['weatherDesc'][0]['value']
            humidity = current['humidity']
            windspeed = current['windspeedKmph']

            print(f"\n🌍 Weather Report for: {city.capitalize()}")
            print(f"🌡️  Temperature : {temp_c}°C")
            print(f"☁️  Condition   : {desc}")
            print(f"💧 Humidity    : {humidity}%")
            print(f"🌬️  Wind Speed  : {windspeed} km/h\n")
        else:
            print("❌ City not found or unable to fetch weather data.")
    except requests.exceptions.RequestException:
        print("❌ Network Error! Please check your internet connection.")

def main():
    while True:
        print("========================================")
        print(" 🌤️  CLI WEATHER & JOKE FETCHER TOOL 🤖 ")
        print("========================================")
        print("1. Get Live Weather")
        print("2. Get a Random Joke")
        print("3. Exit")
        
        choice = input("\nChoose an option (1-3): ").strip()
        
        if choice == '1':
            get_weather()
        elif choice == '2':
            get_random_joke()
        elif choice == '3':
            print("\nExiting... Have a great day! 👋\n")
            sys.exit()
        else:
            print("❌ Invalid choice! Please select 1, 2, or 3.\n")

if __name__ == "__main__":
    main()