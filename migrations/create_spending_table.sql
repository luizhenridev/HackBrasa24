CREATE TABLE IF NOT EXISTS "gasto"(
    spend_id UUID NOT NULL PRIMARY KEY,
    description_spend VARCHAR,
    value_spend FLOAT
    CONSTRAINT fk_user
        FOREIGN KEY(user_id)
        REFERENCES "user"(user_id)
        ON DELETE CASCADE
)