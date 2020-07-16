'''
Copyright (C) 2018-2020
'''
from cryptofeed.backends.kafka import TickerKafka, TradeKafka, BookKafka
from cryptofeed import FeedHandler
from cryptofeed.exchanges import Binance
#from cryptofeed.exchanges import BinanceFutures #tried useing BinanceFutures but symbol is not supprted on exchange
from cryptofeed.defines import TICKER, TRADES, L2_BOOK

import io.confluent.kafka.serializers.AbstractKafkaSchemaSerDeConfig
import org.apache.kafka.clients.consumer.ConsumerConfig
import org.apache.kafka.clients.consumer.ConsumerRecord
import org.apache.kafka.clients.consumer.ConsumerRecords
import org.apache.kafka.clients.consumer.KafkaConsumer
import io.confluent.kafka.serializers.KafkaAvroDeserializer
import io.confluent.kafka.serializers.KafkaAvroDeserializerConfig
import org.apache.kafka.common.serialization.StringDeserializer

import java.time.Duration
import java.util.Collections
import java.util.Properties

'''
currently unable to pull futures ticker data?
'''
def main():
    package io.confluent.examples.clients.basicavro

    public class ConsumerExample {

        private static final String TOPIC = "transactions"

        @SuppressWarnings("InfiniteLoopStatement")
        public static void main(final String[] args) {
            final Properties props = new Properties();
            props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
            props.put(ConsumerConfig.GROUP_ID_CONFIG, "test");
            props.put(ConsumerConfig.ENABLE_AUTO_COMMIT_CONFIG, "true");
            props.put(ConsumerConfig.AUTO_COMMIT_INTERVAL_MS_CONFIG, "1000");
            props.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");
            props.put(AbstractKafkaSchemaSerDeConfig.SCHEMA_REGISTRY_URL_CONFIG, "http://localhost:8081");
            props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);
            props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, KafkaAvroDeserializer.class);
            props.put(KafkaAvroDeserializerConfig.SPECIFIC_AVRO_READER_CONFIG, true);

            try (final KafkaConsumer<String, Payment> consumer = new KafkaConsumer<>(props)) {
                consumer.subscribe(Collections.singletonList(TOPIC));

                while (true) {
                    final ConsumerRecords<String, Payment> records = consumer.poll(Duration.ofMillis(100));
                    for (final ConsumerRecord<String, Payment> record : records) {
                        final String key = record.key();
                        final Payment value = record.value();
                        System.out.printf("key = %s, value = %s%n", key, value);
                    }
                }

            }
        }
    }

    f.run()


if __name__ == '__main__':
    main()
