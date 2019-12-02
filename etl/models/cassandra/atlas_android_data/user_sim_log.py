from sqlalchemy import Column, BIGINT, TEXT, TIMESTAMP, INT, ARRAY, DECIMAL, BOOLEAN, FLOAT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserSimLog(Base):
  __tablename__ = 'user_sim_log'
  user_id = Column(BIGINT, primary_key=True)
  trigger_type = Column(TEXT, primary_key=True)
  trigger_id = Column(BIGINT, primary_key=True)
  data_uploaded_at = Column(TIMESTAMP)
  detected_phone_number = Column(TEXT)
  device_id = Column(TEXT)
  network_operator = Column(TEXT)
  sim_serial_number = Column(TEXT)
  deleted_flag = Column(BOOLEAN)
  uploaded_timestamp = Column(TIMESTAMP)
