SELECT
    Priority,
    ROUND(AVG("Max Day"),2) AS AverageTargetDays,
    MIN("Max Day") AS MinimumDays,
    MAX("Max Day") AS MaximumDays
FROM tickets
GROUP BY Priority;