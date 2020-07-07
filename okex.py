'''
Copyright (C) 2018-2020
'''
from cryptofeed.backends.kafka import TickerKafka, TradeKafka, BookKafka
from cryptofeed import FeedHandler
from cryptofeed.exchanges import OKEx, OKCoin
from cryptofeed.defines import TICKER, TICKER_FUTURES, TRADES, TRADES_FUTURES, L2_BOOK

def main():
    f = FeedHandler()

    okex_symbols = OKEx.get_active_symbols()
#    f.add_feed(OKEx(pairs=okex_symbols, channels=[TICKER_FUTURES], callbacks={TICKER_FUTURES: TradeKafka()}))
    f.add_feed(OKEx(pairs=okex_symbols, channels=[TRADES_FUTURES], callbacks={TRADES_FUTURES: TradeKafka()}))
#    f.add_feed(OKEx(pairs=['BTC-USDT'], channels=[TICKER], callbacks={TICKER: TickerKafka()}))
    f.add_feed(OKEx(pairs=['BTC-USDT'], channels=[TRADES], callbacks={TRADES: TradeKafka()}))
    f.add_feed(OKCoin(pairs=['BTC-USD'], channels=[L2_BOOK], callbacks={L2_BOOK: BookKafka()}))

    f.run()

if __name__ == '__main__':
    main()
