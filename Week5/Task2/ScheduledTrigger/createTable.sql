USE [bikeStoresRep];
GO

CREATE SCHEMA pr;
GO

CREATE TABLE pr.categories (
	category_id INT IDENTITY (1, 1) PRIMARY KEY,
	category_name VARCHAR (255) NOT NULL
);