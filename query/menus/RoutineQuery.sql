CREATE TABLE routine (
    id SERIAL PRIMARY KEY,
    routine_description VARCHAR(255) NOT NULL,
    id_group INTEGER REFERENCES group_profile(id)
)