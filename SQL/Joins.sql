USE my_app_db;


select * from users;
select * from orders;

INSERT INTO users (user_id, name, email, age)
VALUES (3, 'Amit', 'amit@gmail.com', 25);

INSERT INTO users (user_id, name, email, age)
VALUES (4, 'Suresh', 'sumit@gmail.com', 30);




-- inner join gives Returns only the matching rows from both tables.


SELECT users.name,users.email, orders.product_name, orders.amount
FROM users
INNER JOIN orders ON users.user_id = orders.user_id;



-- left join gives Returns all rows from the left table and the matching rows from the right table. If there is no match, the result is NULL on the right side.


SELECT users.name,users.email, orders.product_name, orders.amount
FROM users
LEFT JOIN orders ON users.user_id = orders.user_id;



-- right join gives Returns all rows from the right table and the matching rows from the left table. If there is no match, the result is NULL on the left side.


SELECT users.name,users.email, orders.product_name, orders.amount
FROM users
RIGHT JOIN orders ON users.user_id = orders.user_id;



CREATE TABLE admin_users (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    gender ENUM('Male', 'Female', 'Other'),
    date_of_birth DATE,
    salary INT
);


INSERT INTO admin_users (id, name, email, gender, date_of_birth, salary) VALUES
(101, 'Anil Kumar', 'anil@example.com', 'Male', '1985-04-12', 60000),
(102, 'Pooja Sharma', 'pooja@example.com', 'Female', '1992-09-20', 58000),
(103, 'Rakesh Yadav', 'rakesh@example.com', 'Male', '1989-11-05', 54000),
(104, 'Fatima Begum', 'fatima@example.com', 'Female', '1990-06-30', 62000);



SELECT name,email FROM users
UNION
SELECT name,email FROM admin_users;



SELECT name, 'User' AS role FROM users
UNION
SELECT name, 'Admin' AS role FROM admin_users;




-- self join is a technique where a table is joined with itself. It is used to compare rows within the same table or to find relationships between rows in the same table.

ALTER TABLE users
ADD COLUMN referred_by_id INT;

UPDATE users SET referred_by_id = 1 WHERE user_id IN (2, 3); 
UPDATE users SET referred_by_id = 2 WHERE user_id = 4;  


SELECT 
  a.user_id,
  a.name AS user_name,
  b.name AS referred_by
FROM users a
INNER JOIN users b ON a.referred_by_id = b.user_id;


