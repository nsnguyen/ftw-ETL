from sqlalchemy import Column, BIGINT, TEXT, TIMESTAMP, INT, ARRAY, DECIMAL, BOOLEAN, FLOAT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DedupeBlueToothAddress(Base):
  __tablename__ = 'dedupe_bluetooth_address'
  bluetooth_address = Column(TEXT, primary_key=True)
  seen_at = Column(TIMESTAMP, primary_key=True)
  user_id = Column(BIGINT, primary_key=True)
  trigger_id = Column(BIGINT)
  trigger_type = Column(TEXT)
  deleted_flag = Column(BOOLEAN)
  uploaded_timestamp = Column(TIMESTAMP)
