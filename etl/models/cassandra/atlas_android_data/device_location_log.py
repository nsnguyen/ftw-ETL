from sqlalchemy import Column, BIGINT, TEXT, TIMESTAMP, INT, ARRAY, DECIMAL, BOOLEAN, FLOAT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DeviceLocationLog(Base):
  __tablename__ = 'device_location_log'
  device_id = Column(TEXT, primary_key=True)
  data_uploaded_at = Column(TIMESTAMP, primary_key=True)
  accuracy = Column(FLOAT)
  data_collected_at = Column(TIMESTAMP)
  latitude = Column(FLOAT)
  longitude = Column(FLOAT)
  time_stayed = Column(BIGINT)
  deleted_flag = Column(BOOLEAN)
  uploaded_timestamp = Column(TIMESTAMP)
