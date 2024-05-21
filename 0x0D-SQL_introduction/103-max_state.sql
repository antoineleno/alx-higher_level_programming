-- Import the dump file to a database then perform some operation 
USE hbtn_0c_0
SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state ORDER BY state ASC;

