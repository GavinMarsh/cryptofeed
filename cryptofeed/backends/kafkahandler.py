'''
Copyright (C) 2017-2020  Rez
'''


def connect_kafka_consumer(mytopic):
    _consumer = None
    try:
        _consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'],topic=mytopic)
    except Exception as ex:
        print('Exception while connecting Kafka Consumer')
        print(str(ex))
    finally:
        return _consumer
