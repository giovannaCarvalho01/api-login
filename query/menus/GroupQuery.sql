CREATE TABLE group_profile (
    id SERIAL PRIMARY KEY,
    group_description VARCHAR(255) NOT NULL,
    id_profile INTEGER REFERENCES profile(id)
)