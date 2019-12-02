def import_table(table_name):
  if table_name == 'dedupe_subscriber_id':
    from dags.models.cassandra.atlas_android_data.dedupe_subscriber_id import DedupeSubscriberId
    return DedupeSubscriberId
  if table_name == 'dedupe_phone_number':
    from dags.models.cassandra.atlas_android_data.dedupe_phone_number import DedupePhoneNumber
    return DedupePhoneNumber
  if table_name == 'dedupe_user_sms':
    from dags.models.cassandra.atlas_android_data.dedupe_user_sms import DedupeUserSms
    return DedupeUserSms
  if table_name == 'dedupe_google_ad_id':
    from dags.models.cassandra.atlas_android_data.dedupe_google_ad_id import DedupeGoogleAdId
    return DedupeGoogleAdId
  if table_name == 'dedupe_bluetooh_address':
    from dags.models.cassandra.atlas_android_data.dedupe_bluetooth_address import DedupeBlueToothAddress
    return DedupeBlueToothAddress
  if table_name == 'dedupe_device_id':
    from dags.models.cassandra.atlas_android_data.dedupe_device_id import DedupeDeviceId
    return DedupeDeviceId
  if table_name == 'dedupe_android_id':
    from dags.models.cassandra.atlas_android_data.dedupe_android_id import DedupeAndroidId
    return DedupeAndroidId
  if table_name == 'dedupe_android_serial_number':
    from dags.models.cassandra.atlas_android_data.dedupe_android_serial_number import DedupeAndroidSerialNumber
    return DedupeAndroidSerialNumber
  if table_name == 'dedupe_wlan_mac':
    from dags.models.cassandra.atlas_android_data.dedupe_wlan_mac import DedupeWlanMac
    return DedupeWlanMac
  if table_name == 'dedupe_device_sms':
    from dags.models.cassandra.atlas_android_data.dedupe_device_sms import DedupeDeviceSms
    return DedupeDeviceSms
  if table_name == 'application_log':
    from dags.models.cassandra.atlas_android_data.application_log import ApplicationLog
    return ApplicationLog
  if table_name == 'phone_number_users':
    from dags.models.cassandra.atlas_android_data.phone_number_users import PhoneNumberUsers
    return PhoneNumberUsers
  if table_name == 'phone_number_user_contacts':
    from dags.models.cassandra.atlas_android_data.phone_number_user_contacts import PhoneNumberUserContacts
    return PhoneNumberUserContacts
  if table_name == 'schema_migrations':
    from dags.models.cassandra.atlas_android_data.schema_migrations import SchemaMigrations
    return SchemaMigrations
  if table_name == 'device_settings_log':
    from dags.models.cassandra.atlas_android_data.device_settings_log import DeviceSettingsLog
    return DeviceSettingsLog
  if table_name == 'device_sim_log':
    from dags.models.cassandra.atlas_android_data.device_sim_log import DeviceSimLog
    return DeviceSimLog
  if table_name == 'device_phone_log':
    from dags.models.cassandra.atlas_android_data.device_phone_log import DevicePhoneLog
    return DevicePhoneLog
  if table_name == 'device_contacts_log':
    from dags.models.cassandra.atlas_android_data.device_contacts_log import DeviceContactsLog
    return DeviceContactsLog
  if table_name == 'device_phone_numbers':
    from dags.models.cassandra.atlas_android_data.device_phone_numbers import DevicePhoneNumbers
    return DevicePhoneNumbers
  if table_name == 'device_location_log':
    from dags.models.cassandra.atlas_android_data.device_location_log import DeviceLocationLog
    return DeviceLocationLog
  if table_name == 'device_sms_log':
    from dags.models.cassandra.atlas_android_data.device_sms_log import DeviceSmsLog
    return DeviceSmsLog
  if table_name == 'user_sim_log':
    from dags.models.cassandra.atlas_android_data.user_sim_log import UserSimLog
    return UserSimLog
  if table_name == 'user_sms_log':
    from dags.models.cassandra.atlas_android_data.user_sms_log import UserSmsLog
    return UserSmsLog
  if table_name == 'user_application_log':
    from dags.models.cassandra.atlas_android_data.user_application_log import UserApplicationLog
    return UserApplicationLog
  if table_name == 'user_device_hardware_log':
    from dags.models.cassandra.atlas_android_data.user_device_hardware_log import UserDeviceHardwareLog
    return UserDeviceHardwareLog
  if table_name == 'user_settings_log':
    from dags.models.cassandra.atlas_android_data.user_settings_log import UserSettingsLog
    return UserSettingsLog
  if table_name == 'user_contacts_log':
    from dags.models.cassandra.atlas_android_data.user_contacts_log import UserContactsLog
    return UserContactsLog
  if table_name == 'user_location_log':
    from dags.models.cassandra.atlas_android_data.user_location_log import UserLocationLog
    return UserLocationLog
  if table_name == 'user_phone_log':
    from dags.models.cassandra.atlas_android_data.user_phone_log import UserPhoneLog
    return UserPhoneLog
  if table_name == 'user_phone_numbers':
    from dags.models.cassandra.atlas_android_data.user_phone_numbers import UserPhoneNumbers
    return UserPhoneNumbers
  if table_name == 'user_device_statistics':
    from dags.models.cassandra.atlas_android_data.user_device_statistics import UserDeviceStatistics
    return UserDeviceStatistics
  if table_name == 'phone_number_devices':
    from dags.models.cassandra.atlas_android_data.phone_number_devices import PhoneNumberDevices
    return PhoneNumberDevices
  if table_name == 'raw_sms_log':
    from dags.models.cassandra.atlas_android_data.raw_sms_log import RawSmsLog
    return RawSmsLog
