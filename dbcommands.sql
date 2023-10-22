-- To run all commands type out 
-- cat dbcommands.sql | sqlite3 codeventure.db
-- This will execute all commands in the file
create DATABASE codeventure;


CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

