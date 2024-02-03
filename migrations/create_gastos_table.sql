CREATE TABLE IF NOT EXISTS "gasto"(
    gasto_id UUID NOT NULL PRIMARY KEY,
    descricao_gasto VARCHAR,
    valor_gasto FLOAT
    CONSTRAINT fk_user
        FOREIGN KEY(user_id)
        REFERENCES "user"(user_id)
        ON DELETE CASCADE
)