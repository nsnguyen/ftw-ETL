from sqlalchemy import Column, BIGINT, TEXT, TIMESTAMP, INT, ARRAY, DECIMAL, BOOLEAN, FLOAT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# TODO: need to test this
class PhoneNumberUsers(Base):
  __tablename__ = 'phone_number_users'
  phone_number = Column(TEXT, primary_key=True)
  user_ids = Column(object)
  deleted_flag = Column(BOOLEAN)
  uploaded_timestamp = Column(TIMESTAMP)
