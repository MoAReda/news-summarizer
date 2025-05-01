import requests
from dotenv import load_dotenv
import os
load_dotenv()
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

def fetch_news(topic, timeframe="24 hours"):
    """
    Fetch news articles from NewsAPI based on a topic and timeframe.
    """
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": topic,
        "from": timeframe,  # Adjust based on user input
        "sortBy": "publishedAt",
        "apiKey": NEWSAPI_KEY,
        "pageSize": 5  # Limit the number of articles
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()["articles"]
    else:
        print("Failed to fetch news:", response.status_code)
        return []