SELECT
    Severity,
    Priority,
    COUNT(*) AS TotalTickets
FROM tickets
GROUP BY Severity, Priority
ORDER BY Severity, Priority;