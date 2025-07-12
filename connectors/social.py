import requests
from config import TWITTER_BEARER_TOKEN

class TwitterConnector:
    def search_tweets(self, query: str, max_results: int = 100) -> list:
        if not TWITTER_BEARER_TOKEN or TWITTER_BEARER_TOKEN == "YOUR_KEY_HERE":
            return None # Don't try if key is missing

        url = "https://api.twitter.com/2/tweets/search/recent"
        headers = {"Authorization": f"Bearer {TWITTER_BEARER_TOKEN}"}
        params = {"query": f"{query} -is:retweet lang:en", "max_results": max_results}
        try:
            response = requests.get(url, headers=headers, params=params, timeout=10)
            response.raise_for_status()
            return response.json().get('data', [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching tweets: {e}")
            return None # Return None on failure