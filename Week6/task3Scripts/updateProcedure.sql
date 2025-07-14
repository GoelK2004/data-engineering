CREATE PROCEDURE UpdateWatermark
    @TableName NVARCHAR(100),
    @NewWatermark DATETIME
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE WatermarkControl
    SET LastWatermark = @NewWatermark
    WHERE TableName = @TableName;
END
