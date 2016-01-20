CREATE PROCEDURE uspGetAddress
AS
Select * from AdventureWorks2008R2.Person.Address
Go

EXEC uspGetAddress

CREATE PROCEDURE uspGetAddress @City nvarchar(30)
AS
SELECT * 
FROM AdventureWorks2008R2.Person.Address
WHERE City = @City
GO

EXEC uspGetAddress @City = 'New York'


CREATE PROCEDURE uspGetAddress @City nvarchar(30) = NULL
AS
SELECT *
FROM AdventureWorks2008R2.Person.Address
WHERE City = @City
GO


-- this procedure gets a list of addresses based 
-- on the city value that is passed
CREATE PROCEDURE uspGetAddress @City nvarchar(30) = NULL, @AddressLine1 nvarchar(60) = NULL
AS
SELECT *
FROM AdventureWorks2008R2.Person.Address
WHERE City = ISNULL(@City,City)
AND AddressLine1 LIKE '%' + ISNULL(@AddressLine1 ,AddressLine1) + '%'
GO

CREATE PROCEDURE uspGetAddressCount @City nvarchar(30), @AddressCount int OUTPUT
AS
SELECT @AddressCount = count(*) 
FROM AdventureWorks2008R2.Person.Address 
WHERE City = @City

DECLARE @AddressCount int
EXEC uspGetAddress @City = 'Calgary', @AddressCount = @AddressCount Output
SELECT @AddressCount

CREATE SCHEMA [Communications] AUTHORIZATION [dbo]

CREATE PROCEDURE Communications.uspGetAddressCount @City nvarchar(30), @AddressCount int OUTPUT
AS
SELECT @AddressCount = count(*) 
FROM AdventureWorks2008R2.Person.Address 
WHERE City = @City





CREATE PROCEDURE uspTryCatchTest
AS
BEGIN TRY
    SELECT 1/0
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS ErrorNumber
     ,ERROR_SEVERITY() AS ErrorSeverity
     ,ERROR_STATE() AS ErrorState
     ,ERROR_PROCEDURE() AS ErrorProcedure
     ,ERROR_LINE() AS ErrorLine
     ,ERROR_MESSAGE() AS ErrorMessage;
END CATCH



-- using SET NOCOUNT ON 
CREATE PROCEDURE uspIamNotCounting @City nvarchar(30)
AS
SET NOCOUNT ON
SELECT * 
FROM AdventureWorks2008R2.Person.Address
WHERE City = @City
GO

EXEC uspGetAddress @City = 'New York'

