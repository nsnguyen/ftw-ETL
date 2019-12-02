from sqlalchemy import Column, BIGINT, TEXT, TIMESTAMP, INT, ARRAY, DECIMAL, BOOLEAN, FLOAT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# TODO: check this
class UserLocationLog(Base):
  __tablename__ = 'user_location_log'
  user_id = Column(BIGINT, primary_key=True)
  trigger_type = Column(TEXT, primary_key=True)
  trigger_id = Column(BIGINT, primary_key=True)
  accuracy = Column(FLOAT)
  data_collected_at = Column(TIMESTAMP)
  data_uploaded_at = Column(TIMESTAMP)
  device_id = Column(TEXT)
  latitude = Column(FLOAT)
  longitude = Column(FLOAT)
  time_stayed = Column(BIGINT)
  deleted_flag = Column(BOOLEAN)
  uploaded_timestamp = Column(TIMESTAMP)
