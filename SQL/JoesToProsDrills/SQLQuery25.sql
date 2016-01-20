CREATE SCHEMA [Allen] AUTHORIZATION [dbo]

SELECT * FROM Person.Person

SELECT * FROM HumanResources.EmployeePayHistory

SELECT * FROM Person.EmailAddress

SELECT * FROM Person.AddressType


CREATE PROC Allen.GetEmployeeByLastORFirstName @LastName nvarchar(30) = NULL, @FirstName nvarchar(30) = NULL
AS
	SELECT H.BusinessEntityID, P.PersonType, P.FirstName, P.LastName, H.Rate, A.EmailAddress
	From Person.Person AS P 
	Inner JOIN HumanResources.EmployeePayHistory AS H
	on P.BusinessEntityID = H.BusinessEntityID 
	Inner join Person.EmailAddress AS A
	ON H.BusinessEntityID = A.BusinessEntityID
	Where P.LastName = @LastName
	OR P.FirstName = @FirstName

EXEC Allen.GetEmployeeByLastORFirstName @FirstName = 'Rob'


--, @FirstName nvarchar(30) 
 --AND P.FirstName = @FirstName
