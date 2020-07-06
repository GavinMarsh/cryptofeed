'''
Copyright (C) 2018-2020  Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
'''
from cryptofeed.backends.kafka import TradeKafka, BookKafka, FundingKafka, BookDeltaKafka, TickerKafka, OpenInterestKafka
from cryptofeed import FeedHandler
from cryptofeed.exchanges import Coinbase

from cryptofeed.defines import TRADES, L2_BOOK, OPEN_INTEREST, FUNDING, COINBASE, TICKER, TickerCallback


"""
You can run a consumer in the console with the following command
(assuminng the defaults for the consumer group and bootstrap server)

$ ~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic trades-COINBASE-BTC-USD
"""


def main():
    f = FeedHandler()
    cbs = {TRADES: TradeKafka(), L2_BOOK: BookKafka(), OPEN_INTEREST: OpenInterestKafka()}

    f.add_feed(COINBASE, pairs=['BTC-USD'], channels=[TICKER], callbacks={TICKER: TickerCallback(ticker)})
    f.add_feed(Coinbase(pairs=['BTC-USD'], channels=[TRADES], callbacks={TRADES: TradeCallback(trade)}))
    f.add_feed(Coinbase(config={L2_BOOK: ['BTC-USD', 'ETH-USD'], TRADES: ['ETH-USD', 'BTC-USD']}, callbacks={TRADES: TradeCallback(trade), L2_BOOK: BookCallback(book)}))


    f.run()


if __name__ == '__main__':
    main()
