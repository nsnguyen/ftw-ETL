from sqlalchemy import Column, BIGINT, TEXT, TIMESTAMP, INT, ARRAY, DECIMAL, BOOLEAN, FLOAT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserPhoneLog(Base):
  __tablename__ = 'user_phone_log'
  user_id = Column(BIGINT, primary_key=True)
  trigger_type = Column(TEXT, primary_key=True)
  trigger_id = Column(BIGINT, primary_key=True)
  battery_level = Column(INT)
  data_collected_at = Column(TIMESTAMP)
  data_uploaded_at = Column(TIMESTAMP)
  device_id = Column(TEXT)
  elapsed_time = Column(BIGINT)
  neighboring_cell = Column(ARRAY)
  phone_type = Column(TEXT)
  roaming_status = Column(BOOLEAN)
  uptime = Column(BIGINT)
  wifi_status = Column(BOOLEAN)
  deleted_flag = Column(BOOLEAN)
  uploaded_timestamp = Column(TIMESTAMP)
