import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Keys
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")
COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# API Base URLs
COINGECKO_API_URL = "https://api.coingecko.com/api/v3"