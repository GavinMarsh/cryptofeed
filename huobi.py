'''
Copyright (C) 2018-2020
'''
from cryptofeed.backends.kafka import TickerKafka, TradeKafka, BookKafka
from cryptofeed import FeedHandler
from cryptofeed.exchanges import HuobiDM
from cryptofeed.defines import TRADES, L2_BOOK


def main():
    f = FeedHandler()
    #'BTC201225'
    #'BTC200925'
    config = {L2_BOOK: ['BTC_CQ', 'BTC_NQ']}
    f.add_feed(HuobiDM(config=config, callbacks={TRADES: TradeCallback(trade), L2_BOOK: BookCallback(book)}))
    config = {TRADES: ['BTC-USDT', 'ETH-USDT'], L2_BOOK: ['BTC-USDT']}
    f.add_feed(Huobi(config=config, callbacks={TRADES: TradeCallback(trade), L2_BOOK: BookCallback(book)}))



    f.run()


if __name__ == '__main__':
    main()
