SELECT
    RequestorSeniority,
    COUNT(*) AS TotalTickets
FROM tickets
GROUP BY RequestorSeniority
ORDER BY TotalTickets DESC;