-- To run all commands type out 
-- cat dbcommands.sql | sqlite3 codeventure.db
-- This will execute all commands in the file


CREATE TABLE users (
    id INTEGER   PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    type VARCHAR(255) NOT NULL
    
);

INSERT INTO users (first_name, last_name, email, username, password)
VALUES ('John', 'Doe', 'email@email.com', 'test', 'ptest');


