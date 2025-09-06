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
```python
NEWS_API = "your_news_api_key"
WEATHER_API = "your_weather_api_key"