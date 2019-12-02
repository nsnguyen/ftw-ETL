from sqlalchemy import Column, BIGINT, TEXT, TIMESTAMP, INT, ARRAY, DECIMAL, BOOLEAN, FLOAT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DeviceSmsLog(Base):
  __tablename__ = 'device_sms_log'
  device_id = Column(TEXT, primary_key=True)
  formatted_phone_number = Column(TEXT, primary_key=True)
  message_TIMESTAMP = Column(TIMESTAMP, primary_key=True)
  direction = Column(TEXT, primary_key=True)
  content = Column(TEXT, primary_key=True)
  device_message_id = Column(BIGINT)
  message_hash = Column(TEXT)
  phone_number = Column(TEXT)
  deleted_flag = Column(BOOLEAN)
  uploaded_timestamp = Column(TIMESTAMP)
