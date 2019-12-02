from sqlalchemy import Column, BIGINT, TEXT, TIMESTAMP, INT, ARRAY, DECIMAL, BOOLEAN, FLOAT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserDeviceStatistics(Base):
  __tablename__ = 'user_device_statistics'
  user_id = Column(BIGINT, primary_key=True)
  trigger_type = Column(TEXT, primary_key=True)
  trigger_id = Column(BIGINT, primary_key=True)
  data_uploaded_at = Column(TIMESTAMP)
  device_id = Column(TEXT)
  sms_count = Column(INT)
  deleted_flag = Column(BOOLEAN)
  uploaded_timestamp = Column(TIMESTAMP)
