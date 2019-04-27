SELECT state,count(state)
FROM location l, sighting s
WHERE s.longitude = l.Longitude AND s.latitude=l.Latitude AND l.country ='US' AND l.state !=''
GROUP BY state
ORDER BY count(state) DESC
LIMIT 5;