SELECT * FROM sales.orders
WHERE shipped_date > '@{activity('LastWatermark').output.firstRow.LastWatermark}';