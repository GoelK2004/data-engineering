CREATE TRIGGER
	pr.trg_category_audit
ON
	pr.categories
AFTER INSERT, DELETE
AS
BEGIN
	SET NOCOUNT ON;
	INSERT INTO pr.category_audits(
		category_id,
		category_name,
		updated_at,
		operation
	)
	SELECT
		i.category_id,
		category_name,
		GETDATE(),
		'INS'
	FROM
		inserted as i
	UNION ALL
	SELECT
		d.category_id,
		category_name,
		GETDATE(),
		'DEL'
	FROM
		deleted as d;
END