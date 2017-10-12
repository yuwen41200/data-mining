SELECT 'highest' AS Item, MAX(逐時觀測.溫度) AS Temperature
FROM 逐時觀測
WHERE DATE(逐時觀測.時間) BETWEEN '2016-10-01' AND '2017-06-30'
UNION
SELECT 'lowest' AS Item, MIN(逐時觀測.溫度) AS Temperature
FROM 逐時觀測
WHERE DATE(逐時觀測.時間) BETWEEN '2016-10-01' AND '2017-06-30'
