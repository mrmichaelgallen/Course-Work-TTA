SELECT * FROM [GRANT]

UPDATE [Grant] SET GrantName = '92 Per-cents %% team'
WHERE GrantID = '001'


-- example

UPDATE [Grant] SET GrantName = NULL
WHERE GrantID = '001'

-- Only the TRY or the CATCH will run, both can't

BEGIN TRY
	UPDATE [Grant] SET GrantName = '92 Per-cents %% team'
	WHERE GrantID = '001'
END TRY
BEGIN CATCH
	PRINT 'No Change was made'
END CATCH

-- Example of Catch

BEGIN TRY
	UPDATE [Grant] SET GrantName = NULL --Null can't work, but this is to show that the backup catch command deploys
	WHERE GrantID = '001'
END TRY
BEGIN CATCH
	PRINT 'No Change was made'
END CATCH

-- When doe the "Try Block" hand over execution to the "Catch Block"?

BEGIN TRY
	RAISERROR('Bad stuff', 16, 1)
END TRY
BEGIN CATCH
	PRINT 'Catch Ran'
	PRINT ERROR_MESSAGE() -- Tells to show 'Bad stuff' message above
	PRINT ERROR_SEVERITY() -- Shows the severity
END CATCH

-- Example