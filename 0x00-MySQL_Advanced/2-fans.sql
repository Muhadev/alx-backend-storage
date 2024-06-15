-- Task 2: Ranking country origins of bands by number of fans

-- Calculate the total number of fans per origin and rank them in descending order

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
