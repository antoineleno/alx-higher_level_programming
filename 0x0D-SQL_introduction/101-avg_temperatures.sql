-- Import the dump file to a database then perform some operation 
USE hbtn_0c_0
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;

