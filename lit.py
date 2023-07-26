# uses CCXT to fetch_ticker for BTC/USDT from Kucoin, as well as orderbook and OHLCV data.
# Plots OHLCV and orderbook data using mplfinance, and creates a dataframe with the fetch_ticker data.
# Includes all this visual data in a Streamlit app, along with a button to refresh data, dataframe, and plots


import ccxt
import streamlit as st
import pandas as pd
import mplfinance as mpf
import seaborn as sns
import matplotlib.pyplot as plt


kc = ccxt.kucoin()
kc.load_markets()

BTC = "BTC/USDT"

# setup ticker data and plot
ticker_data = kc.fetch_ticker(BTC)
ticker_data.pop("info")
ticker_df = pd.DataFrame.from_dict([ticker_data])

# display the ticker df in streamlit
st.title("Kucoin Data")
st.write("Ticker Data")
st.write(ticker_df)

# setup orderbook data and depth plot
orderbook_data = kc.fetch_order_book(BTC)
bids = orderbook_data["bids"]
asks = orderbook_data["asks"]
n = 20
# "zoom in" on the orderbook data to show the bid/ask spread and the closest n bids/asks
bids = bids[:n]
asks = asks[:n]
bids_df = pd.DataFrame(bids, columns=["Price", "Amount"])
bids_df["Type"] = "bid"
asks_df = pd.DataFrame(asks, columns=["Price", "Amount"])
asks_df["Type"] = "ask"
orderbook_df = pd.concat([bids_df, asks_df])

# calculate the midpoint and the bid/ask spread (as a percentage with two significant digits)
midpoint = (bids[0][0] + asks[0][0]) / 2
spread = (asks[0][0] - bids[0][0]) / midpoint * 100

fig, ax = plt.subplots()
ax.set_title(f"{BTC} Orderbook ({n} best bids/asks)")
sns.ecdfplot(
    x="Price",
    weights="Amount",
    stat="count",
    complementary=True,
    color="green",
    data=bids_df,
    ax=ax,
)
sns.ecdfplot(
    x="Price", weights="Amount", stat="count", color="red", data=asks_df, ax=ax
)

# annotate the ecdfplot with the midpoint and spread
ax.axvline(midpoint, color="black", linestyle="--")
ax.annotate(
    f"Midpoint: {midpoint:.2f}\nSpread: {spread}%",
    xy=(midpoint, 0.5),
    xytext=(midpoint + 0.1, 3.5),
    xycoords="data",
    textcoords="data",
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3"),
)

# display the depth plot in streamlit
st.write("Orderbook Data")
st.pyplot(fig)


# ohlcv_data = kc.fetch_ohlcv(BTC)

# # Create exchange object
# exchange = ccxt.kucoin()
# exchange.load_markets()

# # Create ticker dataframe
# ticker_info = exchange.fetch_ticker("ADA/USDT")
# ticker_df = pd.DataFrame(ticker_info)

# # Create orderbook dataframe
# orderbook = exchange.fetch_order_book("ADA/USDT")
# orderbook_df = pd.DataFrame(orderbook)

# # Create OHLCV dataframe
# ohlcv = exchange.fetch_ohlcv("ADA/USDT")
# ohlcv_df = pd.DataFrame(
#     ohlcv, columns=["Timestamp", "Open", "High", "Low", "Close", "Volume"]
# )

# # Create streamlit app
# st.title("Kucoin Data")
# st.write("Ticker Data")
# st.write(ticker_df)
# st.write("Orderbook Data")
# st.write(orderbook_df)
# st.write("OHLCV Data")
# st.write(ohlcv_df)
