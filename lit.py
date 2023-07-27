# uses CCXT to fetch_ticker for BTC/USDT from Kucoin, as well as orderbook and OHLCV data.
# Plots OHLCV and orderbook data using mplfinance, and creates a dataframe with the fetch_ticker data.
# Includes all this visual data in a Streamlit app, along with a button to refresh data, dataframe, and plots


import ccxt
import streamlit as st
import pandas as pd
import mplfinance as mpf
import seaborn as sns
import matplotlib.pyplot as plt


# Constants TODO: make these user inputs
COIN = "BTC/USDT"
EXCHANGE_ID = "kucoin"
OHLCV_TIMEFRAME = "5m"

# fetch data from CCXT
exchange = eval(f"ccxt.{EXCHANGE_ID}()")
exchange.load_markets()
ticker_data = exchange.fetch_ticker(COIN)
orderbook_data = exchange.fetch_order_book(COIN)
ohlcv_data = exchange.fetch_ohlcv(COIN, timeframe=OHLCV_TIMEFRAME)

# organize ticker data
ticker_data.pop("info")
ticker_df = pd.DataFrame.from_dict([ticker_data])

# organize orderbook data
bids = orderbook_data["bids"]
asks = orderbook_data["asks"]
n = 20  # "zoom in" on the closest n bids/asks
bids = bids[:n]
asks = asks[:n]
bids_df = pd.DataFrame(bids, columns=["Price", "Amount"])
asks_df = pd.DataFrame(asks, columns=["Price", "Amount"])
orderbook_df = pd.concat([bids_df, asks_df])
midpoint = (bids[0][0] + asks[0][0]) / 2
spread = (asks[0][0] - bids[0][0]) / midpoint * 100

# organize OHLCV data
ohlcv_df = pd.DataFrame(
    ohlcv_data, columns=["Timestamp", "Open", "High", "Low", "Close", "Volume"]
)
ohlcv_df["Timestamp"] = pd.to_datetime(ohlcv_df["Timestamp"], unit="ms")
ohlcv_df.set_index("Timestamp", inplace=True)


# layout the streamlit app
st.set_page_config(layout="wide")
st.sidebar.title("Abacus (alpha)")
st.sidebar.write(f"Exchange: {EXCHANGE_ID.capitalize()}")
st.sidebar.write(f"Market: {COIN}")
st.sidebar.button("Refresh Data")
c1, c2 = st.columns([1, 1])

with c1:
    c11, c12, c13 = st.columns([1, 1, 1])
    # display the ticker, bid, and ask dataframes
    with c11:
        st.write("Ticker Data")
        st.write(ticker_df.T)
    with c12:
        st.write(f"top {n} bids")
        st.write(bids_df)
    with c13:
        st.write(f"top {n} asks")
        st.write(asks_df)

    # plot orderbook depth chart
    fig, ax = plt.subplots()
    ax.set_title(f"{COIN} Orderbook ({n} best bids/asks)")
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
    annotation_y = max(sum(bids_df["Amount"]), sum(asks_df["Amount"])) * 0.85
    ax.annotate(
        f"Midpoint: {midpoint:.2f}\nSpread: {spread}%",
        xy=(midpoint, annotation_y),
        xytext=(midpoint + 0.1, annotation_y),
        xycoords="data",
        textcoords="data",
    )

    # display the depth plot
    st.write("Orderbook Depth Chart")
    st.pyplot(fig)

    # OHLCV plot
    st.write(f"Open-High-Low-Close-Volume Candles ({OHLCV_TIMEFRAME})")
    candlefig, candleax = mpf.plot(
        ohlcv_df,
        type="candle",
        mav=5,
        volume=True,
        style="yahoo",
        returnfig=True,
    )
    st.write(candlefig)

    # OHLCV dataframe (optional)
    with st.expander("Show OHLCV Data"):
        st.write(ohlcv_df)
