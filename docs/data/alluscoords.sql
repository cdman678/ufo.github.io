CREATE VIEW WeightedCoords AS
SELECT s.latitude,s.longitude,count(s.latitude)
FROM sighting s, location l
WHERE l.country='US' AND s.latitude = l.Latitude AND s.longitude = l.Longitude
GROUP BY s.latitude,s.longitude;
