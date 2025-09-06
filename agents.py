import datetime
import requests
from bs4 import BeautifulSoup

# Set API keys from keys.py (create it with NEWS_API, WEATHER_API)
from Keys import NEWS_API, WEATHER_API


# Simple functions to get data
def get_news(query):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("articles", [{"error": "No news found"}])
    return [{"error": "Failed to fetch news"}]


def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {"error": "Failed to fetch weather"}


def get_port_jam(port):
    session = requests.Session()
    login_url = "https://www.gocomet.com/login"
    login_data = {
        "email": "enter your email",
        "password": "enter your password",
    }  # Update with your GoComet login
    session.post(login_url, data=login_data)
    url = f"https://www.gocomet.com/real-time-port-congestion?port={port}"
    response = session.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        level = soup.find("p", class_="item-details-delay delay-low")
        return level.text if level else "Not found"
    return {"error": "Failed to fetch port data"}


# Main function to run tasks
# Main function to run tasks
def run_tasks():
    # Fetch data for Shanghai
    news = get_news("port congestion Shanghai electronics")
    weather = get_weather("Shanghai")
    port_jam = get_port_jam("Shanghai")

    # Combine results
    result = {
        "news": news,
        "weather": weather,
        "port_jam": port_jam,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST"),
    }

    # Print in a simple, readable way
    print("=== Shanghai Port Update ===")
    print(f"Date and Time: {result['timestamp']}")
    print("\nNews:")
    if news and isinstance(news, list) and news[0].get("error"):
        print("  - No specific news found. Check general supply chain updates.")
    else:
        for item in news[:1]:  # Show only the first news item for simplicity
            print(f"  - Title: {item.get('title', 'No title')}")
            print(f"  - Source: {item.get('source', {}).get('name', 'Unknown')}")
            print(f"  - Date: {item.get('publishedAt', 'No date')}")
            print(f"  - Link: {item.get('url', 'No link')}")

    print("\nWeather:")
    if weather.get("error"):
        print("  - Weather data not available.")
    else:
        temp_celsius = (
            weather["main"]["temp"] - 273.15
        )  # Convert from Kelvin to Celsius
        print(f"  - Temperature: {temp_celsius:.1f}°C")
        print(f"  - Condition: {weather['weather'][0]['description']}")
        print(f"  - Humidity: {weather['main']['humidity']}%")

    print("\nPort Jam Status:")
    if isinstance(port_jam, str) and (
        "error" in port_jam.lower() or port_jam == "Not found"
    ):
        print("  - Port jam data not available. Check login or website.")
    else:
        print(f"  - Delay: {port_jam}")

    # Save to file
    with open("port_data.txt", "a") as f:
        f.write(f"{result['timestamp']}: {result}\n")


# Run the script
if __name__ == "__main__":
    run_tasks()
