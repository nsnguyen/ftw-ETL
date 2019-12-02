from sqlalchemy import Column, BIGINT, TEXT, TIMESTAMP, INT, ARRAY, DECIMAL, BOOLEAN, FLOAT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class RawSmsLog(Base):
  __tablename__ = 'raw_sms_log'
  message_hash = Column(TEXT, primary_key=True)
  content = Column(TEXT)
  device_message_id = Column(BIGINT)
  direction = Column(TEXT)
  formatted_phone_number = Column(TEXT)
  message_TIMESTAMP = Column(TIMESTAMP)
  phone_number = Column(TEXT)
  deleted_flag = Column(BOOLEAN)
  uploaded_timestamp = Column(TIMESTAMP)
