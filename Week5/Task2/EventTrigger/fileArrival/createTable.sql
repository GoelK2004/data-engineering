CREATE SCHEMA fl;
GO

IF OBJECT_ID('fl.stores', 'U') IS NULL
BEGIN
    CREATE TABLE fl.stores (
    	store_id INT IDENTITY (1, 1) PRIMARY KEY,
	    store_name VARCHAR (255) NOT NULL,
	    phone VARCHAR (25),
	    email VARCHAR (255),
	    street VARCHAR (255),
	    city VARCHAR (255),
	    state VARCHAR (10),
	    zip_code VARCHAR (5)
    );
END;
GO

IF OBJECT_ID('dbo.FileQueue', 'U') IS NULL
BEGIN
    CREATE TABLE fl.FileQueue (
        id INT IDENTITY(1,1) PRIMARY KEY,
        file_path NVARCHAR(500),
        processed BIT DEFAULT 0,
        created_at DATETIME DEFAULT GETDATE()
    );
END;

