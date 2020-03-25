SELECT salary * months AS totals, COUNT(*)
FROM Employee
GROUP BY totals
ORDER BY totals DESC
LIMIT 1;