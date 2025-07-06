CREATE OR ALTER PROCEDURE fl.ProcessLatestFile
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @file_path NVARCHAR(500);

    SELECT TOP 1 @file_path = file_path
    FROM fl.FileQueue
    WHERE processed = 0
    ORDER BY created_at DESC;

    IF @file_path IS NULL
    BEGIN
        PRINT 'No unprocessed files found.';
        RETURN;
    END

    BEGIN TRY
        TRUNCATE TABLE fl.stores;

        -- Import data from CSV
        DECLARE @sql NVARCHAR(MAX);
        SET @sql = '
            BULK INSERT fl.stores
            FROM ''' + @file_path + '''
            WITH (
                FIELDTERMINATOR = '','',
                ROWTERMINATOR = ''\n'',
                FIRSTROW = 2
            );
        ';
        EXEC sp_executesql @sql;

        UPDATE fl.FileQueue SET processed = 1 WHERE file_path = @file_path;

        PRINT 'File imported: ' + @file_path;
    END TRY
    BEGIN CATCH
        PRINT 'Error: ' + ERROR_MESSAGE();
    END CATCH
END;
GO
