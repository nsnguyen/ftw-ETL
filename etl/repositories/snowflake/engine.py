import sqlalchemy as db
from snowflake.sqlalchemy import URL
import os


class SnowflakeEngine:
  _account = os.environ.get('SNOWFLAKE_ACCOUNT')
  _user = os.environ.get('SNOWFLAKE_USER')
  _password = os.environ.get('SNOWFLAKE_PASSWORD')
  _database = os.environ.get('SNOWFLAKE_DATABASE')
  _schema = os.environ.get('SNOWFLAKE_SCHEMA')
  _warehouse = os.environ.get('SNOWFLAKE_WAREHOUSE')
  _role = os.environ.get('SNOWFLAKE_ROLE')

  @classmethod
  def create_engine(cls):
    return db.create_engine(URL(
      account=cls._account,
      user=cls._user,
      password=cls._password,
      database=cls._database,
      schema=cls._schema,
      warehouse=cls._warehouse,
      role=cls._role,
    ))
