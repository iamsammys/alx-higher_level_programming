-- Lists all the cities of California
-- DML to list all cities of california tha can be found in the hbtn_0d_usa database
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'california')
ORDER BY cities.id ASC;
