SELECT
    FiledAgainst,
    Priority,
    COUNT(*) AS TotalTickets
FROM tickets
GROUP BY FiledAgainst, Priority
ORDER BY FiledAgainst;