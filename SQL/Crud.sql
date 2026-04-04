use employees;

select * from employees


-- insertion operations

INSERT INTO employees (emp_no, birth_date, first_name, last_name, gender, hire_date) VALUES (500001, '1990-01-01', 'John', 'Doe', 'M', '2020-01-01');



-- read operations 
SELECT * FROM  employees WHERE gender != 'F';


SELECT * FROM employees WHERE birth_date IS NULL;


SELECT * FROM employees WHERE birth_date BETWEEN '1990-01-01' AND '2000-12-31';


SELECT * FROM employees  WHERE gender IN ('Other');


SELECT * FROM employees WHERE first_name LIKE '%a';


SELECT * FROM employees ORDER BY hire_date DESC;




-- update operations

UPDATE employees 
SET first_name = 'Jane',last_name = 'Smith'
WHERE emp_no = 500001;

SELECT * FROM employees WHERE emp_no = 500001;





-- delete operations

DELETE FROM employees
WHERE gender = 'M';

SELECT * FROM employees;







