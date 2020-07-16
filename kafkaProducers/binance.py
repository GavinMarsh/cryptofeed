'''
Copyright (C) 2018-2020
'''
from cryptofeed.backends.kafka import TickerKafka, TradeKafka, BookKafka
from cryptofeed import FeedHandler
from cryptofeed.exchanges import Binance
#from cryptofeed.exchanges import BinanceFutures #tried useing BinanceFutures but symbol is not supprted on exchange
from cryptofeed.defines import TICKER, TRADES, L2_BOOK


'''
currently unable to pull futures ticker data?
'''
def main():
    f = FeedHandler()

#    f.add_feed(BinanceFutures(pairs=['BTC-USDT'], channels=[TRADES, TICKER, L2_BOOK], callbacks={L2_BOOK: BookKafka(), TRADES: TradeKafka(), TICKER: TickerKafka()})) # uncomment to test BinanceFutures, correct code
    f.add_feed(Binance(pairs=['BTC-USDT'], channels=[TRADES, TICKER, L2_BOOK], callbacks={L2_BOOK: BookKafka(), TRADES: TradeKafka(), TICKER: TickerKafka()}))



    f.run()


if __name__ == '__main__':
    main()
