from confluent_kafka import Consumer, KafkaException
import sys
import getopt
import json
import logging
from pprint import pformat

# Create logger for consumer (logs will be emitted when poll() is called)
logger = logging.getLogger('consumer')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)-15s %(levelname)-8s %(message)s'))
logger.addHandler(handler)

consumer = Consumer({
  "bootstrap.servers": "localhost:9092",
  "group.id": "atlas-android-data-processor",
  'session.timeout.ms': 6000,
  # 'auto.offset.reset': 'earliest'
}, logger=logger)

output_topic = "data_warehouse"


def print_assignment(consumer, partitions):
  print('Assignment:', partitions)


consumer.subscribe([output_topic], on_assign=print_assignment)

try:
  while True:
    msg = consumer.poll(timeout=1.0)
    if msg is None:
      continue
    if msg.error():
      raise KafkaException(msg.error())
    else:
      # Proper message
      sys.stderr.write('%% %s [%d] at offset %d with key %s:\n' %
                       (msg.topic(), msg.partition(), msg.offset(),
                        str(msg.key())))
      print(msg.value())
except KeyboardInterrupt:
  sys.stderr.write('%% Aborted by user\n')

finally:
  consumer.close()

