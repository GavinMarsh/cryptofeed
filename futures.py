'''
Copyright (C) 2018-2020  Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
'''
from cryptofeed.backends.kafka import TradeKafka, BookKafka, FundingKafka, BookDeltaKafka, TickerKafka, OpenInterestKafka
from cryptofeed import FeedHandler
from cryptofeed.exchanges import Coinbase, Bitmex

from cryptofeed.defines import TRADES, L2_BOOK, OPEN_INTEREST, FUNDING


"""
You can run a consumer in the console with the following command
(assuminng the defaults for the consumer group and bootstrap server)

$ /kafka/bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic trades-COINBASE-BTC-USD
"""


def main():
    f = FeedHandler()
    cbs = {TRADES: TradeKafka(), L2_BOOK: BookKafka(), OPEN_INTEREST: OpenInterestKafka()}

    f.add_feed(Coinbase(max_depth=10, channels=[TRADES, L2_BOOK], pairs=['BTC-USD'], callbacks=cbs))
    bitmex_symbols = Bitmex.get_active_symbols()
    f.add_feed(Bitmex(channels=[OPEN_INTEREST], pairs=['XBTUSD'], callbacks=cbs))
    f.add_feed(Bitmex(channels=[TRADES], pairs=bitmex_symbols, callbacks={TRADES: TradeCallback(trade)}))
    f.add_feed(Bitmex(pairs=['XBTUSD'], channels=[FUNDING, TRADES], callbacks={FUNDING: FundingCallback(funding), TRADES: TradeCallback(trade)}))


    f.run()


if __name__ == '__main__':
    main()
