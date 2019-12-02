CREATE OR REPLACE TABLE dedupe_subscriber_id (
    subscriber_id TEXT,
    seen_at TIMESTAMP,
    user_id BIGINT,
    device_id TEXT,
    trigger_id BIGINT,
    trigger_type TEXT,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (subscriber_id, seen_at, user_id)
)

CREATE OR REPLACE TABLE dedupe_phone_number (
    detected_phone_number TEXT,
    seen_at TIMESTAMP,
    user_id BIGINT,
    trigger_id BIGINT,
    trigger_type TEXT,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (detected_phone_number, seen_at, user_id)
)

CREATE OR REPLACE TABLE dedupe_user_sms (
    message_hash TEXT,
    user_id BIGINT,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (message_hash, user_id)
)

CREATE OR REPLACE TABLE dedupe_google_ad_id (
    google_ad_id TEXT,
    seen_at TIMESTAMP,
    user_id BIGINT,
    trigger_id BIGINT,
    trigger_type TEXT,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (google_ad_id, seen_at, user_id)
)

CREATE OR REPLACE TABLE dedupe_bluetooth_address (
    bluetooth_address TEXT,
    seen_at TIMESTAMP,
    user_id BIGINT,
    trigger_id BIGINT,
    trigger_type TEXT,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (bluetooth_address, seen_at, user_id)
)

CREATE OR REPLACE TABLE dedupe_device_id (
    device_id TEXT,
    seen_at TIMESTAMP,
    user_id BIGINT,
    trigger_id BIGINT,
    trigger_type TEXT,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (device_id, seen_at, user_id)
)

CREATE OR REPLACE TABLE dedupe_android_id (
    android_id TEXT,
    seen_at TIMESTAMP,
    user_id BIGINT,
    trigger_id BIGINT,
    trigger_type TEXT,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (android_id, seen_at, user_id)
)

CREATE OR REPLACE TABLE dedupe_android_serial_number (
    android_serial_number TEXT,
    seen_at TIMESTAMP,
    user_id BIGINT,
    trigger_id BIGINT,
    trigger_type TEXT,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (android_serial_number, seen_at, user_id)
)

CREATE OR REPLACE TABLE dedupe_wlan_mac (
    wlan_mac TEXT,
    seen_at TIMESTAMP,
    user_id BIGINT,
    trigger_id BIGINT,
    trigger_type TEXT,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (wlan_mac, seen_at, user_id)
)

CREATE OR REPLACE TABLE dedupe_device_sms (
    message_hash TEXT,
    device_id TEXT,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (message_hash, device_id)
)

CREATE OR REPLACE TABLE application_log (
    package_name TEXT,
    user_id BIGINT,
    last_uploaded_at TIMESTAMP,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (package_name, user_id)
)

CREATE OR REPLACE TABLE phone_number_users (
    phone_number TEXT,
    user_ids OBJECT,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (phone_number)
)

CREATE OR REPLACE TABLE phone_number_user_contacts (
    phone_number TEXT,
    users OBJECT,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (phone_number)
)


CREATE OR REPLACE TABLE schema_migrations (
    migration_type TEXT,
    migration_date TIMESTAMP,
    migration_number INT,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (migration_type, migration_date)
)

CREATE OR REPLACE TABLE device_settings_log (
    device_id TEXT,
    current_locale TEXT,
    data_collected_at TIMESTAMP,
    default_language TEXT,
    default_locale TEXT,
    device_timezone TEXT,
    font_scale FLOAT,
    keyboard_type TEXT,
    mobile_country_code INT,
    mobile_network_code INT,
    navigation_type TEXT,
    touchscreen_type TEXT,
    user_accounts ARRAY,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (device_id)
)

CREATE OR REPLACE TABLE device_sim_log (
    device_id TEXT,
    trigger_type TEXT,
    trigger_id BIGINT,
    data_uploaded_at TIMESTAMP,
    detected_phone_number TEXT,
    network_operator TEXT,
    sim_serial_number TEXT,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (device_id, trigger_type, trigger_id)
)

CREATE OR REPLACE TABLE device_phone_log (
    device_id TEXT,
    battery_level INT,
    data_collected_at TIMESTAMP,
    elapsed_time BIGINT,
    neighboring_cell ARRAY,
    phone_type TEXT,
    roaming_status BOOLEAN,
    uptime BIGINT,
    wifi_status BOOLEAN,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (device_id)
)

CREATE OR REPLACE TABLE device_contacts_log (
    device_id TEXT,
    formatted_phone_number TEXT,
    users OBJECT,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (device_id, formatted_phone_number)
)

CREATE OR REPLACE TABLE device_phone_numbers (
    device_id TEXT,
    phone_numbers OBJECT,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (device_id)
)

CREATE OR REPLACE TABLE device_location_log (
    device_id TEXT,
    data_uploaded_at TIMESTAMP,
    accuracy FLOAT,
    data_collected_at TIMESTAMP,
    latitude FLOAT,
    longitude FLOAT,
    time_stayed BIGINT,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (device_id, data_uploaded_at)
)

CREATE OR REPLACE TABLE device_sms_log (
    device_id TEXT,
    formatted_phone_number TEXT,
    message_TIMESTAMP TIMESTAMP,
    direction TEXT,
    content TEXT,
    device_message_id BIGINT,
    message_hash TEXT,
    phone_number TEXT,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (device_id, formatted_phone_number, message_TIMESTAMP, direction, content)
)

