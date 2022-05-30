from kafka import KafkaConsumer

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('Topic1',
                         group_id='my-group',
                         bootstrap_servers='localhost:9093')

# i = 0
# while True:
#     records = consumer.poll()
#     print(i)
#     i += 1
#     for k, v in records.items():
#         print(f"{k=}, {v=}")
print(consumer.topics())

for message in consumer:
    # print(message)
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print(f"{message.topic, message.partition, message.offset, message.key, message.value}")
