'''
Copyright (C) 2018-2020  Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
'''
from cryptofeed.backends.influxdb import TradeInflux, FundingInflux, BookInflux, BookDeltaInflux, TickerInflux
#from cryptofeed.callback import TickerCallback, TradeCallback, BookCallback, FundingCallback
from cryptofeed import FeedHandler
from cryptofeed.exchanges import Bitmex

from cryptofeed.defines import TRADES, FUNDING, L2_BOOK, BOOK_DELTA, TICKER, OPEN_INTEREST


def main():

    f = FeedHandler()
    f.add_feed(Bitmex(channels=[FUNDING, L2_BOOK,], pairs=['XBTUSD'], callbacks={FUNDING: FundingInflux('http://localhost:8086', 'example'), L2_BOOK: BookInflux('http://localhost:8086', 'example', numeric_type=float), BOOK_DELTA: BookDeltaInflux('http://localhost:8086', 'example', numeric_type=float)}))

    bitmex_symbols = Bitmex.get_active_symbols()

    f.add_feed(Bitmex(channels=[TRADES], pairs=bitmex_symbols, callbacks={TRADES: TradesInflux('http://localhost:8086', 'example', numeric_type=float)}))

    #cbs = {TRADES: TradesInflux(), L2_BOOK: BookKafka(), OPEN_INTEREST: OpenInterestKafka()}

    #bitmex_symbols = Bitmex.get_active_symbols()
    #f.add_feed(Bitmex(channels=[OPEN_INTEREST], pairs=['XBTUSD'], callbacks=cbs))
    #f.add_feed(Bitmex(channels=[TRADES], pairs=bitmex_symbols, callbacks=cbs))
    #f.add_feed(Bitmex(pairs=['XBTUSD'], channels=[FUNDING, TRADES], callbacks=cbs))

    """
    # Uncomment Here When Using InfluxDB 2.0
    # For InfluxDB 2.0, provide additional org, bucket(instead of db), token and precision(optional)
    # [Note] In order to use visualization and aggregation, numeric_type with float is strongly recommended.

    ADDR = 'https://localhost:9999'
    ORG='my-org'
    BUCKET = 'my-bucket'
    TOKEN = 'token-something-like-end-with-=='

    f = FeedHandler()
    funding_influx = FundingInflux(ADDR, org=ORG, bucket=BUCKET, token=TOKEN, numeric_type=float)
    trade_influx = TradeInflux(ADDR, org=ORG, bucket=BUCKET, token=TOKEN, numeric_type=float)
    book_influx = BookInflux(ADDR, org=ORG, bucket=BUCKET, token=TOKEN, numeric_type=float)
    bookdelta_influx = BookDeltaInflux(ADDR, org=ORG, bucket=BUCKET, token=TOKEN, numeric_type=float)
    ticker_influx = TickerInflux(ADDR, org=ORG, bucket=BUCKET, token=TOKEN, numeric_type=float)

    f.add_feed(Bitmex(channels=[FUNDING, L2_BOOK],pairs=['XBTUSD'], callbacks={FUNDING: funding_influx, L2_BOOK: book_influx, BOOK_DELTA: bookdelta_influx}))
    f.add_feed(Coinbase(channels=[TRADES], pairs=['BTC-USD'], callbacks={TRADES: trade_influx}))
    f.add_feed(Coinbase(channels=[L2_BOOK], pairs=['BTC-USD'], callbacks={L2_BOOK: book_influx, BOOK_DELTA: bookdelta_influx}))
    f.add_feed(Coinbase(channels=[TICKER], pairs=['BTC-USD'], callbacks={TICKER: ticker_influx}))
    """

    f.run()


if __name__ == '__main__':
    main()
