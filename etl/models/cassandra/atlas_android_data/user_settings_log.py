from sqlalchemy import Column, BIGINT, TEXT, TIMESTAMP, INT, ARRAY, DECIMAL, BOOLEAN, FLOAT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# TODO: need to test this
class UserSettingsLog(Base):
  __tablename__ = 'user_settings_log'
  user_id = Column(BIGINT, primary_key=True)
  trigger_type = Column(TEXT, primary_key=True)
  trigger_id = Column(BIGINT, primary_key=True)
  current_locale = Column(TEXT)
  data_collected_at = Column(TIMESTAMP)
  data_uploaded_at = Column(TIMESTAMP)
  default_language = Column(TEXT)
  default_locale = Column(TEXT)
  device_id = Column(TEXT)
  device_timezone = Column(TEXT)
  font_scale = Column(FLOAT)
  keyboard_type = Column(TEXT)
  mobile_country_code = Column(INT)
  mobile_network_code = Column(INT)
  navigation_type = Column(TEXT)
  touchscreen_type = Column(TEXT)
  user_accounts = Column(ARRAY)
  deleted_flag = Column(BOOLEAN)
  uploaded_timestamp = Column(TIMESTAMP)
