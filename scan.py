import ccxt
import datetime
import time

exchange = ccxt.binance()
markets = exchange.load_markets()

for market in markets:
    if "USD" not in market:
        continue
    if "BUSD" in market:
        continue
    if ":" in market:
        continue

    close_price = 0
    since = int(time.mktime((datetime.datetime.utcnow() - datetime.timedelta(weeks=4)).timetuple()) * 1000)
    ohlcv = exchange.fetch_ohlcv(market, "1w", since)
    for period in ohlcv:
        if close_price > period[4]:
            break
        else:
            close_price = period[4]

    if close_price == period[4]:
        print(market)
