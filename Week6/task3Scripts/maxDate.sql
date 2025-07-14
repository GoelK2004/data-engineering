SELECT MAX(shipped_date) AS MaxDate
FROM sales.orders
WHERE shipped_date > '@{activity('LastWatermark').output.firstRow.LastWatermark}';