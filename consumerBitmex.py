'''
Copyright (C) 2017-2020  Rez
'''
from cryptofeed.backends.kafkahandler import connect_kafka_consumer
from kafka import KafkaConsumer

consumer = KafkaConsumer('trades-BITMEX-XBTUSD')
for message in consumer:
    print (message[6]['price'])





#metrics = consumer.metrics()
