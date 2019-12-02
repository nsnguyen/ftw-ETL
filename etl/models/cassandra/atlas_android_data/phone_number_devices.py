from sqlalchemy import Column, BIGINT, TEXT, TIMESTAMP, INT, ARRAY, DECIMAL, BOOLEAN, FLOAT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# TODO: check this
class PhoneNumberDevices(Base):
  __tablename__ = 'phone_number_devices'
  phone_number = Column(TEXT, primary_key=True)
  device_ids = Column(object)
  deleted_flag = Column(BOOLEAN)
  uploaded_timestamp = Column(TIMESTAMP)
