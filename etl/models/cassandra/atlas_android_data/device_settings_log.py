from sqlalchemy import Column, BIGINT, TEXT, TIMESTAMP, INT, ARRAY, DECIMAL, BOOLEAN, FLOAT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DeviceSettingsLog(Base):
  __tablename__ = 'device_settings_log'
  device_id = Column(TEXT, primary_key=True)
  current_locale = Column(TEXT)
  data_collected_at = Column(TIMESTAMP)
  default_language = Column(TEXT)
  default_locale = Column(TEXT)
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
