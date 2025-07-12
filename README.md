# Protocol Upgrade Monitor

![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)![Framework](https://img.shields.io/badge/Framework-FastAPI-green.svg)![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A high-performance, full-stack monitoring system that tracks blockchain network events, predicts market volatility and liquidity shifts, and provides execution guidance for trading strategies.

## Objective

This system connects to multiple data sources including blockchain APIs, social media feeds, and market data streams to provide a real-time risk assessment of protocol upgrades. The user can select a network, and the engine will analyze market and social data to produce a risk score and actionable recommendations.

## Core Features

-   **Multi-Network Support:** Analyze major networks like Ethereum, Polygon, and Arbitrum.
-   **Volatility Forecasting:** Uses a GARCH(1,1) model to predict short-term price volatility based on historical data.
-   **Sentiment Analysis:** Leverages a `transformers` model (DistilBERT) to analyze real-time social media sentiment from Twitter.
-   **Multi-Factor Risk Score:** Generates a single, easy-to-understand risk score (0-100) based on volatility and sentiment.
-   **Actionable Guidance:** Provides recommendations for portfolio rebalancing, execution timing, and risk mitigation.
-   **Modern UI:** A clean, responsive, three-panel user interface for controls and data visualization.
-   **Resilient Data Fetching:** **Includes a mock data fallback mode**, ensuring the application is fully functional and demonstrable even without live API keys.

## Tech Stack

-   **Backend:** Python 3.9+, FastAPI
-   **Machine Learning:** `arch` (for GARCH), `transformers` & `torch` (for Sentiment Analysis)
-   **Data Handling:** Pandas, NumPy
-   **Frontend:** HTML5, CSS3, Vanilla JavaScript
-   **Server:** Uvicorn (ASGI Server)


---

## Setup and Installation

Follow these steps to get the application running on your local machine.

### 1. Prerequisites

-   Python 3.9 or newer
-   `pip` package manager

### 2. Navigate to Project Directory

Open your terminal or command prompt and navigate to the project's root folder.

```bash
cd path/to/your/protocol-upgrade-monitor
```
### 3. Install requirements

```bash
pip install -r requirements.txt
```
### 4. Running the application

```bash
uvicorn api.main:app --reload
```
