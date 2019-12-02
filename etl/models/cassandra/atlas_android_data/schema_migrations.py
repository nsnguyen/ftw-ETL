from sqlalchemy import Column, BIGINT, TEXT, TIMESTAMP, INT, ARRAY, DECIMAL, BOOLEAN, FLOAT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SchemaMigrations(Base):
  __tablename__ = 'schema_migrations'
  migration_type = Column(TEXT, primary_key=True)
  migration_date = Column(TIMESTAMP, primary_key=True)
  migration_number = Column(INT)
  deleted_flag = Column(BOOLEAN)
  uploaded_timestamp = Column(TIMESTAMP)
