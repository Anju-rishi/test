import requests
import pandas as pd
from config import COINGECKO_API_URL, COINGECKO_API_KEY

class CoinGeckoConnector:
    def get_market_chart(self, token_id: str, vs_currency: str, days: int) -> pd.DataFrame:
        url = f"{COINGECKO_API_URL}/coins/{token_id}/market_chart"
        params = {
            'vs_currency': vs_currency,
            'days': days,
            'interval': 'daily',
            'x_cg_demo_api_key': COINGECKO_API_KEY
        }
        try:
            # Add a timeout to prevent long waits
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            prices = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
            prices['timestamp'] = pd.to_datetime(prices['timestamp'], unit='ms')
            
            return prices.set_index('timestamp')
        except requests.exceptions.RequestException as e:
            print(f"Error fetching CoinGecko data: {e}")
            return None # Return None on failure