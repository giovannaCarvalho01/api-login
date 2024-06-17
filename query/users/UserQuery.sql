CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    login VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(11) NOT NULL,
    code_sales_person VARCHAR(6) UNIQUE,
    type_sales VARCHAR(20),
    id_profile INTEGER REFERENCES profile(id),
    tbl_price TEXT[]
)
