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
    # 'BTC/USDT', 
    'ADA/USDT' ]
output_json =  { foo: {} for foo in TICKERS_WE_LIKE}
print(output_json)
for ticker in TICKERS_WE_LIKE:
    print(f"TICKER is {ticker}")
   
    # Orderbook data
    # orderbook = exchange.fetch_order_book(ticker)
    # print("------ ORDER BOOK ---")
    # # print(json.dumps(orderbook, indent=4))
    # output_json[ticker]['orderbook'] = orderbook
    # print(json.dumps(output_json, indent=4))
   
    # # Ticker data
    ticker_info = exchange.fetch_ticker(ticker)
    print("------ HIGH_LEVEL_TICKER_INFO ---")
    # print(json.dumps(orderbook, indent=4))
    output_json[ticker]['ticker_info'] = ticker_info

    # # Candlestick data
    # TODO: candlesticks add too many tokens
    # candlestick_data = exchange.fetch_ohlcv(ticker, '1d')
    # print("------ CANDLESTICK_DATA ---")
    # # print(json.dumps(candlestick_data, indent=4))
    # output_json[ticker]['candlestick_data'] = candlestick_data

output_name = 'market_data_LIVE.json'
# output_name = 'market_data_TRAINING.json'
# output to json file
with open(output_name, 'w') as outfile:
    json.dump(output_json, outfile)

