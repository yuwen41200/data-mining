SELECT A.日期, `北部（板橋）最高溫度`, `中部（臺中）最高溫度`, `南部（高雄）最高溫度`, `東部（花蓮）最高溫度`
FROM (
SELECT DATE(逐時觀測.時間) AS 日期, MAX(逐時觀測.溫度) AS `北部（板橋）最高溫度`
FROM 逐時觀測
WHERE 逐時觀測.測站 = 'BANQIAO,板橋' AND DATE(逐時觀測.時間) BETWEEN '2016-10-01' AND '2017-06-30'
GROUP BY DATE(逐時觀測.時間)
) A
INNER JOIN (
SELECT DATE(逐時觀測.時間) AS 日期, MAX(逐時觀測.溫度) AS `中部（臺中）最高溫度`
FROM 逐時觀測
WHERE 逐時觀測.測站 = 'TAICHUNG,臺中' AND DATE(逐時觀測.時間) BETWEEN '2016-10-01' AND '2017-06-30'
GROUP BY DATE(逐時觀測.時間)
) B ON A.日期 = B.日期
INNER JOIN (
SELECT DATE(逐時觀測.時間) AS 日期, MAX(逐時觀測.溫度) AS `南部（高雄）最高溫度`
FROM 逐時觀測
WHERE 逐時觀測.測站 = 'KAOHSIUNG,高雄' AND DATE(逐時觀測.時間) BETWEEN '2016-10-01' AND '2017-06-30'
GROUP BY DATE(逐時觀測.時間)
) C ON A.日期 = C.日期
INNER JOIN (
SELECT DATE(逐時觀測.時間) AS 日期, MAX(逐時觀測.溫度) AS `東部（花蓮）最高溫度`
FROM 逐時觀測
WHERE 逐時觀測.測站 = 'HUALIEN,花蓮' AND DATE(逐時觀測.時間) BETWEEN '2016-10-01' AND '2017-06-30'
GROUP BY DATE(逐時觀測.時間)
) D ON A.日期 = D.日期
