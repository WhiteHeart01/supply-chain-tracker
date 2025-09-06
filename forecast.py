import pandas as pd
from darts import TimeSeries
from darts.models import ExponentialSmoothing
import datetime

# Fake historical data (add real from agents)
data = {
    "date": [datetime.date(2025, 8, 1), datetime.date(2025, 8, 2), ...],
    "jam_level": [5, 7, ...],
}  # 1-10 scale from news/weather
df = pd.DataFrame(data)
series = TimeSeries.from_dataframe(df, "date", "jam_level")

# Model (light, runs on your CPU)
model = ExponentialSmoothing()
model.fit(series)
prediction = model.predict(3)  # 3 days ahead

print("Next 3 days jam guess:", prediction.values())
