CREATE TABLE IF NOT EXISTS "spending"(
    spend_id UUID NOT NULL PRIMARY KEY,
    user_id INT not null,
    description_spend VARCHAR,
    value_spend FLOAT,
    CONSTRAINT fk_user FOREIGN KEY(user_id) REFERENCES "user"(user_id) ON DELETE CASCADE
);