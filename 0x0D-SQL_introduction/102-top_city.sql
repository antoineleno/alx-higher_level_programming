-- Import the dabase from the file tempertures and perform some operations
use hbtn_0c_0
SELECT city, AVG(value) as avg_temp FROM temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
