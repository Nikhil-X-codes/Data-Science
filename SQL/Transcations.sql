USE sakila;

SET autocommit = 0;
SELECT * FROM actor;

INSERT INTO actor (first_name, last_name) VALUES ('John', 'Doe');

SELECT * FROM actor WHERE first_name = 'John' AND last_name = 'Doe';

Rollback;

INSERT INTO actor (first_name, last_name) VALUES ('John', 'Doe');
SELECT * FROM actor WHERE first_name = 'John' AND last_name = 'Doe';

commit;

