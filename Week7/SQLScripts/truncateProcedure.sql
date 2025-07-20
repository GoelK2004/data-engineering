CREATE PROCEDURE truncateData
AS
BEGIN
    TRUNCATE TABLE cust.mstr;
    TRUNCATE TABLE cust.mstch;
    TRUNCATE TABLE cust.ecom;
END;