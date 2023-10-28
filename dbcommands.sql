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

INSERT INTO users (first_name, last_name, email, username, password,type)
VALUES ('John', 'Doe', 'email@email.com', 'test', 'ptest','student');



CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    level INTEGER  DEFAULT 1,
    experience DEFAULT 0,
    teacher DEFAULT NULL
);

CREATE TABLE educators (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    students INTEGER DEFAULT 0
);

CREATE TABLE educator_to_learner (
    id SERIAL PRIMARY KEY,
    educator_id INTEGER NOT NULL,
    learner_id INTEGER NOT NULL,
    FOREIGN KEY (educator_id) REFERENCES educators(id),
    FOREIGN KEY (learner_id) REFERENCES learners(id)
);

CREATE TABLE feedback(
    feedback_id INTEGER PRIMARY KEY,
    giver_username VARCHAR(255) NOT NULL,
    feedback_text TEXT
);

CREATE TRIGGER update_students AFTER INSERT ON users 
BEGIN
    CASE WHEN NEW.type = 'student' THEN
        INSERT INTO educators (username) VALUES (NEW.username);
    END CASE;
   
END;





