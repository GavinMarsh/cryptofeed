'''
Copyright (C) 2018-2020
'''
from cryptofeed.backends.kafka import TickerKafka, TradeKafka, BookKafka
from cryptofeed import FeedHandler
from cryptofeed.exchanges import BinanceFutures
from cryptofeed.defines import TICKER, TRADES, L2_BOOK


def main():
    f = FeedHandler()

    f.add_feed(BinanceFutures(pairs=['BTC-USDT-'], channels=[TRADES, TICKER, L2_BOOK], callbacks={L2_BOOK: BookKafka(), TRADES: TradeKafka(), TICKER: TickerKafka()}))
#   f.add_feed(Binance(pairs=['BTC-USDT'], channels=[TRADES, TICKER, L2_BOOK], callbacks={L2_BOOK: BookKafka(), TRADES: TradeKafka(), TICKER: TickerKafka()}))

#    f.add_feed(Huobi(config=config, callbacks={TRADES: TradeKafka(), L2_BOOK: BookKafka()}))



    f.run()


if __name__ == '__main__':
    main()
