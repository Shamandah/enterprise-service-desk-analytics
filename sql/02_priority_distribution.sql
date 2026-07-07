SELECT
    TicketType,
    COUNT(*) AS TotalTickets,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM tickets), 2) AS Percentage
FROM tickets
GROUP BY TicketType;