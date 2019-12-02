from sqlalchemy import Column, BIGINT, TEXT, TIMESTAMP, INT, ARRAY, DECIMAL, BOOLEAN, FLOAT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserSmsLog(Base):
  __tablename__ = 'user_sms_log'
  user_id = Column(BIGINT, primary_key=True)
  trigger_type = Column(TEXT, primary_key=True)
  trigger_id = Column(BIGINT, primary_key=True)
  content = Column(TEXT, primary_key=True)
  data_uploaded_at = Column(TIMESTAMP)
  device_id = Column(TEXT)
  device_message_id = Column(BIGINT)
  direction = Column(TEXT)
  formatted_phone_number = Column(TEXT)
  message_hash = Column(TEXT)
  message_TIMESTAMP = Column(TIMESTAMP)
  phone_number = Column(TEXT)
  deleted_flag = Column(BOOLEAN)
  uploaded_timestamp = Column(TIMESTAMP)