-- 8.Cities of California
SELECT cities.id, cities.name FROM cities, states
WHERE states.name = 'California' ORDER BY cities.id ASC
