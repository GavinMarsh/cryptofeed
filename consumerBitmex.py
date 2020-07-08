'''
Copyright (C) 2017-2020  Rez
'''
from cryptofeed.backends.kafkahandler import connect_kafka_consumer
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('trades-BITMEX-XBTUSD',bootstrap_servers = ['localhost:9092'],
value_deserializer=lambda m: json.loads(m.decode('utf-8')))
for message in consumer:
    print (message[6]["Spot price: ",'price'])

consumer2 = KafkaConsumer('trades-BITMEX-XBTZ20',bootstrap_servers = ['localhost:9092'],
value_deserializer=lambda m: json.loads(m.decode('utf-8')))
for message2 in consumer2:
    print (message2[6]["Dec Futures price: ",'price'])



#metrics = consumer.metrics()
