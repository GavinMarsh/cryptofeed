'''
Copyright (C) 2018-2020
'''
from cryptofeed.backends.kafka import TickerKafka, TradeKafka, BookKafka
from cryptofeed import FeedHandler
from cryptofeed.exchanges import OKEx
from cryptofeed.defines import L2_BOOK_FUTURES, L2_BOOK, BID, ASK, TRADES, TRADES_FUTURES, TICKER, TICKER_FUTURES

def main():
    f = FeedHandler()

    cbs = {TRADES_FUTURES: TradeKafka(), L2_BOOK: BookKafka(), TICKER_FUTURES: TickerKafka()}
    pairs = OKEx.get_active_symbols()
    f.add_feed(OKEx(pairs=pairs, channels=[TRADES_FUTURES, L2_BOOK_FUTURES, TICKER_FUTURES], callbacks=cbs))
#    f.add_feed(OKEx(pairs=['BTC-USDT'], channels=[TICKER], callbacks={TICKER: TickerKafka()}))
#    f.add_feed(OKEx(pairs=['BTC-USDT'], channels=[TRADES], callbacks={TRADES: TradeKafka()}))
#    f.add_feed(OKEx(pairs=okex_symbols, channels=[TRADES_FUTURES], callbacks={TRADES_FUTURES: TradeKafka()}))
#    f.add_feed(OKCoin(pairs=['BTC-USD'], channels=[L2_BOOK], callbacks={L2_BOOK: BookKafka()}))

    f.run()

if __name__ == '__main__':
    main()
