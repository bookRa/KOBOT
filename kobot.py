import ccxt
import os
import openai
from dotenv import load_dotenv
import json 

load_dotenv()

openai.organization = "org-VAzYa2yfTTttUMNvCBhluUKn"
openai.api_key = os.getenv("OPENAI_API_KEY")
# print(openai.Model.list())

# instantiate ccxt connector to kucoin exchange and get orderbook data
exchange = ccxt.kucoin()
exchange.load_markets()

TICKERS_WE_LIKE = [
    'BTC/USDT', 
    'ADA/USDT' ]

all_my_tickers = exchange.fetch_tickers(TICKERS_WE_LIKE)

print(json.dumps(all_my_tickers, indent=4))