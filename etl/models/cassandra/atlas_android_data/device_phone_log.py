from sqlalchemy import Column, BIGINT, TEXT, TIMESTAMP, INT, ARRAY, DECIMAL, BOOLEAN, FLOAT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DevicePhoneLog(Base):
  __tablename__ = 'device_phone_log'
  device_id = Column(TEXT, primary_key=True)
  battery_level = Column(INT)
  data_collected_at = Column(TIMESTAMP)
  elapsed_time = Column(BIGINT)
  neighboring_cell = Column(ARRAY)
  phone_type = Column(TEXT)
  roaming_status = Column(BOOLEAN)
  uptime = Column(BIGINT)
  wifi_status = Column(BOOLEAN)
  deleted_flag = Column(BOOLEAN)
  uploaded_timestamp = Column(TIMESTAMP)
