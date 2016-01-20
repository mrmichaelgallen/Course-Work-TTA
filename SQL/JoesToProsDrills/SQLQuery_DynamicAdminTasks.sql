BACKUP DATABASE JProCo TO DISK = 'c:\Joes2Pros\JProCo.bak'
GO

-- History of Backup files

-- To PEINT

DECLARE @DbName VARCHAR(100)
SET @DbName = 'dbBasics'
DECLARE @Path VARCHAR(100) = '''C:\Joes2Pros\' + @DbName + '.bak'''
SELECT @Path
PRINT ('BACKUP DATABASE dbBasics TO DISK = ' + @Path ) -- USE PRINT TO SHOW HOW well item concantenated

-- To EXEC

DECLARE @DbName VARCHAR(100)
SET @DbName = 'dbBasics'
DECLARE @Path VARCHAR(100) = '''C:\Joes2Pros\' + @DbName + '.bak'''
EXEC ('BACKUP DATABASE dbBasics TO DISK = ' + @Path )

-- Making it dynamic regardeless of the name. Ex. above on last line points to specific unit, while below it no longer does

DECLARE @DbName VARCHAR(100)
SET @DbName = 'dbMovie'
DECLARE @Path VARCHAR(100) = '''C:\Joes2Pros\' + @DbName + '.bak'''
DECLARE @Command VARCHAR(100) = 'BACKUP DATABASE ' + @DbName + ' TO DISK = ' + @Path
EXEC (@Command)

-- Time to backup JProCo, stamp with dates, I also added underscore

DECLARE @DbName VARCHAR(100)
SET @DbName = 'dbMovie'
DECLARE @Date VARCHAR (100) = '20012June01'
DECLARE @Path VARCHAR(100) = '''C:\Joes2Pros\' + @DbName + '_' + @Date + '.bak'''
DECLARE @Command VARCHAR(100) = 'BACKUP DATABASE ' + @DbName + ' TO DISK = ' + @Path
EXEC (@Command)


-- Lab 3.3 Dynamic Admin Tasks

DECLARE @DbName VARCHAR(100)
SET @DbName = 'dbBasics'
DECLARE @Date VARCHAR (100) = '2012June01'
DECLARE @Path VARCHAR(100) = '''C:\Joes2Pros\' + @DbName + '_' + @Date + '.bak'''
DECLARE @Command VARCHAR(100) = 'BACKUP DATABASE ' + @DbName + ' TO DISK = ' + @Path
EXEC (@Command)

-- Processed 192 pages for database 'dbBasics', file 'dbBasics' on file 1.
-- Processed 1 pages for database 'dbBasics', file 'dbBasics_log' on file 1.
-- BACKUP DATABASE successfully processed 193 pages in 0.390 seconds (3.866 MB/sec).
