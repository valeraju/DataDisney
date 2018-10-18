from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json

es = Elasticsearch()

# To consume messages
consumer = KafkaConsumer('topic1', bootstrap_servers=['localhost:9092'])
print("connected to consumer")

i = 0

for message in consumer:
    attraction = json.loads(message.value.decode())
    print("json attraction load")
    es.index(index='disney', doc_type='attraction', body=attraction)
    i = i + 1
    print(i)