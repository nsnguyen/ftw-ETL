from sqlalchemy import Column, BIGINT, TEXT, TIMESTAMP, INT, ARRAY, DECIMAL, BOOLEAN, FLOAT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserContactsLog(Base):
  __tablename__ = 'user_contacts_log'
  user_id = Column(BIGINT, primary_key=True)
  trigger_type = Column(TEXT, primary_key=True)
  trigger_id = Column(BIGINT, primary_key=True)
  formatted_phone_number = Column(TEXT, primary_key=True)
  contact_name = Column(TEXT)
  data_uploaded_at = Column(TIMESTAMP)
  device_id = Column(TEXT)
  last_contacted_at = Column(TIMESTAMP)
  phone_number = Column(TEXT)
  phone_type = Column(TEXT)
  times_contacted = Column(INT)
  deleted_flag = Column(BOOLEAN)
  uploaded_timestamp = Column(TIMESTAMP)
