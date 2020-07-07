'''
Copyright (C) 2018-2020
'''
from cryptofeed.backends.kafka import TickerKafka, TradeKafka, BookKafka
from cryptofeed import FeedHandler
from cryptofeed.exchanges import Bitmex
from cryptofeed.defines import TICKER, TRADES, L2_BOOK


def main():
    f = FeedHandler()

    bitmex_symbols = Bitmex.get_active_symbols()
    f.add_feed(Bitmex(channels=[TICKER], pairs=bitmex_symbols, callbacks={TICKER: TickerKafka()}))
#    f.add_feed(Bitmex(channels=[TRADES], pairs=bitmex_symbols, callbacks={TRADES: TradeKafka()}))
#    f.add_feed(Bitmex(pairs=['XBTUSD'], channels=[L2_BOOK], callbacks={L2_BOOK: BookKafka()}))


    f.run()


if __name__ == '__main__':
    main()
