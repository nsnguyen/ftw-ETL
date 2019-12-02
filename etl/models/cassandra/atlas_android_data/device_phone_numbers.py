from sqlalchemy import Column, BIGINT, TEXT, TIMESTAMP, INT, ARRAY, DECIMAL, BOOLEAN, FLOAT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# TODO: need to check this
class DevicePhoneNumbers(Base):
  __tablename__ = 'device_phone_numbers'
  device_id = Column(TEXT, primary_key=True)
  phone_numbers = Column(object)
  deleted_flag = Column(BOOLEAN)
  uploaded_timestamp = Column(TIMESTAMP)
