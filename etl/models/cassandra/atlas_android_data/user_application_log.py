from sqlalchemy import Column, BIGINT, TEXT, TIMESTAMP, INT, ARRAY, DECIMAL, BOOLEAN, FLOAT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserApplicationLog(Base):
  __tablename__ = 'user_application_log'
  user_id = Column(BIGINT, primary_key=True)
  trigger_type = Column(TEXT, primary_key=True)
  trigger_id = Column(BIGINT, primary_key=True)
  package_name = Column(TEXT, primary_key=True)
  application_name = Column(TEXT)
  data_collected_at = Column(TIMESTAMP)
  data_uploaded_at = Column(TIMESTAMP)
  device_id = Column(TEXT)
  installed_at = Column(TIMESTAMP)
  is_system_app = Column(BOOLEAN)
  status = Column(TEXT)
  deleted_flag = Column(BOOLEAN)
  uploaded_timestamp = Column(TIMESTAMP)
