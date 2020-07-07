'''
Copyright (C) 2018-2020
'''
from cryptofeed.backends.kafka import TickerKafka, TradeKafka, BookKafka
from cryptofeed import FeedHandler
from cryptofeed.exchanges import Binance
#from cryptofeed.defines import TICKER, TRADES, L2_BOOK, TICKER_FUTURES
from cryptofeed.defines import L2_BOOK_FUTURES, L2_BOOK, BID, ASK, TRADES, TRADES_FUTURES, TICKER, TICKER_FUTURES

def main():
    f = FeedHandler()

    f.add_feed(BinanceFutures(pairs=['BTC-USDT'], channels=[TRADES_FUTURES, TICKER_FUTURES, L2_BOOK_FUTURES], callbacks={L2_BOOK_FUTURES: BookKafka(), TRADES_FUTURES: TradeKafka(), TICKER_FUTURES: TickerKafka()}))
 #   f.add_feed(Binance(pairs=['BTC-USDT'], channels=[TRADES, TICKER, L2_BOOK], callbacks={L2_BOOK: BookKafka(), TRADES: TradeKafka(), TICKER: TickerKafka()}))

#    f.add_feed(Huobi(config=config, callbacks={TRADES: TradeKafka(), L2_BOOK: BookKafka()}))



    f.run()


if __name__ == '__main__':
    main()
