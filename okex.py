'''
Copyright (C) 2018-2020  Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
'''
from cryptofeed.backends.kafka import TradeKafka, BookKafka, FundingKafka, BookDeltaKafka, TickerKafka, OpenInterestKafka
from cryptofeed import FeedHandler
from cryptofeed.exchanges import OKEx, OKCoin
from cryptofeed.defines import TRADES, L2_BOOK, OPEN_INTEREST, FUNDING, TICKER_FUTURES

"""
You can run a consumer in the console with the following command
(assuminng the defaults for the consumer group and bootstrap server)

$ ~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic trades-COINBASE-BTC-USD
"""

"""
OKEx has the same api as OKCoin, just a different websocket endpoint
"""
def main():
    f = FeedHandler()


    okex_symbols = OKEx.get_active_symbols()
#    f.add_feed(OKEx(pairs=okex_symbols, channels=[TRADES], callbacks={TRADES: TradeKafka()}))

    f.add_feed(OKCoin(channels=[TRADES_FUTURES], pairs=okex_symbols, callbacks={TRADES_FUTURES: TradeKafka()}))
    f.add_feed(OKCoin(pairs=['BTC-USD'], channels=[L2_BOOK], callbacks={L2_BOOK: BookKafka()}))
    f.add_feed(OKEx(pairs=['BTC-USDT'], channels=[TRADES], callbacks={TRADES: TradeKafka()}))

    f.run()


if __name__ == '__main__':
    main()
