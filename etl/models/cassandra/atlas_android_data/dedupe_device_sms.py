from sqlalchemy import Column, BIGINT, TEXT, TIMESTAMP, INT, ARRAY, DECIMAL, BOOLEAN, FLOAT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DedupeDeviceSms(Base):
  __tablename__ = 'dedupe_device_sms'
  message_hash = Column(TEXT, primary_key=True)
  device_id = Column(TEXT, primary_key=True)
  deleted_flag = Column(BOOLEAN)
  uploaded_timestamp = Column(TIMESTAMP)
