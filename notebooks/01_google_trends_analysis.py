from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

pytrends = TrendReq(hl='en-US', tz=360)

keywords = ["Netflix", "HBO", "Streaming services"]

pytrends.build_payload(keywords, cat=0, timeframe='2019-01-01 2024-12-31', geo='', gprop='')

data = pytrends.interest_over_time()
data = data.drop(columns=['isPartial'])

plt.figure(figsize=(12,6))
for col in data.columns:
    plt.plot(data.index, data[col], label=col)

plt.title("Google Search Interest Over Time")
plt.xlabel("Year")
plt.ylabel("Interest")
plt.legend()
plt.grid()
plt.show()
