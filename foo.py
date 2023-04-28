import ccxt


exchange = ccxt.kucoin()
exchange.load_markets()

ticker_info = exchange.fetch_ticker("ADA/USDT")

print(ticker_info)