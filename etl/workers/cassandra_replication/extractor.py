import os
import json
import sys
from sqlalchemy.orm import Session
from confluent_kafka import Consumer, KafkaException
from etl.repositories.snowflake.engine import SnowflakeEngine
from etl.models.import_cassandra import import_table
from etl.utils.timestamps import current_time
from etl.utils.logging import stdout_log, stderr_log
from etl.utils.traceback import stack_trace
import traceback
import pdb



class CassandraReplicationExtractor:

  def execute(self):
    print('do some stuff in extractor')
    BufferWriter().run()








class BufferWriter:
  def __init__(self):
    self.messages = []
    self.filtered_messages = {}

    # NOTE: kafka consumer configs are found here
    # https://kafka.apache.org/documentation.html#newconsumerconfigs
    self.consumer = Consumer({
      "bootstrap.servers": "localhost:9092",
      "group.id": "atlas-android-data-processor",
      'session.timeout.ms': 6000,
      # 'auto.offset.reset': 'earliest'
    })
    self.output_topic = "data_warehouse"

  def run(self) -> None:
    # TODO: log to sumologic
    # stdout_log('read_messages from Kafka\n')
    # stdout_log('upload to Snowflake\n')
    self.consumer.subscribe([self.output_topic])

    try:
      start = current_time()
      while True:
        if current_time() - start >= 100:
          # flush all if time exceeds limit in seconds
          self.flush_all()  # just flush everything and wait for next cycle in airflow
          break

        # loop through each table to check if it's above message
        for table, messages in self.filtered_messages.items():
          print('table:', table)
          print('message length:', len(messages))

          if len(messages) >= 5:
            self.upload(table_name=table, messages=messages)
            self.filtered_messages[table] = []  # reset to empty list

        # poll here poll 1 message at a time.
        kafka_message = self.consumer.poll(timeout=1.0)
        if kafka_message is None:
          continue

        if kafka_message.error():
          raise KafkaException(kafka_message.error())

        else:
          json_message = json.loads(kafka_message.value())
          self.filter_message(message=json_message)

    except KeyboardInterrupt:
      stderr_log('%% Aborted by user\n')

    except Exception as e:
      trace = stack_trace(sys.exc_info())
      stderr_log(str(e))
      stderr_log(trace)

    finally:
      self.consumer.close()

  def filter_message(self, message: {}) -> None:
    self.filtered_messages.setdefault(message['Message']['table_name'], []).append(message['Message']['attributes'])

  @staticmethod
  def upload(table_name: str, messages: []) -> None:
    print('write to snowflake', table_name)
    # engine = SnowflakeEngine.create_engine()
    # session = Session(bind=engine)
    # _class = import_table(table_name=table_name)
    # session.bulk_insert_mappings(_class, messages)
    # session.commit()
    # session.close()

  def flush_all(self) -> None:
    print('full flush to snowflake for all tables')
    for table, messages in self.filtered_messages.items():
      self.upload(table_name=table, messages=messages)
