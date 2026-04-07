use my_app_db;

CREATE TABLE user_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    name VARCHAR(100),
    created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TRIGGER after_user_insert
AFTER INSERT ON users
FOR EACH ROW
BEGIN
    INSERT INTO user_log (user_id, name)
    VALUES (NEW.user_id, NEW.name);
END


INSERT INTO users (name, email, age)
VALUES ('Nikhil', 'nik@gmail.com', 25);


SELECT * FROM user_log;


DROP TRIGGER IF EXISTS after_user_insert;


INSERT INTO users (name, email, age)
VALUES ('rakhi', 'rakhi@gmail.com', 28);