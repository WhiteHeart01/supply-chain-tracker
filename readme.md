# Supply Chain Tracker

Welcome to the Supply Chain Tracker! This simple tool helps track port conditions to avoid shipping delays and save money. It checks news, weather, and port jam status for Shanghai, a key hub for electronics shipments.

## What It Does
- **News**: Finds recent news about port congestion or supply chain issues.
- **Weather**: Shows the current weather in Shanghai to spot delays from bad conditions.
- **Port Jam**: Checks how long ships might be delayed at Shanghai port (if data is available).

## How It Works
The tool runs a Python script (`agents.py`) that:
- Uses free APIs for news and weather.
- Scrapes port data from GoComet (needs login).
- Saves results to a file (`port_data.txt`) and prints them in an easy format.

## Requirements
- **Linux Operating System** (this project is built for Linux).
- **Python 3.10** (with Anaconda environment `supply_chain`).
- **Packages**: Install these with `pip`:

- **API Keys**: Create a `keys.py` file with:
NEWS_API = "your_news_api_key"
WEATHER_API = "your_weather_api_key"

##Example Output


=== Shanghai Port Update ===
Date and Time: 2025-09-03 17:29:35 IST

News:
  - Title: Michael Rastiello Discusses Global Supply Chain Disruptions
  - Source: International Business Times
  - Date: 2025-08-29T19:51:30Z
  - Link: https://www.ibtimes.com/...

Weather:
  - Temperature: 27.8°C
  - Condition: broken clouds
  - Humidity: 80%

Port Jam Status:
  - __________________________
  - or 
  - --
  -Port jam data not available. Check login or website.

####Notes

Port Jam Fix: If "Not found" shows, update login_data in agents.py with your GoComet email and password. Check the website’s HTML for the correct tag.
Security: Add keys.py to .gitignore to keep API keys safe (already included).

#Contributing
Feel free to suggest improvements or fix issues by forking this repo and submitting a pull request!
