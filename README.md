/protocol-upgrade-monitor/
├── api/
│   ├── __init__.py
│   ├── main.py             # FastAPI server, API endpoints
│   └── mock_data.py        # Fallback data generator
├── connectors/
│   ├── __init__.py
│   ├── market.py           # CoinGecko API connector
│   └── social.py           # Twitter API connector
├── models/
│   ├── __init__.py
│   ├── sentiment.py        # Sentiment analysis model logic
│   └── volatility.py       # GARCH model logic
├── templates/
│   └── index.html          # Frontend UI
├── .env                      # API keys (local)
├── config.py                 # Configuration loader
├── requirements.txt          # Python dependencies
└── README.md                 # This file
