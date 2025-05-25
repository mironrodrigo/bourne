CREATE KEYSPACE IF NOT EXISTS bourne
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 3};

CREATE TABLE IF NOT EXISTS bourne.profiles (
    customer_id UUID PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    phone TEXT,
    address TEXT,
    custom_attributes MAP<TEXT, TEXT>,
    identifiers MAP<TEXT, TEXT>
);

CREATE TABLE IF NOT EXISTS bourne.resolution_rules (
    tenant_id UUID PRIMARY KEY,
    default_attributes SET<TEXT>,
    custom_attributes SET<TEXT>,
    match_strategy TEXT
);