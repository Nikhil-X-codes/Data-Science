use employees

select * from salaries


SELECT MIN(salary) AS min_salary, MAX(salary) AS max_salary FROM salaries;

SELECT AVG(salary) AS avg_salary FROM salaries;

SELECT COUNT(*) AS total_salaries FROM salaries;


SELECT gender, AVG(salary) AS avg_salary
FROM users
GROUP BY gender;


SELECT NOW();

SELECT CONCAT(first_name, ' <', last_name, '>') AS user_contact FROM employees;


SELECT name, YEAR(date_of_birth) AS birth_year FROM users;


SELECT name, TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) AS age FROM users;


SELECT name, gender,
       IF(gender = 'Female', 'Yes', 'No') AS is_female
FROM users;


