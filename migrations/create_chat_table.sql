CREATE TABLE IF NOT EXISTS chat(
    chat_id UUID NOT NULL,
    message_id UUID UNIQUE NOT NULL,
    body_message TEXT,
    user_id UUID,
    message_date DATE,
    CONSTRAINT chat_id_pkey PRIMARY KEY (chat_id),
    CONSTRAINT message_id_unique UNIQUE (message_id),
    CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES "user"(user_id)

);