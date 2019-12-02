from confluent_kafka import Consumer, Producer
import json
import os

import uuid
import sys
import pdb

device_location_log = {
  'MessageId': str(uuid.uuid4()),
  'TopicArn': 'cassandra-atlas-android-data-replication',
  'Message': {
    'table_name': 'device_location_log',
    'attributes': {
      'device_id': 219787711815,
      'data_uploaded_at': '2019-08-26 09:52:20.703000-0700',
      'accuracy': 500,
      'data_collected_at': '2019-08-26 09:45:34.933000-0700',
      'latitude': 37.78014,
      'longitude': -122.39664,
      'time_stayed': 0,
      'deleted_flag': False
    },
  },  # message can be stored as string here and we can parse it into json in worker
  'Timestamp': '2019-10-09 22:04:59.532000-0700',  # will be stored in int,
}

user_contacts_log = {
  'MessageId': str(uuid.uuid4()),
  'TopicArn': 'cassandra-atlas-android-data-replication',
  'Message': {
    'table_name': 'user_contacts_log',
    'deleted_flag': False,
    'attributes': {
      'user_id': 1523289,
      'trigger_type': 'loan_application',
      'trigger_id': 41677,
      'formatted_phone_number': 917021208769,
      'contact_name': 'Jignesh Mahalaxmi',
      'data_uploaded_at': '2019-10-09 22:04:59.532000-0700',
      'device_id': 866760030367603,
      'last_contacted_at': None,
      'phone_number': 7021208769,
      'phone_type': 'mobile',
      'times_contacted': 0,
      'deleted_flag': False
    }
  },
  'Timestamp': '2019-10-09 22:04:59.532000-0700',  # will be stored in int,
}
messages = [device_location_log, user_contacts_log]

# output_topic = os.environ.get("KAFKA_LOADER_TOPIC")
output_topic = "data_warehouse"

config = {
  # "bootstrap.servers": "{}:9092".format(os.environ.get("KAFKA_BROKERS")),
  "bootstrap.servers": "localhost:9092",
  "delivery.timeout.ms": 2000,
  "request.timeout.ms": 1000
}

producer = Producer(**config)


def delivery_callback(err, msg):
  if err:
    sys.stderr.write('%% Message failed delivery: %s\n' % err)
  else:
    sys.stderr.write('%% Message delivered to %s [%d] @ %d\n' %
                     (msg.topic(), msg.partition(), msg.offset()))


for message in messages:
  _json = json.dumps(message)
  print(_json)

  try:
    producer.produce(output_topic, key=message['MessageId'], value=_json, callback=delivery_callback)
  except BufferError:
    sys.stderr.write('%% Local producer queue is full (%d messages awaiting delivery): try again\n' %
                     len(producer))
  producer.poll(0)

sys.stderr.write('%% Waiting for %d deliveries\n' % len(producer))
producer.flush()
