SELECT
    FiledAgainst,
    COUNT(*) AS TotalTickets
FROM tickets
GROUP BY FiledAgainst
ORDER BY TotalTickets DESC;