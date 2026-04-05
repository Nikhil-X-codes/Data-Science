CREATE DATABASE my_app_db;

USE my_app_db;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    age INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    product_name VARCHAR(100),
    amount DECIMAL(10,2),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);


INSERT INTO users (name, email, age)
VALUES 
('Nikhil', 'nikhil@example.com', 21),
('Rahul', 'rahul@example.com', 22);



INSERT INTO orders (user_id, product_name, amount)
VALUES
(1, 'Laptop', 55000.00),
(2, 'Phone', 20000.00);



select * from users;
select * from orders;


-- to show the name of foreign keys

SHOW CREATE TABLE orders;



-- to delete the foreign key constraint and refernce column

ALTER TABLE orders
DROP FOREIGN KEY orders_ibfk_1;


ALTER TABLE orders
DROP COLUMN user_id;


-- to add the foreign key constraint and reference column again


ALTER TABLE orders
ADD COLUMN user_id INT;


ALTER TABLE orders
ADD CONSTRAINT fk_user_orders
FOREIGN KEY (user_id)
REFERENCES users(user_id);

-- to update the reference column with the correct values we have to update it manually as we have deleted the column and added it again so it will be empty now

UPDATE orders
SET user_id = 1
WHERE order_id = 1;

UPDATE orders
SET user_id = 2
WHERE order_id = 2;




