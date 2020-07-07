'''
Copyright (C) 2018-2020
'''
from cryptofeed.backends.kafka import TradeKafka, BookKafka, FundingKafka, BookDeltaKafka, TickerKafka, OpenInterestKafka
from cryptofeed import FeedHandler
from cryptofeed.exchanges import OKEx, OKCoin
from cryptofeed.defines import TRADES, L2_BOOK, OPEN_INTEREST, FUNDING, TICKER_FUTURES, TRADES_FUTURES, TICKER

def main():
    f = FeedHandler()

    okex_symbols = OKEx.get_active_symbols()
    f.add_feed(OKEx(pairs=okex_symbols, channels=[TICKER_FUTURES], callbacks={TICKER_FUTURES: TradeKafka()}))
    f.add_feed(OKEx(pairs=['BTC-USDT'], channels=[TICKER], callbacks={TICKER: TickerKafka()}))
    f.add_feed(OKEx(pairs=['BTC-USDT'], channels=[TRADES], callbacks={TRADES: TradeKafka()}))
    f.add_feed(OKCoin(pairs=['BTC-USD'], channels=[L2_BOOK], callbacks={L2_BOOK: BookKafka()}))

    f.run()

if __name__ == '__main__':
    main()
