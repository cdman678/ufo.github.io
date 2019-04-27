SELECT shape, count(shape)
FROM description
GROUP BY shape
ORDER BY count(shape) DESC
LIMIT 5;