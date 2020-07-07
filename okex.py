'''
Copyright (C) 2018-2020  Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
'''
from cryptofeed.backends.kafka import TradeKafka, BookKafka, FundingKafka, BookDeltaKafka, TickerKafka, OpenInterestKafka
from cryptofeed import FeedHandler
from cryptofeed.exchanges import OKEx
from cryptofeed.defines import OKEX, TRADES, L2_BOOK, OPEN_INTEREST, FUNDING

"""
You can run a consumer in the console with the following command
(assuminng the defaults for the consumer group and bootstrap server)

$ ~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic trades-COINBASE-BTC-USD
"""

def main():
    f = FeedHandler()
    cbs = {TRADES: TradeKafka(), L2_BOOK: BookKafka(), OPEN_INTEREST: OpenInterestKafka()}

    okex_symbols = OKEx.get_active_symbols()
    f.add_feed(OKEx(channels=[OPEN_INTEREST], pairs=['BTCUSD'], callbacks=cbs))
    f.add_feed(OKEx(channels=[TRADES], pairs=okex_symbols, callbacks=cbs))
    f.add_feed(OKEx(pairs=['BTCUSD'], channels=[FUNDING, TRADES], callbacks=cbs))


    f.run()


if __name__ == '__main__':
    main()
