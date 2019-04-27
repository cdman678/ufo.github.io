SELECT city,state,count(city)
FROM location l, sighting s
WHERE s.longitude = l.Longitude AND s.latitude=l.Latitude AND l.country ='US'
GROUP BY city
ORDER BY count(city) DESC
LIMIT 5;