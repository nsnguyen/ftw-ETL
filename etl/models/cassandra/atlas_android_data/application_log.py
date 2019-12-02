from sqlalchemy import Column, BIGINT, TEXT, TIMESTAMP, INT, ARRAY, DECIMAL, BOOLEAN, FLOAT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ApplicationLog(Base):
  __tablename__ = 'application_log'
  package_name = Column(TEXT, primary_key=True)
  user_id = Column(BIGINT, primary_key=True)
  last_uploaded_at = Column(TIMESTAMP)
  deleted_flag = Column(BOOLEAN)
  uploaded_timestamp = Column(TIMESTAMP)
