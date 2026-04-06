use my_app_db;

show tables;


-- CREATE PROCEDURE select_users()
-- BEGIN
--     SELECT * FROM users;
-- END;

call select_users();





-- CREATE PROCEDURE add_user(
--     IN p_name VARCHAR(100),
--     IN p_email VARCHAR(100),
--     IN p_age INT
-- )
-- BEGIN
--     INSERT INTO users (name, email, age)
--     VALUES (p_name, p_email, p_age);
-- END;

CALL add_user('Ravi', 'ravi@gmail.com', 24);



SHOW PROCEDURE STATUS WHERE Db = 'my_app_db';

DROP PROCEDURE IF EXISTS select_users;

