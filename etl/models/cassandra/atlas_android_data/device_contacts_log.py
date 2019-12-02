from sqlalchemy import Column, BIGINT, TEXT, TIMESTAMP, INT, ARRAY, DECIMAL, BOOLEAN, FLOAT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# TODO: need to check this
class DeviceContactsLog(Base):
  __tablename__ = 'device_contacts_log'
  device_id = Column(TEXT, primary_key=True)
  formatted_phone_number = Column(TEXT, primary_key=True)
  users = Column(object)
  deleted_flag = Column(BOOLEAN)
  uploaded_timestamp = Column(TIMESTAMP)
