import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "Missing Alpha Vantage API Key. "
        "Create a .env file with your API Key. "
    )
