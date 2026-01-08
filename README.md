# Stock Market Visualizer

A desktop application that allows users to search stock symbols and visualize historical closing price data using a real-time financial API.

## Tech Stack
- Python
- Flet (UI framework)
- Alpha Vantage API
- REST APIs
- Environment-based configuration

## Features
- Search stock symbols and retrieve historical price data
- View Open, High, Low, and Close prices
- Selectable time ranges (1week to 5 years)
- Interactive line chart visualization
- Graceful handling of API errors and rate limits

## Project Architecture
- UI layer built with Flet
- API logic isolated in a service module
- Secure environment variable configuration

## Setup Instructions

```bash
git clone https://github.com/yourusername/stock-market-visualizer.git
cd stock-market-visualizer
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
