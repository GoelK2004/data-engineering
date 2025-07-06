USE [bikeStoresRep];
GO

CREATE OR ALTER PROCEDURE CopyData
AS
BEGIN
    INSERT INTO pr.categories (category_name)
    SELECT category_name
    FROM bikeStores.production.categories bsc
    WHERE bsc.category_id NOT IN (
        SELECT category_id from pr.categories
    );
END;
