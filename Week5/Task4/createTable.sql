CREATE SCHEMA sl;
GO

CREATE TABLE sl.staff (
    [staff_id] INT,
    [first_name] VARCHAR(50),
    [last_name] VARCHAR(50),
    [email] VARCHAR(255),
    [phone] VARCHAR(25),
    [active] TINYINT,
    [store_id] INT,
    [manager_id] INT
);
