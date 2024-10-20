-- Select all elements of a table
-- after sorting them with 'order by'

SELECT origin, SUM(fans) AS nb_fans FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
