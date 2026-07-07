SELECT
    Severity,
    COUNT(*) AS TotalTickets
FROM tickets
GROUP BY Severity
ORDER BY TotalTickets DESC;