SELECT DATE(Power.updateTime), MAX(Power.northSupply), MAX(Power.northUsage),
  MAX(Power.centerSupply), MAX(Power.centerUsage), MAX(Power.southSupply),
  MAX(Power.southUsage), MAX(Power.eastSupply), MAX(Power.eastUsage)
FROM Power
WHERE DATE(Power.updateTime) BETWEEN '2016-10-01' AND '2017-06-30'
GROUP BY DATE(Power.updateTime)
