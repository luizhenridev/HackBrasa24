CREATE TABLE IF NOT EXISTS "user" (
    user_id UUID NOT NULL,
    name TEXT,
    cellphone_number TEXT,
    created_at DATE,
    CONSTRAINT user_id_pkey PRIMARY KEY (user_id)
);