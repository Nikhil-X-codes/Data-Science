CREATE DATABASE startersql;

USE startersql;


CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    gender ENUM('Male', 'Female', 'Other'),
    date_of_birth DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO users (name, email, gender, date_of_birth)
VALUES
('John Doe', 'john.doe@example.com', 'Male', '1992-03-12'),
('Emma Watson', 'emma.watson@example.com', 'Female', '1998-07-21'),
('Rahul Sharma', 'rahul.sharma@example.com', 'Male', '1995-11-05'),
('Priya Singh', 'priya.singh@example.com', 'Female', '1997-01-18'),
('Alex Taylor', 'alex.taylor@example.com', 'Other', '2000-09-30'),
('Sneha Patel', 'sneha.patel@example.com', 'Female', '1996-04-25'),
('Michael Brown', 'michael.brown@example.com', 'Male', '1993-12-14'),
('Sara Khan', 'sara.khan@example.com', 'Female', '1999-06-08');

RENAME TABLE users TO customers;


ALTER TABLE customers ADD COLUMN is_active BOOLEAN DEFAULT TRUE;

ALTER TABLE customers DROP COLUMN name;

ALTER TABLE customers MODIFY COLUMN email VARCHAR(150);

ALTER TABLE customers MODIFY COLUMN gender ENUM('Male', 'Female', 'Other') AFTER id;

SELECT * FROM customers;


ALTER TABLE customers 
MODIFY date_of_birth DATE NOT NULL;















