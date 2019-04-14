SELECT country, count(country)
FROM sighting s , location l
WHERE l.Latitude = s.latitude and l.Longitude = s.longitude and country!='US'
GROUP BY country
ORDER BY count(country) DESC
LIMIT 5;