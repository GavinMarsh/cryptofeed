'''
Copyright (C) 2018-2020
'''
from cryptofeed.backends.kafka import TickerKafka, TradeKafka, BookKafka, FundingKafka, BookDeltaKafka, OpenInterestKafka
from cryptofeed import FeedHandler
from cryptofeed.exchanges import Bitmex
from cryptofeed.defines import TICKER, TRADES, L2_BOOK, OPEN_INTEREST, FUNDING


def main():
    f = FeedHandler()
    cbs = {TRADES: TradeKafka(), L2_BOOK: BookKafka(), OPEN_INTEREST: OpenInterestKafka()}

    bitmex_symbols = Bitmex.get_active_symbols()
    f.add_feed(Bitmex(channels=[TICKER], pairs=['XBTUSD'], callbacks={TICKER: TickerKafka()}))
    f.add_feed(Bitmex(channels=[TRADES], pairs=bitmex_symbols, callbacks=cbs))
    f.add_feed(Bitmex(pairs=['XBTUSD'], channels=[FUNDING, TRADES], callbacks=cbs))

    f.run()


if __name__ == '__main__':
    main()