CREATE OR REPLACE TABLE user_sim_log (
    user_id BIGINT,
    trigger_type TEXT,
    trigger_id BIGINT,
    data_uploaded_at TIMESTAMP,
    detected_phone_number TEXT,
    device_id TEXT,
    network_operator TEXT,
    sim_serial_number TEXT,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (user_id, trigger_type, trigger_id)
)

CREATE OR REPLACE TABLE user_sms_log (
    user_id BIGINT,
    trigger_type TEXT,
    trigger_id BIGINT,
    content TEXT,
    data_uploaded_at TIMESTAMP,
    device_id TEXT,
    device_message_id BIGINT,
    direction TEXT,
    formatted_phone_number TEXT,
    message_hash TEXT,
    message_TIMESTAMP TIMESTAMP,
    phone_number TEXT,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (user_id, trigger_type, trigger_id, content)
)

CREATE OR REPLACE TABLE user_application_log (
    user_id BIGINT,
    trigger_type TEXT,
    trigger_id BIGINT,
    package_name TEXT,
    application_name TEXT,
    data_collected_at TIMESTAMP,
    data_uploaded_at TIMESTAMP,
    device_id TEXT,
    installed_at TIMESTAMP,
    is_system_app BOOLEAN,
    status TEXT,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (user_id, trigger_type, trigger_id, package_name)
)

CREATE OR REPLACE TABLE user_device_hardware_log (
    user_id BIGINT,
    trigger_type TEXT,
    trigger_id BIGINT,
    android_id TEXT,
    android_serial_number TEXT,
    android_version TEXT,
    battery_capacity INT,
    bluetooth_address TEXT,
    country_iso TEXT,
    cpu_core INT,
    data_uploaded_at TIMESTAMP,
    device_id TEXT,
    device_id_slot_1 TEXT,
    device_id_slot_2 TEXT,
    device_id_type TEXT,
    device_model TEXT,
    device_storage INT,
    dual_sim BOOLEAN,
    google_ad_id TEXT,
    is_rooted BOOLEAN,
    max_cpu_frequency INT,
    number_of_camera INT,
    phone_number TEXT,
    screen_resolution TEXT,
    screen_size FLOAT,
    sd_card_storage INT,
    sensor_list ARRAY,
    subscriber_id TEXT,
    tala_version_code TEXT,
    tala_version_name TEXT,
    wlan_mac TEXT,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (user_id, trigger_type, trigger_id)
)

CREATE OR REPLACE TABLE user_settings_log (
    user_id BIGINT,
    trigger_type TEXT,
    trigger_id BIGINT,
    current_locale TEXT,
    data_collected_at TIMESTAMP,
    data_uploaded_at TIMESTAMP,
    default_language TEXT,
    default_locale TEXT,
    device_id TEXT,
    device_timezone TEXT,
    font_scale FLOAT,
    keyboard_type TEXT,
    mobile_country_code INT,
    mobile_network_code INT,
    navigation_type TEXT,
    touchscreen_type TEXT,
    user_accounts ARRAY,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (user_id, trigger_type, trigger_id)
)

CREATE OR REPLACE TABLE user_contacts_log (
    user_id BIGINT,
    trigger_type TEXT,
    trigger_id BIGINT,
    formatted_phone_number TEXT,
    contact_name TEXT,
    data_uploaded_at TIMESTAMP,
    device_id TEXT,
    last_contacted_at TIMESTAMP,
    phone_number TEXT,
    phone_type TEXT,
    times_contacted INT,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (user_id, trigger_type, trigger_id, formatted_phone_number)
)

CREATE OR REPLACE TABLE user_location_log (
    user_id BIGINT,
    trigger_type TEXT,
    trigger_id BIGINT,
    accuracy FLOAT,
    data_collected_at TIMESTAMP,
    data_uploaded_at TIMESTAMP,
    device_id TEXT,
    latitude FLOAT,
    longitude FLOAT,
    time_stayed BIGINT,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (user_id, trigger_type, trigger_id)
)

CREATE OR REPLACE TABLE user_phone_log (
    user_id BIGINT,
    trigger_type TEXT,
    trigger_id BIGINT,
    battery_level INT,
    data_collected_at TIMESTAMP,
    data_uploaded_at TIMESTAMP,
    device_id TEXT,
    elapsed_time BIGINT,
    neighboring_cell ARRAY,
    phone_type TEXT,
    roaming_status BOOLEAN,
    uptime BIGINT,
    wifi_status BOOLEAN,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (user_id, trigger_type, trigger_id)
)

CREATE OR REPLACE TABLE user_phone_numbers (
    user_id BIGINT,
    phone_numbers OBJECT,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (user_id)
)

CREATE OR REPLACE TABLE user_device_statistics (
    user_id BIGINT,
    trigger_type TEXT,
    trigger_id BIGINT,
    data_uploaded_at TIMESTAMP,
    device_id TEXT,
    sms_count INT,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (user_id, trigger_type, trigger_id)
)

CREATE OR REPLACE TABLE phone_number_devices (
    phone_number TEXT,
    device_ids OBJECT,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (phone_number)
)

CREATE OR REPLACE TABLE raw_sms_log (
    message_hash TEXT,
    content TEXT,
    device_message_id BIGINT,
    direction TEXT,
    formatted_phone_number TEXT,
    message_TIMESTAMP TIMESTAMP,
    phone_number TEXT,
    deleted_flag BOOLEAN,
    uploaded_timestamp TIMESTAMP,
    CONSTRAINT pk_prim_id PRIMARY KEY (message_hash)
)
