use dbBasics
use JProCo
SELECT * FROM Employee

-- Simple query

SELECT * FROM MgmtTraining

-- Code to Print strings below

DECLARE @SELECT NVARCHAR(50) = 'SELECT * '
DECLARE @FROM NVARCHAR(50) = 'FROM MgmtTraining'
PRINT (@SELECT + @FROM)

-- Below is how to get above script to run dynamically

DECLARE @SELECT NVARCHAR(50) = 'SELECT * '
DECLARE @FROM NVARCHAR(50) = 'FROM MgmtTraining'
EXEC (@SELECT + @FROM)

-- Example

DECLARE @Query NVARCHAR(50)
DECLARE @TableName NVARCHAR(50)
SET @Query = 'SELECT * FROM '
SET @TableName = 'MgmtTraining'
EXEC (@Query + @TableName)


-- NOTE: You can not concatenate an Object and a string(s)

CREATE PROC GeneralQuery @TableName NVARCHAR(50)
AS
	SELECT * FROM + @TableName
GO

-- Example

CREATE PROC GeneralQuery @TableName NVARCHAR(50)
AS
	DECLARE @SQL NVARCHAR(1000)
	SET @SQL = 'SELECT * FROM ' + @TableName
	EXEC (@SQL)
GO

-- The StoreProcedure

EXEC GeneralQuery 'MgmtTraining'

-- with a different variable using the StoreProdecure above

EXEC GeneralQuery 'Location'

-- Lab 3.1 Lab - Skill Check #1

CREATE PROC GeneralDatabase @DbName NVARCHAR(50)
AS

	DECLARE @SQL NVARCHAR(1000)
	SET @SQL = 'CREATE DATABASE ' + @DbName
	EXEC (@SQL)
	
GO

-- Script to below to run code above

EXEC GeneralDatabase 'SkillCheckCh3'

-- Lab 3.1 Lab - Skill Check #2

CREATE PROC DropGeneralDatabase @DbName NVARCHAR(50)
AS

	DECLARE @SQL NVARCHAR(1000)
	SET @SQL = 'DROP DATABASE ' + @DbName
	EXEC (@SQL)
	
GO

-- Script to below to run code above

EXEC DropGeneralDatabase 'SkillCheckCh3'

-- Lab 3.1 Lab - Skill Check #3

	DECLARE @SQLQuery NVARCHAR(1000)
	DECLARE @List NVARCHAR(100)
	SET @SQLQuery = 'SELECT * FROM Employee WHERE EmpID IN ('+ @List +')'
	EXEC (@SQLQuery)



