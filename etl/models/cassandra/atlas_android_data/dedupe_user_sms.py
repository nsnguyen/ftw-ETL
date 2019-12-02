from sqlalchemy import Column, BIGINT, TEXT, TIMESTAMP, INT, ARRAY, DECIMAL, BOOLEAN, FLOAT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DedupeUserSms(Base):
  __tablename__ = 'dedupe_user_sms'
  message_hash = Column(TEXT, primary_key=True)
  user_id = Column(BIGINT, primary_key=True)
  deleted_flag = Column(BOOLEAN)
  uploaded_timestamp = Column(TIMESTAMP)
