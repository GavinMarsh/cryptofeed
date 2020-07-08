'''
Copyright (C) 2017-2020  Rez
'''
from cryptofeed.backends.kafkahandler import connect_kafka_consumer
from kafka import KafkaConsumer

#consumer = KafkaConsumer('trades-BITMEX-XBTUSD')
consumer = connect_kafka_consumer('trades-BITMEX-XBTUSD')
for msg in consumer:
    print (msg)

if __name__ == '__main__':
    main()
