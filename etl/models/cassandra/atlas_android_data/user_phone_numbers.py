from sqlalchemy import Column, BIGINT, TEXT, TIMESTAMP, INT, ARRAY, DECIMAL, BOOLEAN, FLOAT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# TODO: check this
class UserPhoneNumbers(Base):
  __tablename__ = 'user_phone_numbers'
  user_id = Column(BIGINT, primary_key=True)
  phone_numbers = Column(object)
  deleted_flag = Column(BOOLEAN)
  uploaded_timestamp = Column(TIMESTAMP)
