use my_app_db;

SHOW INDEXES FROM orders;

SELECT * from admin_users;

CREATE INDEX idx_data ON orders(order_date,amount);


DROP INDEX idx_data ON orders;



-- subquery: query inside query

select name,email,salary from admin_users where salary > (
SELECT AVG(salary) FROM admin_users
)




-- group by: group rows that have the same values into summary rows
-- rollup: add extra rows to the result set that represent subtotals and grand totals

SELECT gender, AVG(salary) AS avg_sal
FROM admin_users
GROUP BY gender with rollup;





-- having : filter groups based on a condition after grouping

select name,salary from admin_users
group BY name,salary 
having AVG(salary) > 50000;








