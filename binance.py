'''
Copyright (C) 2018-2020
'''
from cryptofeed.backends.kafka import TickerKafka, TradeKafka, BookKafka
from cryptofeed import FeedHandler
from cryptofeed.exchanges import Binance_futures
#from cryptofeed.defines import TICKER, TRADES, L2_BOOK
from cryptofeed.defines import TICKER, TRADES, L2_BOOK, BINANCE_FUTURES


'''
currently unable to pull futures ticker data?
'''
def main():
    f = FeedHandler()

    f.add_feed(Binance_futures(pairs=['BTC-USDT'], channels=[BINANCE_FUTURES, TICKER, L2_BOOK], callbacks={L2_BOOK: BookKafka(), TRADES: TradeKafka(), TICKER: TickerKafka()}))
#    f.add_feed(Binance(pairs=['BTC-USDT'], channels=[TRADES, TICKER, L2_BOOK], callbacks={L2_BOOK: BookKafka(), TRADES: TradeKafka(), TICKER: TickerKafka()}))



    f.run()


if __name__ == '__main__':
    main()
