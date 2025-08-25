CREATE DATABASE face_recognition;
USE face_recognition;

CREATE TABLE users(
	name_user varchar(50) NOT NULL,
    id_user int NOT NULL,
    age_user int NOT NULL,
    UNIQUE KEY (id_user),
    PRIMARY KEY (id_user)
);

SELECT * FROM users;
DELETE FROM users where id_user = 1
