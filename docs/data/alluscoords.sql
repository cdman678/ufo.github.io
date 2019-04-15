SELECT s.latitude,s.longitude
FROM sighting s, location l
WHERE l.country='US' AND s.latitude = l.Latitude AND s.longitude = l.Longitude;